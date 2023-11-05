import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      Chapter A3.10 Conservation II - Assessing Agricultural
#                Intensification Near Protected Areas
#  Checkpoint:   A310a
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
Map