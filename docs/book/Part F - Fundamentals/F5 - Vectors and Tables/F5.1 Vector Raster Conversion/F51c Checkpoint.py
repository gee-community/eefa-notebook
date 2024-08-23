import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F5.1 Raster/Vector Conversions
#  Checkpoint:   F51c
#  Authors:      Keiko Nomura, Samuel Bowers
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#-------------#
# Section 1.4 #
#-------------#

# Load required datasets.
gfc = ee.Image('UMD/hansen/global_forest_change_2020_v1_8')
wdpa = ee.FeatureCollection('WCMC/WDPA/current/polygons')

# Display deforestation.
deforestation = gfc.select('lossyear')

Map.addLayer(deforestation, {
    'min': 1,
    'max': 20,
    'palette': ['yellow', 'orange', 'red']
}, 'Deforestation raster')

# Select protected areas in the Colombian Amazon.
amazonianProtectedAreas = [
    'Cordillera de los Picachos', 'La Paya', 'Nukak',
    'Serrania de Chiribiquete',
    'Sierra de la Macarena', 'Tinigua'
]

wdpaSubset = wdpa.filter(ee.Filter.inList('NAME',
    amazonianProtectedAreas))

# Display protected areas as an outline.
protectedAreasOutline = ee.Image().byte().paint({
    'featureCollection': wdpaSubset,
    'color': 1,
    'width': 1
})

Map.addLayer(protectedAreasOutline, {
    'palette': 'white'
}, 'Amazonian protected areas')

# Set up map display.
Map.centerObject(wdpaSubset)
Map.setOptions('SATELLITE')

scale = deforestation.projection().nominalScale()

# Use 'reduceRegions' to sum together pixel areas in each protected area.
wdpaSubset = deforestation.gte(1) \
    .multiply(ee.Image.pixelArea().divide(10000)).reduceRegions({
        'collection': wdpaSubset,
        'reducer': ee.Reducer.sum().setOutputs([
            'deforestation_area']),
        'scale': scale
    })

print(wdpaSubset); # Note the new 'deforestation_area' property.

# Normalize by area.
wdpaSubset = wdpaSubset.map(
    def function(feat):
        return feat.set('deforestation_rate',
            ee.Number(feat.get('deforestation_area')) \
            .divide(feat.area().divide(10000)) \
            .divide(20) \
            .multiply(100));
    )

# Print to identify rates of change per protected area.
# Which has the fastest rate of loss?
print(wdpaSubset.reduceColumns({
    'reducer': ee.Reducer.toList().repeat(2),
    'selectors': ['NAME', 'deforestation_rate']
}))

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
