import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.7 Humanitarian Applications
#  Checkpoint:   A17d
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

###############################/
#/ Section Two: Mapping features within the refugee settlement
###############################/

# Visualize Open Buildings dataset.
footprints = ee.FeatureCollection(
    'GOOGLE/Research/open-buildings/v1/polygons')
footprintsHigh = footprints.filter('confidence > 0.75')
footprintsLow = footprints.filter('confidence <= 0.75')

Map.addLayer(footprintsHigh, {
    'color': 'FFA500'
}, 'Buildings high confidence')
Map.addLayer(footprintsLow, {
    'color': '800080'
}, 'Buildings low confidence')

# Load land cover samples.
lcPts = ee.FeatureCollection(
    'projects/gee-book/assets/A1-7/lcPts')
print('lcPts', lcPts)

# Create a function to set Feature properties based on value.
def setColor(f):
    value = f.get('class')
    mapDisplayColors = ee.List(['#13a1ed', '#7d02bf',
        '#f0940a', '#d60909'
    ])
    # Use the class as an index to lookup the corresponding display color.
    return f.set({
        'style': {
            'color': mapDisplayColors.get(value)
        }
    })


# Apply the function and view the results.
styled = lcPts.map(setColor)
Map.addLayer(styled.style(**{
    'styleProperty': 'style'
}), {}, 'Land cover samples')

# Convert land cover sample FeatureCollection to an Image.
lcBand = lcPts.reduceToImage({
    'properties': ['class'],
    'reducer': ee.Reducer.first()
}).rename('class')

# Add lcBand to the post-establishment composite.
postMedian = postMedian.addBands(lcBand)

# Define bands that will be visualized in chart.
chartBands = ['blue', 'green', 'red', 'nir', 'swir1', 'swir2', 'class']

print(postMedian, 'postMedian')

# Plot median band value for each land cover type.
postBandsChart = ui.Chart.image \
    .byClass({
      'image': postMedian.select(chartBands),
      'classBand': 'class',
      'region': lcPts,
      'reducer': ee.Reducer.median(),
      'scale': 30,
      'classLabels': ['Settlement', 'Road', 'Forest', 'Agriculture'],
      'xLabels': chartBands
    }) \
    .setChartType('ScatterChart') \
    .setOptions({
      'title': 'Band Values',
      'hAxis': {
        'title': 'Band Name',
        'titleTextStyle': '{italic': False, 'bold': True},
      },
      'vAxis': {
        'title': 'Reflectance (x1e4)',
        'titleTextStyle': '{italic': False, 'bold': True}
      },
      'colors': ['#13a1ed', '#7d02bf', '#f0940a','#d60909'],
      'pointSize': 0,
      'lineSize': 5,
      'curveType': 'function'
    })
print(postBandsChart)

# Define spectral indices that will be visualized in the chart.
indexBands = ['NDVI', 'NDBI', 'NBR', 'class']

# Plot median index value for each land cover type.
postIndicesChart = ui.Chart.image \
    .byClass({
        'image': postMedian.select(indexBands),
        'classBand': 'class',
        'region': lcPts,
        'reducer': ee.Reducer.median(),
        'scale': 30,
        'classLabels': ['Settlement', 'Road', 'Forest',
            'Agriculture'
        ],
        'xLabels': indexBands
    }) \
    .setChartType('ScatterChart') \
    .setOptions({
        'title': 'Index Values',
        'hAxis': {
            'title': 'Index Name',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            },
            #viewWindow: {min: wavelengths[0], max: wavelengths[2]}
            'scaleType': 'string'
        },
        'vAxis': {
            'title': 'Value',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'colors': ['#13a1ed', '#7d02bf', '#f0940a', '#d60909'],
        'pointSize': 5
    })
print(postIndicesChart)

# Create an empty image into which to paint the features, cast to byte.
empty = ee.Image().byte()

# Paint all the polygon edges with the same number and width, display.
pagirinyaOutline = empty.paint({
    'featureCollection': pagirinya,
    'color': 1,
    'width': 2
})

# Map outline of Pagirinya in blue.
Map.addLayer(pagirinyaOutline,
    {
        'palette': '0000FF'
    },
    'Pagirinya Refugee Settlement boundary')

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------

##############################
#/ Section Three: Delineating refugee settlement boundaries
##############################

# Create samples to input to a K-means classifier.
numPx = 500
samples = postMedian.select('NDVI').sample({
    'scale': 30, # Landsat resolution
    'numPixels': numPx,
    'geometries': True
})

Map.addLayer(samples, {}, 'K-means samples')

# Set-up the parameters for K-means.
numClusters = 2
maxIter = 5
seedValue = 21

# Seed the classifier using land cover samples.
clusterer = ee.Clusterer.wekaKMeans({
    'nClusters': numClusters,
    'maxIterations': maxIter,
    'seed': seedValue
}).train(samples)

# Apply the K-means classifier.
kmeansResult = postMedian.cluster(clusterer)
Map.addLayer(kmeansResult, {
    'bands': ['cluster'],
    'max': 1,
    'min': 0
}, 'K-means output')

