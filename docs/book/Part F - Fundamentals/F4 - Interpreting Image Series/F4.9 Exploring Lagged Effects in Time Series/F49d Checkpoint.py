import ee 
import math
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F4.9 Exploring Lagged Effects in Time Series
#  Checkpoint:   F49d
#  Authors:      Andréa Puzzi Nicolau, Karen Dyson, David Saah, Nicholas Clinton
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


# Import region of interest. Area over California.
roi = ee.Geometry.Polygon([
    [-119.44617458417066,35.92639730653253],
    [-119.07675930096754,35.92639730653253],
    [-119.07675930096754,36.201704711823844],
    [-119.44617458417066,36.201704711823844],
    [-119.44617458417066,35.92639730653253]
])

# Import the USGS Landsat 8 Level 2, Collection 2, Tier 1 collection,
# filter, mask clouds, scale, and add variables.
landsat8sr = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') \
    .filterBounds(roi) \
    .filterDate('2013-01-01', '2018-01-01') \
    .map(maskScaleAndAddVariable)

# Set map center.
Map.centerObject(roi, 10)

# List of the independent variable names.
independents = ee.List(['constant', 't'])

# Name of the dependent variable.
dependent = ee.String('NDVI')

# Compute a linear trend.  This will have two bands: 'residuals' and
# a 2x1 band called coefficients (columns are for dependent variables).
trend = landsat8sr.select(independents.add(dependent)) \
    .reduce(ee.Reducer.linearRegression(independents.length(), 1))

# Flatten the coefficients into a 2-band image
coefficients = trend.select('coefficients') \
    .arrayProject([0]) \
    .arrayFlatten([independents])

# Compute a detrended series.

def func_hhj(image):
    return image.select(dependent) \
        .subtract(image.select(independents).multiply(
                coefficients) \
            .reduce('sum')) \
        .rename(dependent) \
        .copyProperties(image, ['system:time_start'])

detrended = landsat8sr.map(func_hhj)









# Function that creates a lagged collection.
def lag(leftCollection, rightCollection, lagDays):
    filter = ee.Filter.And(
        ee.Filter.maxDifference({
            'difference': 1000 * 60 * 60 * 24 * lagDays,
            'leftField': 'system:time_start',
            'rightField': 'system:time_start'
        }),
        ee.Filter.greaterThan({
            'leftField': 'system:time_start',
            'rightField': 'system:time_start'
        }))

    return ee.Join.saveAll({
        'matchesKey': 'images',
        'measureKey': 'delta_t',
        'ordering': 'system:time_start',
        'ascending': False, # Sort reverse chronologically
    }).apply({
        'primary': leftCollection,
        'secondary': rightCollection,
        'condition': filter
    })


# Create a lagged collection of the detrended imagery.
lagged17 = lag(detrended, detrended, 17)

# Function to stack bands.
def merge(image):
    # Function to be passed to iterate.
    def merger(current, previous):
        return ee.Image(previous).addBands(current)
    
    return ee.ImageCollection.fromImages(image.get('images')) \
        .iterate(merger, image)


# Apply merge function to the lagged collection.
merged17 = ee.ImageCollection(lagged17.map(merge))

# Function to compute covariance.
def covariance(mergedCollection, band, lagBand):
        image) {
        return image.toArray()
    }).reduce(ee.Reducer.covariance(), 8)


# Concatenate the suffix to the NDVI band.
lagBand = dependent.cat('_1')

# Compute covariance.
covariance17 = ee.Image(covariance(merged17, dependent, lagBand)) \
    .clip(roi)

# The output of the covariance reducer is an array image,
# in which each pixel stores a 2x2 variance-covariance array.
# The off diagonal elements are covariance, which you can map
# directly using:
Map.addLayer(covariance17.arrayGet([0, 1]),
    {
        'min': 0,
        'max': 0.02
    },
    'covariance (lag = 17 days)')

