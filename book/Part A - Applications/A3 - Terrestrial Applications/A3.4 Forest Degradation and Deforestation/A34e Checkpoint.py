import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A3.4 Forest Degradation and Deforestation
#  Checkpoint:   A34e
#  Author:       Carlos Souza Jr., Karis Tenneson, John Dilger,
#                Crystal Wespestad, Eric Bullock
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

api = require('users/bullocke/coded:CODED/api')
utils = require('projects/GLANCE:ccdcUtilities/api')

# ------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------

# We will use the geometry of the image from the previous section as
# the study area.
studyArea = ee.Image(
        'LANDSAT/LT05/C02/T1_L2/LT05_226068_19840411') \
    .geometry()

# Get cloud masked (Fmask) Landsat imagery.
landsat = utils.Inputs.getLandsat() \
    .filterBounds(studyArea) \
    .filterDate('1984-01-01', '2021-01-01')

# Make a forest mask
gfwImage = ee.Image('UMD/hansen/global_forest_change_2019_v1_7')

# Get areas of forest cover above the threshold
treeCover = 40
forestMask = gfwImage.select('treecover2000') \
    .gte(treeCover) \
    .rename('landcover')

samples = ee.FeatureCollection(
    'projects/gee-book/assets/A3-4/sample_with_pred_hansen_2010')

minObservations = 4
chiSquareProbability = 0.97
training = samples
forestValue = 1
startYear = 1990
endYear = 2020
classBands = ['NDFI', 'GV', 'Shade', 'NPV', 'Soil']
prepTraining = False

#---------------- CODED parameters
codedParams = {
    'minObservations': minObservations,
    'chiSquareProbability': chiSquareProbability,
    'training': training,
    'studyArea': studyArea,
    forestValue: forestValue,
    forestMask: forestMask,
    'classBands': classBands,
    'collection': landsat,
    'startYear': startYear,
    'endYear': endYear,
    'prepTraining': prepTraining
}

# -------------- Run CODED
results = api.ChangeDetection.coded(codedParams)
print(results)

# ------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------

# Format the results for exporting.
degradation = results.Layers.DatesOfDegradation \
    .rename(['degradation_1', 'degradation_2',
        'degradation_3', 'degradation_4'
    ])
deforestation = results.Layers.DatesOfDeforestation \
    .rename(['deforestation_1', 'deforestation_2',
        'deforestation_3', 'deforestation_4'
    ])
mask = results.Layers.mask.rename('mask')
change = ee.Image.cat([degradation, deforestation]).selfMask() \
    .toInt32()
mag = results.Layers.magnitude.reduce(ee.Reducer.min()) \
    .rename('magnitude')

def makeStrata(img, magThreshold):
    strata = img.select('mask').remap([0, 1], [2, 1])
    mag = img.select('magnitude').lte(magThreshold)

    deg = img.select(['deg.*']).gt(0).reduce(ee.Reducer.max()) \
        .multiply(mag)
    def = img.select(['def.*']).gt(0).reduce(ee.Reducer.max()) \
        .multiply(mag)
    strata = strata.where(deg, 3).where(def, 4)

    return strata.clip(studyArea)


fullOutput = ee.Image.cat([mask, change, mag])
magnitudeThresh = -0.6
strata = makeStrata(ee.Image(fullOutput), magnitudeThresh) \
    .rename('strata')

Export.image.toAsset({
    'image': strata,
    'description': 'strata',
    'region': studyArea,
    'scale': 30,
    'maxPixels': 1e13,
})

exportedStrata = ee.Image('projects/gee-book/assets/A3-4/strata')
Map.addLayer(exportedStrata,
    {
        'min': 1,
        'max': 4,
        'palette': 'green,black,yellow,red'
    },
    'strata')
Map.setCenter(-55.0828, -11.24, 11)

# ------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------
Map
