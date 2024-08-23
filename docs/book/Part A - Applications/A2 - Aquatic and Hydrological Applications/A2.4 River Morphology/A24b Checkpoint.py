import ee
import geemap

Map = geemap.Map()

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
aoi =

    # shown: False #
    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[-67.18414102495456, -11.09095257894929],
          [-67.18414102495456, -11.402427204567534],
          [-66.57886300981784, -11.402427204567534],
          [-66.57886300981784, -11.09095257894929]]], None, False),
    sword = ee.FeatureCollection("projects/gee-book/assets/A2-4/SWORD")
#**** End of imports. If edited, may not auto-convert in the playground. ****#
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A2.4 River Morphology
#  Checkpoint:   A24b
#  Authors:      Xiao Yang, Theodore Langhorst, Tamlin M. Pavelsky
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# THIS SCRIPT IS DESIGNED AS A TUTORIAL TO SHOWCASE USING GOOGLE EARTH ENGINE TO ANALYSE
# RIVER PLANVIEW GEOMETRIES AND MORPHOLOGICAL DYNAMICS. THE ANALYSIS IS BUILT ON EXISTING
# MONTHLY WATER CLASSIFICATIONS DATASETS AVAILABLE IN GOOGLE EARTH ENGINE. BY SHOWING
# PREPROCESSING STEPS LIKE HOW TO IDENTIFY RIVERS FROM OTHER TYPES OF WATER BODIES, AND HOW
# TO USE MULTI TEMPORAL WATER LAYERS TO EXTRACT DYNAMICAL CHANGES IN RIVER MORPHOLOGY, IT PROVIDES
# A GUIDE TO EXTRACT INFORMATIONS ON RIVERS USING GOOGLE EARTH ENGINE.

# ==========================================================

def getUTMProj(lon, lat):
    # given longitude and latitude (in degree decimals) return EPSG string for the
    # corresponding UTM projection
    # see https:#apollomapping.com/blog/gtm-finding-a-utm-zone-number-easily and
    # https:#sis.apache.Org/faq.html
    utmCode = ee.Number(lon).add(180).divide(6).ceil().int()
    output = ee.Algorithms.If(ee.Number(lat).gte(0),
        ee.String('EPSG:326').cat(utmCode.format('%02d')),
        ee.String('EPSG:327').cat(utmCode.format('%02d')))
    return (output)


coords = aoi.centroid(30).coordinates()
lon = coords.get(0)
lat = coords.get(1)
crs = getUTMProj(lon, lat)
scale = ee.Number(30)

def rpj(image):
    return image.reproject({
        'crs': crs,
        'scale': scale
    })


# ------------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------------

# IMPORT AND VISUALIZE SURFACE WATER MASK.
# Surface water occurrence dataset from the JRC (Pekel et al., 2016).
jrcYearly = ee.ImageCollection('JRC/GSW1_3/YearlyHistory')

# Select the seasonal and permanent pixels image representing the year 2000
watermask = jrcYearly.filter(ee.Filter.eq('year', 2000)).first() \
    .gte(2).unmask(0) \
    .clip(aoi)

Map.centerObject(aoi)
Map.addLayer(ee.Image.constant(0), {
    'min': 0,
    'palette': ['black']
}, 'bg', False)
Map.addLayer(watermask, {}, 'watermask', False)

# REMOVE NOISE AND SMALL ISLANDS TO SIMPLIFY THE TOPOLOGY.

# a. Image closure operation to fill small holes.
watermask = watermask.focal_max().focal_min()

# b. Identify small bars and fill them in to create a filled water mask.
MIN_SIZE = 2E3
barPolys = watermask.Not().selfMask() \
    .reduceToVectors({
        'geometry': aoi,
        'scale': 30,
        'eightConnected': True
    }) \
    .filter(ee.Filter.lte('count', MIN_SIZE));
filled = watermask.paint(barPolys, 1)

Map.addLayer(rpj(filled), {
    'min': 0,
    'max': 1
}, 'filled water mask', False)

# IDENTIFYING RIVERS FROM OTHER TYPES OF WATER BODIES.
# Cumulative cost mapping to find pixels connected to a reference centerline.
costmap = filled.Not().cumulativeCost({
    'source': watermask.And(ee.Image().toByte().paint(sword,
        1)),
    'maxDistance': 3E3,
    'geodeticDistance': False
})

rivermask = costmap.eq(0).rename('riverMask')
channelmask = rivermask.And(watermask)

Map.addLayer(sword, {
    'color': 'red'
}, 'sword', False)
Map.addLayer(rpj(costmap), {
    'min': 0,
    'max': 1E3
}, 'costmap', False)
Map.addLayer(rpj(rivermask), {}, 'rivermask', False)
Map.addLayer(rpj(channelmask), {}, 'channelmask', False)

# ------------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------------
Map
