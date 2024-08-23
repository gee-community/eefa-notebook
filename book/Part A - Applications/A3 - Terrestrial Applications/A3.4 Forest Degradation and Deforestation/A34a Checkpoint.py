import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A3.4 Forest Degradation and Deforestation
#  Checkpoint:   A34a
#  Author:       Carlos Souza Jr., Karis Tenneson, John Dilger,
#                Crystal Wespestad, Eric Bullock
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# SMA Model - Section 1

# Define the Landsat endmembers (source: Souza et al. 2005)
# They can be applied to Landsat 5, 7, 8, and potentially 9.
endmembers = [
  [0.0119,0.0475,0.0169,0.625,0.2399,0.0675], # GV
  [0.1514,0.1597,0.1421,0.3053,0.7707,0.1975], # NPV
  [0.1799,0.2479,0.3158,0.5437,0.7707,0.6646], # Soil
  [0.4031,0.8714,0.79,0.8989,0.7002,0.6607] # Cloud
]

# Select a Landsat 5 scene on which to apply the SMA model.
image = ee.Image('LANDSAT/LT05/C02/T1_L2/LT05_226068_19840411') \
    .multiply(0.0000275).add(-0.2)

# Center the map on the image object.
Map.centerObject(image, 10)

# Define and select the Landsat bands to apply the SMA model.
# use ['SR_B1', 'SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B7'] for Landsat 5 and 7.
# use ['SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'] for Landsat 8.
bands = ['SR_B1', 'SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B7']
image = image.select(bands)

# Unmixing image using Singular Value Decomposition.
def getSMAFractions(image, endmembers):
    unmixed = ee.Image(image) \
        .select([0, 1, 2, 3, 4,
        5]) # Use the visible, NIR, and SWIR bands only! \
        .unmix(endmembers) \
        .max(0) \
        .rename('GV', 'NPV', 'Soil', 'Cloud')
    return ee.Image(unmixed.copyProperties(image))


# Calculate GVS and NDFI and add them to image fractions.
# Run the SMA model passing the Landsat image and the endmembers.
sma = getSMAFractions(image, endmembers)

Map.addLayer(sma, {
    'bands': ['NPV', 'GV', 'Soil'],
    'min': 0,
    'max': 0.45
}, 'sma')

# Calculate the Shade and GV shade-normalized (GVs) fractions from the SMA bands.
Shade = sma.reduce(ee.Reducer.sum()) \
    .subtract(1.0) \
    .abs() \
    .rename('Shade')

GVs = sma.select('GV') \
    .divide(Shade.subtract(1.0).abs()) \
    .rename('GVs')

# Add the new bands to the SMA image variable.
sma = sma.addBands([Shade, GVs])

# Calculate the NDFI using image expression.
NDFI = sma.expression(
    '(GVs - (NPV + Soil))  / (GVs + NPV + Soil)', {
        'GVs': sma.select('GVs'),
        'NPV': sma.select('NPV'),
        'Soil': sma.select('Soil')
    }).rename('NDFI')

# Add the NDFI band to the SMA image.
sma = sma.addBands(NDFI)

# Define NDFI color table.
palettes = require(
    'projects/gee-edu/book:Part A - Applications/A3 - Terrestrial Applications/A3.4 Forest Degradation and Deforestation/modules/palettes'
)
ndfiColors = palettes.ndfiColors

imageVis = {
    'bands': ['SR_B5', 'SR_B4', 'SR_B3'],
    'min': 0,
    'max': 0.4
}

# Add the Landsat color composite to the map.
Map.addLayer(image, imageVis, 'Landsat 5 RGB-543', True)

# Add the fraction images to the map.
Map.addLayer(sma.select('Soil'), {
    'min': 0,
    'max': 0.2
}, 'Soil')
Map.addLayer(sma.select('GV'), {
    'min': 0,
    'max': 0.6
}, 'GV')
Map.addLayer(sma.select('NPV'), {
    'min': 0,
    'max': 0.2
}, 'NPV')
Map.addLayer(sma.select('Shade'), {
    'min': 0,
    'max': 0.8
}, 'Shade')
Map.addLayer(sma.select('GVs'), {
    'min': 0,
    'max': 0.9
}, 'GVs')
Map.addLayer(sma.select('NDFI'), {
    'palette': ndfiColors
}, 'NDFI')

def getWaterMask(sma):
    waterMask = (sma.select('Shade').gte(0.65)) \
        .And(sma.select('GV').lte(0.15)) \
        .And(sma.select('Soil').lte(0.05))
    return waterMask.rename('Water')


# You can use the variable below to get the cloud mask.
cloud = sma.select('Cloud').gte(0.1)
water = getWaterMask(sma)

cloudWaterMask = cloud.max(water)
Map.addLayer(cloudWaterMask.selfMask(),
    {
        'min': 1,
        'max': 1,
        'palette': 'blue'
    },
    'Cloud and water mask')

# Mask NDFI.
maskedNDFI = sma.select('NDFI').updateMask(cloudWaterMask.Not())
Map.addLayer(maskedNDFI, {
    'palette': ndfiColors
}, 'NDFI')

# ------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------
Map
