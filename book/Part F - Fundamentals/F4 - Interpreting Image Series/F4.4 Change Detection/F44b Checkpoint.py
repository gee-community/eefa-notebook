import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F4.4 Change Detection
#  Checkpoint:   F44b
#  Author:       Karis Tenneson, John Dilger, Crystal Wespestad, Brian Zutta,
#                Andréa P Nicolau, Karen Dyson
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

landsat8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') \
    .select(
        ['SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
        ['blue', 'green', 'red', 'nir', 'swir1', 'swir2']
    )

point = ee.Geometry.Point([-123.64, 42.96])
Map.centerObject(point, 11)

preImage = landsat8 \
    .filterBounds(point) \
    .filterDate('2013-06-01', '2013-06-30') \
    .sort('CLOUD_COVER', True) \
    .first()

postImage = landsat8 \
    .filterBounds(point) \
    .filterDate('2020-06-01', '2020-06-30') \
    .sort('CLOUD_COVER', True) \
    .first()

visParam = {
    'bands': ['swir2', 'nir', 'red'],
    'min': 7750,
    'max': 22200
}
Map.addLayer(preImage, visParam, 'pre')
Map.addLayer(postImage, visParam, 'post')

# Calculate NBR.
nbrPre = preImage.normalizedDifference(['nir', 'swir2']) \
    .rename('nbr_pre')
nbrPost = postImage.normalizedDifference(['nir', 'swir2']) \
    .rename('nbr_post')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# 2-date change.
diff = nbrPost.subtract(nbrPre).rename('change')

palette = [
    '011959', '0E365E', '1D5561', '3E6C55', '687B3E',
    '9B882E', 'D59448', 'F9A380', 'FDB7BD', 'FACCFA'
]
visParams = {
    'palette': palette,
    'min': -0.2,
    'max': 0.2
}
Map.addLayer(diff, visParams, 'change')

# Classify change
thresholdGain = 0.10
thresholdLoss = -0.10

diffClassified = ee.Image(0)

diffClassified = diffClassified.where(diff.lte(thresholdLoss), 2)
diffClassified = diffClassified.where(diff.gte(thresholdGain), 1)

changeVis = {
    'palette': 'fcffc8,2659eb,fa1373',
    'min': 0,
    'max': 2
}

Map.addLayer(diffClassified.selfMask(),
    changeVis,
    'change classified by threshold')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

Map