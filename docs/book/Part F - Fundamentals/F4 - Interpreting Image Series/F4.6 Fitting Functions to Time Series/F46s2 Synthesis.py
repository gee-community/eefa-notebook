import ee 
import math
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F4.6 Fitting Functions to Time Series
#  Checkpoint:   F46s2
#  Authors:      Andréa Puzzi Nicolau, Karen Dyson, Biplov Bhandari, David Saah,
#                Nicholas Clinton
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Satellite basemap.
Map.setOptions('SATELLITE')

# Define roi, a point over the Brazilian Amazon.
roi = ee.Geometry.Point([-59.985146, -2.871413])

# Add the point to the map.
Map.addLayer(roi, {
    'color': 'red'
}, 'roi')
Map.centerObject(roi, 16)

# The dependent variable we are modeling.
dependent = 'NDVI'

# The number of cycles per year to model.
harmonics = 1

# Make a list of harmonic frequencies to model.
# These also serve as band name suffixes.
harmonicFrequencies = ee.List.sequence(1, harmonics)

# Function to get a sequence of band names for harmonic terms.
def getNames(base, list):

def func_xyi(i):
        return ee.String(base).cat(ee.Number(i).int())

    return ee.List(list).map(func_xyi)





# Construct lists of names for the harmonic terms.
cosNames = getNames('cos_', harmonicFrequencies)
sinNames = getNames('sin_', harmonicFrequencies)

# Independent variables.
independents = ee.List(['constant', 't']) \
    .cat(cosNames).cat(sinNames)

# Define function to mask clouds, scale, and add variables
# (NDVI, time and a constant) to Landsat 8 imagery.
def maskScaleAndAddVariable(image):
    # Bit 0 - Fill
    # Bit 1 - Dilated Cloud
    # Bit 2 - Cirrus
    # Bit 3 - Cloud
    # Bit 4 - Cloud Shadow
    qaMask = image.select('QA_PIXEL').bitwiseAnd(parseInt('11111',
        2)).eq(0)
    saturationMask = image.select('QA_RADSAT').eq(0)

    # Apply the scaling factors to the appropriate bands.
    opticalBands = image.select('SR_B.').multiply(0.0000275).add(-
        0.2)
    thermalBands = image.select('ST_B.*').multiply(0.00341802) \
        .add(149.0)

    # Replace the original bands with the scaled ones and apply the masks.
    img = image.addBands(opticalBands, None, True) \
        .addBands(thermalBands, None, True) \
        .updateMask(qaMask) \
        .updateMask(saturationMask)
    imgScaled = image.addBands(img, None, True)

    # Now we start to add variables of interest.
    # Compute time in fractional years since the epoch.
    date = ee.Date(image.get('system:time_start'))
    years = date.difference(ee.Date('1970-01-01'), 'year')
    timeRadians = ee.Image(years.multiply(2 * math.pi))
    # Return the image with the added bands.
    return imgScaled \
        .addBands(imgScaled.normalizedDifference(['SR_B5', 'SR_B4']) \
            .rename('NDVI')) \
        .addBands(timeRadians.rename('t')) \
        .float() \
        .addBands(ee.Image.constant(1))


# Function to compute the specified number of harmonics
# and add them as bands.  Assumes the time band is present.
def addHarmonics(freqs):
    return function(image) {
        # Make an image of frequencies.
        frequencies = ee.Image.constant(freqs)
        # This band should represent time in radians.
        time = ee.Image(image).select('t')
        # Get the cosine terms.
        cosines = time.multiply(frequencies).cos() \
            .rename(cosNames)
        # Get the sin terms.
        sines = time.multiply(frequencies).sin() \
            .rename(sinNames)
        return image.addBands(cosines).addBands(sines)
    }


# Import the USGS Landsat 8 Level 2, Collection 2, Tier 1 image collection),
# and map functions.
harmonicLandsat = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') \
    .filterBounds(roi) \
    .map(maskScaleAndAddVariable) \
    .map(addHarmonics(harmonicFrequencies))

# Filter for the pre-disturbance period.
harmonicLandsatPre = harmonicLandsat.filterDate('2013-01-01',
    '2014-12-12')

# The output of the regression reduction is a 4x1 array image.
harmonicTrendPre = harmonicLandsatPre \
    .select(independents.add(dependent)) \
    .reduce(ee.Reducer.linearRegression(independents.length(), 1))

# Turn the array image into a multi-band image of coefficients.
harmonicTrendCoefficientsPre = harmonicTrendPre.select(
        'coefficients') \
    .arrayProject([0]) \
    .arrayFlatten([independents])

# Compute fitted values.

def func_cvr(image):
    return image.addBands(
        image.select(independents) \
        .multiply(harmonicTrendCoefficientsPre) \
        .reduce('sum') \
        .rename('fitted'))

fittedHarmonicPre = harmonicLandsatPre.map(func_cvr)








# Filter for the disturbance period.
harmonicLandsatDist = harmonicLandsat.filterDate('2014-12-13',
    '2019-01-01')

# The output of the regression reduction is a 4x1 array image.
harmonicTrendDist = harmonicLandsatDist \
    .select(independents.add(dependent)) \
    .reduce(ee.Reducer.linearRegression(independents.length(), 1))

# Turn the array image into a multi-band image of coefficients.
harmonicTrendCoefficientsDist = harmonicTrendDist.select(
        'coefficients') \
    .arrayProject([0]) \
    .arrayFlatten([independents])

# Compute fitted values.

def func_ovx(image):
    return image.addBands(
        image.select(independents) \
        .multiply(harmonicTrendCoefficientsDist) \
        .reduce('sum') \
        .rename('fitted'))

fittedHarmonicDist = harmonicLandsatDist.map(func_ovx)








# Merge fitted models.
mergedFitted = fittedHarmonicPre.merge(fittedHarmonicDist)

# Plot the fitted models and the original data at the ROI.
print(ui.Chart.image.series(
        mergedFitted.select(['fitted', 'NDVI']), roi, ee.Reducer \
        .mean(), 30) \
    .setOptions({
        'title': 'Harmonic model: original and fitted values Merged models',
        'lineWidth': 1,
        'pointSize': 3,
    }))

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map