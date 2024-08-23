import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      Chapter A3.10 Conservation II - Assessing Agricultural
#                Intensification Near Protected Areas
#  Checkpoint:   A310c
#  Authors:      Pradeep Koulgi, MD Madhusudan
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1. Parameters to function calls

# 1.1. Annual dry season max NDVI calculation
modis_veg = ee.ImageCollection('MODIS/006/MOD13Q1')
ndviBandName = 'NDVI'
ndviValuesScaling = 0.0001
modisVegScale = 250; # meters
maxNDVIBandname = 'max_dryseason_ndvi'
yearTimestampBandname = 'year'
years = ee.List.sequence(2000, 2021, 1)
drySeasonStart_doy = 1
drySeasonEnd_doy = 90

# 1.2. Boundaries of Protected Areas of interest
paBoundaries = ee.FeatureCollection(
    'projects/gee-book/assets/A3-10/IndiaMainlandPAs')
boundaryBufferWidth = 5000; # meters
bufferingMaxError = 30; # meters
# Choose PAs in only the western states
western_states = [
    'Rajasthan', 'Gujarat', 'Madhya Pradesh',
    'Maharashtra', 'Goa', 'Karnataka', 'Kerala'
]
western_pas = paBoundaries \
    .filter(ee.Filter.inList('STATE', western_states))

# 1.3. Regression analysis
regressionReducer = ee.Reducer.sensSlope()
regressionX = yearTimestampBandname
regressionY = maxNDVIBandname

# 1.4. Surface water layer to mask water pixels from assessment
# Selects pixels where water has ever been detected between 1984 and 2021
surfaceWaterExtent = ee.Image('JRC/GSW1_3/GlobalSurfaceWater') \
    .select('max_extent')

# 1.5. Average annual precipitation layer
rainfall = ee.Image('WORLDCLIM/V1/BIO').select('bio12')

# 1.6. Visualization parameters
regressionResultVisParams = {
    'min': -3,
    'max': 3,
    'palette': ['ff8202', 'ffffff', '356e02']
}
regressionSummaryChartingOptions = {
    'title': 'Yearly change in dry-season vegetation greenness ' + \
        'in PA buffers in relation to average annual rainfall',
    'hAxis': {
        'title': 'Annual Precipitation'
    },
    'vAxis': {
        'title': 'Median % yearly change in vegetation greenness ' + \
            'in 5 km buffer'
    },
    'series': {
        '0': {
            'visibleInLegend': False
        }
    },
}

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------

# 2. Raster processing for change analysis

# Defining functions to be used in this script

# 2.1. Annual dry season maxima of NDVI

def annualDrySeasonMaximumNDVIAndTime(y):
    # Convert year y to a date object
    yDate = ee.Date.fromYMD(y, 1, 1)
    # Calculate max NDVI for year y
    yMaxNdvi = drySeasonNdviColl \
        .filter(ee.Filter.date(yDate, yDate.advance(1, 'year'))) \
        .max()
        # Apply appropriate scale, as per the dataset's \
        .multiply(ndviValuesScaling) \
        .rename(maxNDVIBandname)
    # Create an image with constant value y, to be used in regression. Name it something comprehensible.
    # Name it something comprehensible.
    yTime = ee.Image.constant(y).int().rename(
        yearTimestampBandname)
    # Combine the two images into a single 2-band image, and return
    return ee.Image.cat([yMaxNdvi, yTime]).set('year', y)


# Create a collection of annual dry season maxima
# for the years of interest.  Select the NDVI band and
# filter to the collection of dry season observations.
drySeasonNdviColl = modis_veg.select([ndviBandName]) \
    .filter(ee.Filter.calendarRange(drySeasonStart_doy,
        drySeasonEnd_doy, 'day_of_year'))
# For each year of interest, calculate the NDVI maxima and create a corresponding time band
dryseason_coll = ee.ImageCollection.fromImages(
    years.map(annualDrySeasonMaximumNDVIAndTime)
)

# 2.2. Annual regression to estimate average yearly change in greenness

ss = dryseason_coll.select([regressionX, regressionY]).reduce(
    regressionReducer)

# Mask surface water from vegetation change image
ss = ss.updateMask(surfaceWaterExtent.eq(0))

# 2.3. Summarise estimates of change in buffer regions of PAs of interest
def extractBufferRegion(pa):
    #reduce vertices in PA boundary
    pa = pa.simplify({
        'maxError': 100
    })
    # Extend boundary into its buffer
    withBuffer = pa.buffer(boundaryBufferWidth,
        bufferingMaxError)
    # Compute the buffer-only region by "subtracting" boundary with buffer from boundary
    # Subtracting the whole set of boundaries eliminates inclusion of forests from adjacent PAs into buffers.
    bufferOnly = withBuffer.difference(paBoundaries.geometry())

    return bufferOnly


# Create buffer regions of PAs
pa_buff = western_pas.map(extractBufferRegion)

# Normalize the metric of NDVI change to a baseline (dry-season max NDVI in the very first year)
baselineNdvi = dryseason_coll.select([maxNDVIBandname]).filter(ee \
    .Filter.eq('year', years.getNumber(0))).first()
stats = ss.select('slope').divide(baselineNdvi).multiply(100) \
    .rename('vegchange')

# Combine it with average annual rainfall data
stats = stats.addBands(rainfall.rename('rainfall'))

# Calculate mean of change metric over buffer regions of each PA of interest
paBufferwiseMedianChange = stats.reduceRegions({
    'collection': pa_buff,
    'reducer': ee.Reducer.median(),
    'scale': 1000,
    'tileScale': 16
})

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------

# 3. Visualize results
medianChangeChart = ui.Chart.feature.byFeature({
    'features': paBufferwiseMedianChange,
    'xProperty': 'rainfall',
    'yProperties': ['vegchange']
}).setOptions(regressionSummaryChartingOptions).setChartType(
    'ScatterChart')
print(medianChangeChart)

Map.centerObject(western_pas, 9)
Map.setCenter(79.2205, 23.3991, 9)
Map.setOptions('SATELLITE')
Map.addLayer(stats.select('vegchange').clipToCollection(pa_buff),
    regressionResultVisParams, 'yearly % change')
Map.addLayer(western_pas, {}, 'Western PAs')

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map