# Define the correlation function.
def correlation(vcArrayImage):
    covariance = ee.Image(vcArrayImage).arrayGet([0, 1])
    sd0 = ee.Image(vcArrayImage).arrayGet([0, 0]).sqrt()
    sd1 = ee.Image(vcArrayImage).arrayGet([1, 1]).sqrt()
    return covariance.divide(sd0).divide(sd1).rename(
        'correlation')


# Apply the correlation function.
correlation17 = correlation(covariance17).clip(roi)
Map.addLayer(correlation17,
    {
        'min': -1,
        'max': 1
    },
    'correlation (lag = 17 days)')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

########### Cross-covariance and Cross-correlation ##########/

# Precipitation (covariate)
chirps = ee.ImageCollection('UCSB-CHG/CHIRPS/PENTAD')

# Join the t-l (l=1 pentad) precipitation images to the Landsat.
lag1PrecipNDVI = lag(landsat8sr, chirps, 5)

# Add the precipitation images as bands.
merged1PrecipNDVI = ee.ImageCollection(lag1PrecipNDVI.map(merge))

# Compute and display cross-covariance.
cov1PrecipNDVI = covariance(merged1PrecipNDVI, 'NDVI',
    'precipitation').clip(roi)
Map.addLayer(cov1PrecipNDVI.arrayGet([0, 1]), {},
    'NDVI - PRECIP cov (lag = 5)')

# Compute and display cross-correlation.
corr1PrecipNDVI = correlation(cov1PrecipNDVI).clip(roi)
Map.addLayer(corr1PrecipNDVI, {
    'min': -0.5,
    'max': 0.5
}, 'NDVI - PRECIP corr (lag = 5)')

# Join the precipitation images from the previous month.
lag30PrecipNDVI = lag(landsat8sr, chirps, 30)

    image) {
    laggedImages = ee.ImageCollection.fromImages(image \
        .get('images'))
    return ee.Image(image).addBands(laggedImages.sum() \
        .rename('sum'))
}))

# Compute covariance.
cov30PrecipNDVI = covariance(sum30PrecipNDVI, 'NDVI', 'sum').clip(
    roi)
Map.addLayer(cov1PrecipNDVI.arrayGet([0, 1]), {},
    'NDVI - sum cov (lag = 30)')

# Correlation.
corr30PrecipNDVI = correlation(cov30PrecipNDVI).clip(roi)
Map.addLayer(corr30PrecipNDVI, {
    'min': -0.5,
    'max': 0.5
}, 'NDVI - sum corr (lag = 30)')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

########### Auto-regressive models ##########/

lagged34 = ee.ImageCollection(lag(landsat8sr, landsat8sr, 34))


def func_trh(image):
    return image.set('n', ee.List(image.get('images')) \
        .length())

merged34 = lagged34.map(merge).map(func_trh
).filter(ee.Filter.gt('n', 1))


).filter(ee.Filter.gt('n', 1))

arIndependents = ee.List(['constant', 'NDVI_1', 'NDVI_2'])

ar2 = merged34 \
    .select(arIndependents.add(dependent)) \
    .reduce(ee.Reducer.linearRegression(arIndependents.length(), 1))

# Turn the array image into a multi-band image of coefficients.
arCoefficients = ar2.select('coefficients') \
    .arrayProject([0]) \
    .arrayFlatten([arIndependents])

# Compute fitted values.

def func_gnj(image):
    return image.addBands(
        image.expression(
            'beta0 + beta1 * p1 + beta2 * p2', {
                'p1': image.select('NDVI_1'),
                'p2': image.select('NDVI_2'),
                'beta0': arCoefficients.select('constant'),
                'beta1': arCoefficients.select('NDVI_1'),
                'beta2': arCoefficients.select('NDVI_2')
            }).rename('fitted'))

fittedAR = merged34.map(func_gnj)












# Create an Earth Engine point object to print the time series chart.
pt = ee.Geometry.Point([-119.0955, 35.9909])

