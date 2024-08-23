import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.7 Humanitarian Applications
#  Checkpoint:   A17a
#  Authors:      Jamon Van Den Hoek, Hannah K. Friedrich
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###########################
#/ Section One: Seeing refugee settlements from above
###########################
Map.setOptions('SATELLITE')

# Load UNHCR settlement boundary for Pagirinya Refugee Settlement.
pagirinya = ee.Feature(ee.FeatureCollection(
    'projects/gee-book/assets/A1-7/pagirinya_settlement_boundary'
).first())

Map.addLayer(pagirinya, {}, 'Pagirinya Refugee Settlement')
Map.centerObject(pagirinya, 14)

# Create buffered settlement boundary geometry.
# 500 meter buffer size is arbitrary but large enough
# to capture area outside of the study settlement.
bufferSize = 500; # (in meters)

# Buffer and convert to Geometry for spatial filtering and clipping.
bufferedBounds = pagirinya.buffer(bufferSize) \
    .bounds().geometry()

def addIndices(img):
    ndvi = img.normalizedDifference(['nir', 'red']) \
        .rename('NDVI');
    ndbi = img.normalizedDifference(['swir1', 'nir']) \
        .rename(['NDBI']);
    nbr = img.normalizedDifference(['nir', 'swir2']) \
        .rename(['NBR']);
    imgIndices = img.addBands(ndvi).addBands(ndbi).addBands(nbr)
    return imgIndices


# Create L8 SR Collection 2 band names and new names.
landsat8BandNames = ['SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6',
    'SR_B7'
]
landsat8BandRename = ['blue', 'green', 'red', 'nir', 'swir1', 'swir2']

# Create image collection.
landsat8Sr = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
ic = ee.ImageCollection(landsat8Sr.filterDate('2015-01-01',
        '2020-12-31') \
    .filterBounds(bufferedBounds) \
    .filter(ee.Filter.lt('CLOUD_COVER', 40)) \
    .select(landsat8BandNames, landsat8BandRename) \
    .map(addIndices))

# Make annual pre- and post-establishment composites.
preMedian = ic.filterDate('2015-01-01', '2015-12-31').median() \
    .clip(bufferedBounds)
postMedian = ic.filterDate('2017-01-01', '2017-12-31').median() \
    .clip(bufferedBounds)

# Import visualization palettes https:#github.com/gee-community/ee-palettes.
palettes = require('users/gena/packages:palettes')
greenPalette = palettes.colorbrewer.Greens[9]
prGreenPalette = palettes.colorbrewer.PRGn[9]

# Set-up "True color" visualization parameters.
TCImageVisParam = {
    'bands': ['red', 'green', 'blue'],
    'gamma': 1,
    'max': 13600,
    'min': 8400,
    'opacity': 1
}

# Set-up "False color" visualization parameters.
FCImageVisParam = {
    'bands': ['nir', 'red', 'green'],
    'gamma': 1,
    'min': 9000,
    'max': 20000,
    'opacity': 1
}

# Display True-color composites.
Map.addLayer(preMedian, TCImageVisParam,
    'Pre-Establishment Median TC')
Map.addLayer(postMedian, TCImageVisParam,
    'Post-Establishment Median TC')

# Display False-color composites.
Map.addLayer(preMedian, FCImageVisParam,
    'Pre-Establishment Median FC')
Map.addLayer(postMedian, FCImageVisParam,
    'Post-Establishment Median FC')

# Display median NDVI composites.
Map.addLayer(preMedian, {
    'min': 0,
    'max': 0.7,
    'bands': ['NDVI'],
    'palette': greenPalette
}, 'Pre-Establishment Median NDVI')
Map.addLayer(postMedian, {
    'min': 0,
    'max': 0.7,
    'bands': ['NDVI'],
    'palette': greenPalette
}, 'Post-Establishment Median NDVI')

# Create an empty byte Image into which we’ll paint the settlement boundary.
empty = ee.Image().byte()

# Convert settlement boundary’s geometry to an Image for overlay.
pagirinyaOutline = empty.paint({
    'featureCollection': pagirinya,
    'color': 1,
    'width': 2
})

# Display Pagirinya boundary in blue.
Map.addLayer(pagirinyaOutline,
    {
        'palette': '0000FF'
    },
    'Pagirinya Refugee Settlement boundary')

# Compare pre- and post-establishment differences in NDVI.
diffMedian = postMedian.subtract(preMedian)
Map.addLayer(diffMedian,
    {
        'min': -0.1,
        'max': 0.1,
        'bands': ['NDVI'],
        'palette': prGreenPalette
    },
    'Difference Median NDVI')

# Chart the NDVI distributions for pre- and post-establishment.
combinedNDVI = preMedian.select(['NDVI'], ['pre-NDVI']) \
    .addBands(postMedian.select(['NDVI'], ['post-NDVI']))

prePostNDVIFrequencyChart =
    ui.Chart.image.histogram({
        'image': combinedNDVI,
        'region': bufferedBounds,
        'scale': 30
    }).setSeriesNames(['Pre-Establishment', 'Post-Establishment']) \
    .setOptions({
        'title': 'NDVI Frequency Histogram',
        'hAxis': {
            'title': 'NDVI',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            },
        },
        'vAxis':
        {
            'title': 'Count',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'colors': ['cf513e', '1d6b99']
    })
print(prePostNDVIFrequencyChart)

# Import package to support text annotation.
text = require('users/gena/packages:text')
rgbVisParam = {
    'bands': ['red', 'green', 'blue'],
    'gamma': 1,
    'max': 12011,
    'min': 8114,
    'opacity': 1
}

# Define arguments for animation function parameters.
videoArgs = {
    'region': bufferedBounds,
    'framesPerSecond': 3,
    'scale': 10
}

annotations = [{
    'position': 'left',
    'offset': '5%',
    'margin': '5%',
    'property': 'label',
    'scale': 30
}]

def addText(image):
    date = ee.String(ee.Date(image.get('system:time_start')) \
        .format(' YYYY-MM-dd'))
    # Set a property called label for each image.
    image = image.clip(bufferedBounds).visualize(rgbVisParam) \
        .set({
            'label': date
        })
    # Create a new image with the label overlaid using gena's package.
    annotated = text.annotateImage(image, {}, bufferedBounds,
        annotations)
    return annotated


# Add timestamp annotation to all images in video.
tempCol = ic.map(addText)

# Click the URL to watch the time series video.
print('L8 Time Series Video', tempCol.getVideoThumbURL(videoArgs))

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map
