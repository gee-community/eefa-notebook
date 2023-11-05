import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F5.1 Raster/Vector Conversions
#  Checkpoint:   F51e
#  Authors:      Keiko Nomura, Samuel Bowers
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#-------------#
# Section 2.2 #
#-------------#

# Load required datasets.
gfc = ee.Image('UMD/hansen/global_forest_change_2020_v1_8')
wdpa = ee.FeatureCollection('WCMC/WDPA/current/polygons')

# Select a single protected area.
protectedArea = wdpa.filter(ee.Filter.equals('NAME', 'La Paya'))

# Maximum distance in meters is set in the brackets.
distance = protectedArea.distance(1000000)

Map.addLayer(distance, {
    'min': 0,
    'max': 20000,
    'palette': ['white', 'grey', 'black'],
    'opacity': 0.6
}, 'Distance')

Map.centerObject(protectedArea)

# Produce a raster of inside/outside the protected area.

def func_azl(feat):
    return feat.set('protected', 1)

protectedAreaRaster = protectedArea.map(func_azl
).reduceToImage(['protected'], ee.Reducer.first())

).reduceToImage(['protected'], ee.Reducer.first())

Map.addLayer(distance.updateMask(protectedAreaRaster), {
    'min': 0,
    'max': 20000
}, 'Distance inside protected area')

Map.addLayer(distance.updateMask(protectedAreaRaster.unmask() \
.Not()), {
    'min': 0,
    'max': 20000
}, 'Distance outside protected area')

distanceZones = ee.Image(0) \
    .where(distance.gt(0), 1) \
    .where(distance.gt(1000), 2) \
    .where(distance.gt(3000), 3) \
    .updateMask(distance.lte(5000))

Map.addLayer(distanceZones, {}, 'Distance zones')

deforestation = gfc.select('loss')
deforestation1km = deforestation.updateMask(distanceZones.eq(1))
deforestation3km = deforestation.updateMask(distanceZones.lte(2))
deforestation5km = deforestation.updateMask(distanceZones.lte(3))

Map.addLayer(deforestation1km, {
    'min': 0,
    'max': 1
}, 'Deforestation within a 1km buffer')
Map.addLayer(deforestation3km, {
    'min': 0,
    'max': 1,
    'opacity': 0.5
}, 'Deforestation within a 3km buffer')
Map.addLayer(deforestation5km, {
    'min': 0,
    'max': 1,
    'opacity': 0.5
}, 'Deforestation within a 5km buffer')

deforestation1kmOutside = deforestation1km \
    .updateMask(protectedAreaRaster.unmask().Not())

# Get the value of each pixel in square meters
# and divide by 10000 to convert to hectares.
deforestation1kmOutsideArea = deforestation1kmOutside.eq(1) \
    .multiply(ee.Image.pixelArea()).divide(10000)

# We need to set a larger geometry than the protected area
# for the geometry parameter in reduceRegion().
deforestationEstimate = deforestation1kmOutsideArea \
    .reduceRegion({
        'reducer': ee.Reducer.sum(),
        'geometry': protectedArea.geometry().buffer(1000),
        'scale': deforestation.projection().nominalScale()
    })

print('Deforestation within a 1km buffer outside the protected area (ha)',
    deforestationEstimate)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map