import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F5.1 Raster/Vector Conversions
#  Checkpoint:   F51d
#  Authors:      Keiko Nomura, Samuel Bowers
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#-------------#
# Section 2.1 #
#-------------#

# Load required datasets.
gfc = ee.Image('UMD/hansen/global_forest_change_2020_v1_8')
wdpa = ee.FeatureCollection('WCMC/WDPA/current/polygons')

# Get deforestation.
deforestation = gfc.select('lossyear')

# Generate a new property called 'protected' to apply to the output mask.

def func_hmy(feat):
    return feat.set('protected', 1)

wdpa = wdpa.map(func_hmy)




# Rasterize using the new property.
# unmask() sets areas outside protected area polygons to 0.
wdpaMask = wdpa.reduceToImage(['protected'], ee.Reducer.first()) \
    .unmask()

# Center on Colombia.
Map.setCenter(-75, 3, 6)

# Display on map.
Map.addLayer(wdpaMask, {
    'min': 0,
    'max': 1
}, 'Protected areas (mask)')

# Set the deforestation layer to 0 where outside a protected area.
deforestationProtected = deforestation.where(wdpaMask.eq(0), 0)

# Update mask to hide where deforestation layer = 0
deforestationProtected = deforestationProtected \
    .updateMask(deforestationProtected.gt(0))

# Display deforestation in protected areas
Map.addLayer(deforestationProtected, {
    'min': 1,
    'max': 20,
    'palette': ['yellow', 'orange', 'red']
}, 'Deforestation protected')

# Produce an image with unique ID of protected areas.
wdpaId = wdpa.reduceToImage(['WDPAID'], ee.Reducer.first())

Map.addLayer(wdpaId, {
    'min': 1,
    'max': 100000
}, 'Protected area ID')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map