# Define the kernel used for morphological operations.
kernel = ee.Kernel.square({
    'radius': 3
})

# Perform a dilation followed by an erosion.
kMeansCleaned = kmeansResult \
    .focal_max({
        'kernel': kernel,
        'iterations': 1
    }) # Dilation \
    .focal_min({
        'kernel': kernel,
        'iterations': 1
    }); # Erosion
Map.addLayer(kMeansCleaned, {
    'bands': ['cluster'],
    'max': 1,
    'min': 0
}, 'K-means cleaned')

# Convert cleaned K-means settlement and non-settlement coverages to polygons.
kMeansCleanedPolygon = kMeansCleaned.reduceToVectors({
    'scale': 30,
    'eightConnected': True
})

Map.addLayer(kMeansCleanedPolygon, {}, 'K-Means cleaned polygon')

# Map outline of Pagirinya in blue.
Map.addLayer(pagirinyaOutline,
    {
        'palette': '0000FF'
    },
    'Pagirinya Refugee Settlement boundary')

# Intersect K-means polygons with UNHCR settlement boundary and
# return intersection area as a feature property.

def func_mbh(feat):
    boundaryIsect = pagirinya.intersection(feat, ee \
        .ErrorMargin(1))
    return ee.Feature(feat).set({
        'isectArea': boundaryIsect.area()
    })

kMeansIntersect = kMeansCleanedPolygon.map(func_mbh)








# Sort to select the polygon with largest overlap with the UNHCR settlement boundary.
kMeansBoundary = ee.Feature(kMeansIntersect.sort('isectArea',
    False).first())
Map.addLayer(kMeansBoundary, {}, 'K-Means Settlement Boundary')

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------

##################################/
#/ Section Four: Estimating refugee population within the settlement
##################################/

Map.centerObject(pagirinya, 14)

ghslPop = ee.ImageCollection('JRC/GHSL/P2016/POP_GPW_GLOBE_V1') \
    .filter(ee.Filter.date('2015-01-01', '2016-01-01')).first() \
    .select(['population_count'], ['population'])
hrslPop = ee.Image('projects/gee-book/assets/A1-7/HRSL') \
    .select(['b1'], ['population'])
worldPop = ee.ImageCollection(
        'WorldPop/GP/100m/pop_age_sex_cons_unadj') \
    .filterMetadata('country', 'equals', 'UGA') \
    .first() \
    .select(['population'])

# Set-up visualization to be shared by all population datasets.
visualization = {
    'bands': ['population'],
    'min': 0.0,
    'max': 50.0,
    'palette': ['24126c', '1fff4f', 'd4ff50']
}

# Map population datasets.
Map.addLayer(ghslPop, visualization, 'GHSL Pop')
Map.addLayer(hrslPop, visualization, 'HRSL Pop')
Map.addLayer(worldPop, visualization, 'WorldPop')

# Collect spatial resolution of each dataset.
ghslPopProjection = ghslPop.projection()
ghslPopScale = ghslPopProjection.nominalScale()
print(ghslPopScale, 'GHSL scale')

hrslPopProjection = hrslPop.projection()
hrslPopScale = hrslPopProjection.nominalScale()
print(hrslPopScale, 'HRSL scale')

worldPopProjection = worldPop.projection()
worldPopScale = worldPopProjection.nominalScale()
print(worldPopScale, 'WorldPop scale')

# Summarize population totals for each population product at each settlement and
# assign as new properties to the UNHCR boundary Feature.
pagirinya = pagirinya.set(ghslPop.select(['population'], ['GHSL']) \
    .reduceRegion({
        'reducer': 'sum',
        'scale': ghslPopScale,
        'geometry': pagirinya.geometry(),
        'maxPixels': 1e9,
    }))

pagirinya = pagirinya.set(hrslPop.select(['population'], ['HRSL']) \
    .reduceRegion({
        'reducer': 'sum',
        'scale': hrslPopScale,
        'geometry': pagirinya.geometry(),
        'maxPixels': 1e9,
    }))

pagirinya = pagirinya.set(worldPop.select(['population'], [
    'WorldPop']) \
    .reduceRegion({
        'reducer': 'sum',
        'scale': worldPopScale,
        'geometry': pagirinya.geometry(),
        'maxPixels': 1e9,
    }))

print(pagirinya, 'Pagirinya with population estimates')

# Measure difference between settlement product and UNHCR-recorded population values.
unhcrPopulation = ee.Number(pagirinya.get('UNHCR_Pop'))
ghslDiff = ee.Number(pagirinya.get('GHSL')).subtract(
    unhcrPopulation)
hrslDiff = ee.Number(pagirinya.get('HRSL')).subtract(
    unhcrPopulation)
worldPopDiff = ee.Number(pagirinya.get('WorldPop')).subtract(
    unhcrPopulation)

# Update UNHCR boundary Feature with population difference properties.
pagirinya = pagirinya.set(ee.Dictionary.fromLists(['GHSL_diff',
        'HRSL_diff', 'WorldPop_diff'
    ],
    [ghslDiff, hrslDiff, worldPopDiff]))

print('Pagirinya Population Estimations', pagirinya)

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map