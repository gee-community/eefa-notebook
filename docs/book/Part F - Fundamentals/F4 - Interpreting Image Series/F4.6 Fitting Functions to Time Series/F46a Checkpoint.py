import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F4.6 Fitting Functions to Time Series
#  Checkpoint:   F46a
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
Map