print(ui.Chart.image.series(
        fittedAR.select(['fitted', 'NDVI']), pt, ee.Reducer \
    .mean(), 30) \
    .setSeriesNames(['NDVI', 'fitted']) \
    .setOptions({
        'title': 'AR(2) model: original and fitted values',
        'lineWidth': 1,
        'pointSize': 3,
    }))

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

########/ Forecasting ############/

# Forecasting
def fill(current, list):
    # Get the date of the last image in the list.
    latestDate = ee.Image(ee.List(list).get(-1)).date()
    # Get the date of the current image being processed.
    currentDate = ee.Image(current).date()
    # If those two dates are more than 16 days apart, there's
    # a temporal gap in the sequence.  To fill in the gap, compute
    # the potential starting and ending dates of the gap.
    start = latestDate.advance(16, 'day').millis()
    end = currentDate.advance(-16, 'day').millis()
    # Determine if the start and end dates are chronological.
    blankImages = ee.Algorithms.If({
        # Watch out for this.  Might need a tolerance here.
        'condition': start.lt(end),
        # Make a sequence of dates to fill in with empty images.
        'TrueCase': ee.List.sequence({
            'start': start,
            'end': end,
            'step': 1000 * 60 * 60 * 24 * 16

def func_qlc(date):
            # Return a dummy image with a masked NDVI band and a date.
            return ee.Image(0).mask(0).rename(
                'NDVI').set({
                'dummy': True,
                'system:time_start': ee \
                    .Date(date).millis()
            })

        }).map(func_qlc
),







),
        # If there's no gap, return an empty list.
        'FalseCase': []
    })
    # Add any dummy images and the current image to the list.
    return ee.List(list).cat(blankImages).add(current)


# The first image is the starting image.
first = landsat8sr.first()

# The first image is duplicated in this list, so slice it off.
filled = ee.List(landsat8sr.iterate(fill, [first])).slice(1)

# Now, map a function over this list to do the prediction.
indices = ee.List.sequence(5, filled.length().subtract(1))

# A function to forecast from the previous two images.
def forecast(current, list):
    ndvi = ee.Image(current).select('NDVI')
    # Get the t-1 and t-2 images.
    size = ee.List(list).size()
    image1 = ee.Image(ee.List(list).get(size.subtract(1)))
    image2 = ee.Image(ee.List(list).get(size.subtract(2)))

    predicted = ee.Image().expression(
            'beta0 + beta1 * p1 + beta2 * p2', {
                'p1': image1.select('NDVI'),
                'p2': image2.select('NDVI'),
                'beta0': arCoefficients.select('constant'),
                'beta1': arCoefficients.select('NDVI_1'),
                'beta2': arCoefficients.select('NDVI_2')
            }).rename('NDVI') \
        .set('system:time_start', current.get(
            'system:time_start'))

    # Replace the entire image if it's a dummy.
    replaced = ee.Algorithms.If({
        'condition': current.get('dummy'),
        'TrueCase': predicted,
        # Otherwise replace only masked pixels.
        'FalseCase': current.addBands({
            'srcImg': ndvi.unmask().where(ndvi \
            .mask().Not(), predicted).rename(
                'NDVI'),
            'overwrite': True
        })
    })
    # Add the predicted image to the list.
    return ee.List(list).add(replaced)


# Start at a point in the sequence with three consecutive real images.
startList = filled.slice(4, 5)

# Iterate over the filled series to replace dummy images with predictions.
modeled = ee.ImageCollection.fromImages(
        ee.ImageCollection(filled).iterate(forecast, startList)) \
    .select('NDVI')

print(ui.Chart.image.series(
        modeled, pt, ee.Reducer.mean(), 30) \
    .setSeriesNames(['NDVI']) \
    .setOptions({
        'title': 'Forecast',
        'lineWidth': 1,
        'pointSize': 3,
    }))

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map