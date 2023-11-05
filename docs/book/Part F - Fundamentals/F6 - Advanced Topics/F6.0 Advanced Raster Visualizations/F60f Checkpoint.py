import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F6.0 Advanced Raster Visualization
#  Checkpoint:   F60f
#  Authors:      Gennadii Donchyts, Fedor Baart
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

text = require('users/gena/packages:text')

geometry = ee.Geometry.Polygon(
    [
        [
            [-109.248, 43.3913],
            [-109.248, 33.2689],
            [-86.5283, 33.2689],
            [-86.5283, 43.3913]
        ]
    ], None, False)

Map.centerObject(geometry, 6)

def annotate(image):
    # Annotates an image by adding outline border and cloudiness
    # Cloudiness is shown as a text string rendered at the image center.

    # Add an edge around the image.
    edge = ee.FeatureCollection([image]) \
        .style(**{
            'color': 'cccc00cc',
            'fillColor': '00000000'
        })

    # Draw cloudiness as text.
    props = {
        'textColor': '0000aa',
        'outlineColor': 'ffffff',
        'outlineWidth': 2,
        'outlineOpacity': 0.6,
        'fontSize': 24,
        'fontType': 'Consolas'
    }
    center = image.geometry().centroid(1)
    str = ee.Number(image.get('CLOUD_COVER')).format('%.2f')
    scale = Map.getScale()
    textCloudiness = text.draw(str, center, scale, props)

    # Shift left 25 pixels.
    textCloudiness = textCloudiness \
        .translate(-scale * 25, 0, 'meters', 'EPSG:3857')

    # Merge results.
    return ee.ImageCollection([edge, textCloudiness]).mosaic()


# Select images.
images = ee.ImageCollection('LANDSAT/LC08/C02/T1_RT_TOA') \
    .select([5, 4, 2]) \
    .filterBounds(geometry) \
    .filterDate('2018-01-01', '2018-01-7')

# dim background.
Map.addLayer(ee.Image(1), {
    'palette': ['black']
}, 'black', True, 0.5)

# Show images.
Map.addLayer(images, {
    'min': 0.05,
    'max': 1,
    'gamma': 1.4
}, 'images')

# Show annotations.
labels = images.map(annotate)
labelsLayer = ui.Map.Layer(labels, {}, 'annotations')
Map.layers().add(labelsLayer)

# re-render (rescale) annotations when map zoom changes.
Map.onChangeZoom(function(zoom) {
    labelsLayer.setEeObject(images.map(annotate))
})

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map