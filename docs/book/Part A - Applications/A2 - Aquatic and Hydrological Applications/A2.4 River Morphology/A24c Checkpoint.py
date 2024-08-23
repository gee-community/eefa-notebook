import ee
import math
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
#  Checkpoint:   A24c
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

# Import existing functions from RivWidthCloud.
# Code repository for RivWidthCloud can be accessed at
# https:#code.earthengine.google.com/?accept_repo=users/eeProject/RivWidthCloudPaper
riverFunctions = require(
    'users/eeProject/RivWidthCloudPaper:functions_river.js')
clFunctions = require(
    'users/eeProject/RivWidthCloudPaper:functions_centerline_width.js'
)

#Calculate distance from shoreline using distance transform.

distance = clFunctions.CalcDistanceMap(rivermask, 256, scale)
Map.addLayer(rpj(distance), {
    'min': 0,
    'max': 500
}, 'distance raster', False)

# Calculate gradient of the distance raster.
# There are three different ways (kernels) to calculate the gradient.
# By default, the function used the second approach.
# For details on the kernels, please see the source code for this function.
gradient = clFunctions.CalcGradientMap(distance, 2, scale)
Map.addLayer(rpj(gradient), {}, 'gradient raster', False)

# Threshold the gradient raster and derive 1px width centerline using skeletonization.

centerlineRaw = clFunctions.CalcOnePixelWidthCenterline(rivermask,
    gradient, 0.9)
raw1pxCenterline = rpj(centerlineRaw).eq(1).selfMask()
Map.addLayer(raw1pxCenterline, {
    'palette': ['red']
}, 'raw 1px centerline', False)

# Prune the centerline to remove spurious branches.
MAXDISTANCE_BRANCH_REMOVAL = 500
# Note: the last argument of the CleanCenterline function enables removal of the pixels
# so that the resulting centerline will have 1px width in an 8-connected way.
# Once it is done, it doesn’t need to be done the second time (thus it equals False)
cl1px = clFunctions \
    .CleanCenterline(centerlineRaw, MAXDISTANCE_BRANCH_REMOVAL, True)
cl1px = clFunctions \
    .CleanCenterline(cl1px, MAXDISTANCE_BRANCH_REMOVAL, False)
final1pxCenterline = rpj(cl1px).eq(1).selfMask()
Map.addLayer(final1pxCenterline, {
    'palette': ['red']
}, 'final 1px centerline', False)

# Calculate perpendicular direction for the cleaned centerline.
angle = clFunctions.CalculateAngle(cl1px)
angleVis = {
    'min': 0,
    'max': 360,
    'palette': ['#ffffd4', '#fed98e', '#fe9929', '#d95f0e',
        '#993404'
    ]
}
Map.addLayer(rpj(angle), angleVis, 'cross-sectional directions',
    False)

# Estimate width.
rwcFunction = require(
    'users/eeProject/RivWidthCloudPaper:rwc_watermask.js')
rwc = rwcFunction.rwGen_waterMask(4000, 333, 500, aoi)
watermask = ee.Image(watermask.rename(['waterMask']).setMulti({
    'crs': crs,
    'scale': 30,
    'image_id': 'aoi'
}))

widths = rwc(watermask)
print('example width output', widths.first())

bankMask = channelmask.focal_max(1).neq(channelmask)

bankDistance = channelmask.Not().cumulativeCost({
    'source': channelmask,
    'maxDistance': 1E2,
    'geodeticDistance': False
})

bankAspect = ee.Terrain.aspect(bankDistance) \
    .multiply(math.pi).divide(180) \
    .mask(bankMask).rename('bankAspect')

distanceKernel = ee.Kernel.euclidean({
    'radius': 30,
    'units': 'meters',
    'magnitude': 0.5
})
bankLength = bankMask.convolve(distanceKernel) \
    .mask(bankMask).rename('bankLength')

radianVis = {
    'min': 0,
    'max': 2 * math.pi,
    'palette': ['red', 'yellow', 'green', 'teal', 'blue', 'magenta',
        'red'
    ]
}
Map.addLayer(rpj(bankAspect), radianVis, 'bank aspect', False)
Map.addLayer(rpj(bankLength), {
    'min': 0,
    'max': 60
}, 'bank length', False)

# ------------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------------
Map
