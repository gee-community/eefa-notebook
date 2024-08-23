import ee
import math
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F4.6 Fitting Functions to Time Series
#  Checkpoint:   F46c
#  Authors:      Andréa Puzzi Nicolau, Karen Dyson, Biplov Bhandari, David Saah,
#                Nicholas Clinton
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##########/ Sections 1 & 2 ##############/


# Define function to mask clouds, scale, and add variables
# (NDVI, time and a constant) to Landsat 8 imagery.
def maskScaleAndAddVariable(image):
    # Bit 0 - Fill
    # Bit 1 - Dilated Cloud
    # Bit 2 - Cirrus
    # Bit 3 - Cloud
    # Bit 4 - Cloud Shadow
    qaMask = image.select("QA_PIXEL").bitwiseAnd(parseInt("11111", 2)).eq(0)
    saturationMask = image.select("QA_RADSAT").eq(0)

    # Apply the scaling factors to the appropriate bands.
    opticalBands = image.select("SR_B.").multiply(0.0000275).add(-0.2)
    thermalBands = image.select("ST_B.*").multiply(0.00341802).add(149.0)

    # Replace the original bands with the scaled ones and apply the masks.
    img = (
        image.addBands(opticalBands, None, True)
        .addBands(thermalBands, None, True)
        .updateMask(qaMask)
        .updateMask(saturationMask)
    )
    imgScaled = image.addBands(img, None, True)

    # Now we start to add variables of interest.
    # Compute time in fractional years since the epoch.
    date = ee.Date(image.get("system:time_start"))
    years = date.difference(ee.Date("1970-01-01"), "year")
    # Return the image with the added bands.
    return (
        imgScaled.addBands(
            imgScaled.normalizedDifference(["SR_B5", "SR_B4"]).rename("NDVI")
        )
        .addBands(ee.Image(years).rename("t"))
        .float()
        .addBands(ee.Image.constant(1))
    )


# Import point of interest over California, USA.
roi = ee.Geometry.Point([-121.059, 37.9242])

# Import the USGS Landsat 8 Level 2, Collection 2, Tier 1 image collection),
# filter, mask clouds, scale, and add variables.
landsat8sr = (
    ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
    .filterBounds(roi)
    .filterDate("2013-01-01", "2018-01-01")
    .map(maskScaleAndAddVariable)
)

# Set map center over the ROI.
Map.centerObject(roi, 6)

# Plot a time series of NDVI at a single location.
landsat8Chart = (
    ui.Chart.image.series(landsat8sr.select("NDVI"), roi)
    .setChartType("ScatterChart")
    .setOptions(
        {
            "title": "Landsat 8 NDVI time series at ROI",
            "lineWidth": 1,
            "pointSize": 3,
        }
    )
)
print(landsat8Chart)

# Plot a time series of NDVI with a linear trend line
# at a single location.
landsat8ChartTL = (
    ui.Chart.image.series(landsat8sr.select("NDVI"), roi)
    .setChartType("ScatterChart")
    .setOptions(
        {
            "title": "Landsat 8 NDVI time series at ROI",
            "trendlines": {"0": {"color": "CC0000"}},
            "lineWidth": 1,
            "pointSize": 3,
        }
    )
)
print(landsat8ChartTL)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

##########/ Section 3 ##############/

# List of the independent variable names
independents = ee.List(["constant", "t"])

# Name of the dependent variable.
dependent = ee.String("NDVI")

# Compute a linear trend.  This will have two bands: 'residuals' and
# a 2x1 (Array Image) band called 'coefficients'.
# (Columns are for dependent variables)
trend = landsat8sr.select(independents.add(dependent)).reduce(
    ee.Reducer.linearRegression(independents.length(), 1)
)
Map.addLayer(trend, {}, "trend array image")

# Flatten the coefficients into a 2-band image.
coefficients = (
    trend.select("coefficients").arrayProject([0]).arrayFlatten([independents])
)
Map.addLayer(coefficients, {}, "coefficients image")

# Compute a detrended series.


def func_zcs(image):
    return (
        image.select(dependent)
        .subtract(image.select(independents).multiply(coefficients).reduce("sum"))
        .rename(dependent)
        .copyProperties(image, ["system:time_start"])
    )


detrended = landsat8sr.map(func_zcs)


# Plot the detrended results.
detrendedChart = ui.Chart.image.series(detrended, roi, None, 30).setOptions(
    {
        "title": "Detrended Landsat time series at ROI",
        "lineWidth": 1,
        "pointSize": 3,
        "trendlines": {"0": {"color": "CC0000"}},
    }
)
print(detrendedChart)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

##########/ Section 4 ##############/

# Use these independent variables in the harmonic regression.
harmonicIndependents = ee.List(["constant", "t", "cos", "sin"])

# Add harmonic terms as new image bands.


def func_yrj(image):
    timeRadians = image.select("t").multiply(2 * math.pi)
    return image.addBands(timeRadians.cos().rename("cos")).addBands(
        timeRadians.sin().rename("sin")
    )


harmonicLandsat = landsat8sr.map(func_yrj)


# Fit the model.
harmonicTrend = harmonicLandsat.select(harmonicIndependents.add(dependent)).reduce(
    ee.Reducer.linearRegression(harmonicIndependents.length(), 1)
)

# Turn the array image into a multi-band image of coefficients.
harmonicTrendCoefficients = (
    harmonicTrend.select("coefficients")
    .arrayProject([0])
    .arrayFlatten([harmonicIndependents])
)

# Compute fitted values.


def func_xur(image):
    return image.addBands(
        image.select(harmonicIndependents)
        .multiply(harmonicTrendCoefficients)
        .reduce("sum")
        .rename("fitted")
    )


fittedHarmonic = harmonicLandsat.map(func_xur)


# Plot the fitted model and the original data at the ROI.
print(
    ui.Chart.image.series(
        fittedHarmonic.select(["fitted", "NDVI"]), roi, ee.Reducer.mean(), 30
    )
    .setSeriesNames(["NDVI", "fitted"])
    .setOptions(
        {
            "title": "Harmonic model: original and fitted values",
            "lineWidth": 1,
            "pointSize": 3,
        }
    )
)

# Compute phase and amplitude.
phase = (
    harmonicTrendCoefficients.select("sin")
    .atan2(harmonicTrendCoefficients.select("cos"))
    .unitScale(-math.pi, math.pi)
)

amplitude = (
    harmonicTrendCoefficients.select("sin")
    .hypot(harmonicTrendCoefficients.select("cos"))
    .multiply(5)
)

# Compute the mean NDVI.
meanNdvi = landsat8sr.select("NDVI").mean()

# Use the HSV to RGB transformation to display phase and amplitude.
rgb = ee.Image.cat(
    [
        phase,  # hue
        amplitude,  # saturation (difference from white)
        meanNdvi,  # value (difference from black)
    ]
).hsvToRgb()

Map.addLayer(rgb, {}, "phase (hue), amplitude (sat), ndvi (val)")

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

Map
