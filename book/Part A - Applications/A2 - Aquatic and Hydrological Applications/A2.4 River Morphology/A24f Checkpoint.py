import ee
import math
import geemap

Map = geemap.Map()

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
jrcYearly = ee.ImageCollection("JRC/GSW1_3/YearlyHistory"),
    aoi =

    # shown: False #
    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[-66.75498758257174, -11.090110301403685],
          [-66.75498758257174, -11.258517279582335],
          [-66.56650339067721, -11.258517279582335],
          [-66.56650339067721, -11.090110301403685]]], None, False),
    sword = ee.FeatureCollection("projects/gee-book/assets/A2-4/SWORD")
#**** End of imports. If edited, may not auto-convert in the playground. ****#
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A2.4 River Morphology
#  Checkpoint:   A24f
#  Authors:      Xiao Yang, Theodore Langhorst, Tamlin M. Pavelsky
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def getUTMProj(lon, lat):
    # Given longitude and latitude in decimal degrees,
    # return EPSG string for the corresponding UTM projection. See:
    # https:#apollomapping.com/blog/gtm-finding-a-utm-zone-number-easily
    # https:#sis.apache.Org/faq.html
    utmCode = ee.Number(lon).add(180).divide(6).ceil().int()
    output = ee.Algorithms.If({
        'condition': ee.Number(lat).gte(0),
        'TrueCase': ee.String('EPSG:326').cat(utmCode \
            .format('%02d')),
        'FalseCase': ee.String('EPSG:327').cat(utmCode \
            .format('%02d'))
    })
    return (output)


coords = aoi.centroid(30).coordinates()
lon = coords.get(0)
lat = coords.get(1)
crs = getUTMProj(lon, lat)
scale = 30

def rpj(image):
    return image.reproject({
        'crs': crs,
        'scale': scale
    })


distanceKernel = ee.Kernel.euclidean({
    'radius': 30,
    'units': 'meters',
    'magnitude': 0.5
})

def makeChannelmask(year):
    watermask = jrcYearly.filter(ee.Filter.eq('year', year)) \
        .first() \
        .gte(2).unmask() \
        .focal_max().focal_min() \
        .rename('watermask')

    barPolys = watermask.Not().selfMask() \
        .reduceToVectors({
            'geometry': aoi,
            'scale': 30,
            'eightConnected': False
        }) \
        .filter(ee.Filter.lte('count', 1E4));

    filled = watermask.paint(barPolys, 1).rename('filled')

    costmap = filled.Not().cumulativeCost({
        'source': watermask.And(ee.Image().toByte().paint(
            sword, 1)),
        'maxDistance': 5E3,
        'geodeticDistance': False
    }).rename('costmap')

    rivermask = costmap.eq(0).rename('rivermask')
    channelmask = rivermask.And(watermask).rename(
        'channelmask')

    bankMask = channelmask.focal_max(1).neq(channelmask) \
        .rename('bankMask')
    bankDistance = channelmask.Not().cumulativeCost({
        'source': channelmask,
        'maxDistance': 1E2,
        'geodeticDistance': False
    })
    bankAspect = ee.Terrain.aspect(bankDistance).mask(
        bankMask).rename('bankAspect')

    bankLength = bankMask.convolve(distanceKernel) \
        .mask(bankMask).rename('bankLength')

    return ee.Image.cat([
            watermask, channelmask, rivermask, bankMask,
            bankAspect, bankLength
        ]).set('year', year) \
        .clip(aoi)


#
  Isolate the river channel from the JRC data for two years and apply the bank morphology
  calculations from Section 1. Here we will simply compare two years with two explicit
  calls to the makeChannelmask() function, but you can also map this function over a list
  'of years like follows':

  masks = ee.List.sequence(2000,2020,5).map(makeChannelmask)
#

masks1 = makeChannelmask(2015)
masks2 = makeChannelmask(2020)
Map.centerObject(aoi, 13)
year1mask = rpj(masks1.select('channelmask').selfMask())
Map.addLayer(year1mask, {
    'palette': ['blue']
}, 'year 1')
year2mask = rpj(masks2.select('channelmask').selfMask())
Map.addLayer(year2mask, {
    'palette': ['red']
}, 'year 2', True, 0.5)

# Pixels that are now the river channel but were previously land.
erosion = masks2.select('channelmask') \
    .And(masks1.select('watermask').Not()).rename('erosion')
Map.addLayer(rpj(erosion).selfMask(), {}, 'erosion', False)

# Erosion distance assuming the shortest distance between banks.
erosionEndpoints = erosion.focal_max(1).And(masks2.select(
    'bankMask'))
erosionDistance = erosion.focal_max(1).selfMask() \
    .cumulativeCost({
        'source': erosionEndpoints,
        'maxDistance': 1E3,
        'geodeticDistance': True
    }).rename('erosionDistance')
Map.addLayer(rpj(erosionDistance),
    {
        'min': 0,
        'max': 300
    },
    'erosion distance',
    False)

# Direction of the erosion following slope of distance.
erosionDirection = ee.Terrain.aspect(erosionDistance) \
    .multiply(math.pi).divide(180) \
    .clip(aoi) \
    .rename('erosionDirection')
erosionDistance = erosionDistance.mask(erosion)
Map.addLayer(rpj(erosionDirection),
    {
        'min': 0,
        'max': math.pi
    },
    'erosion direction',
    False)

#
  Map each pixel to the closest river centerline point.
#

# Distance to nearest SWORD centerline point.
distance = sword.distance(2E3).clip(aoi)

# Second derivatives of distance.
# Finding the 0s identifies boundaries between centerline points.
concavityBounds = distance.convolve(ee.Kernel.laplacian8()) \
    .gte(0).rename('bounds')

Map.addLayer(rpj(distance), {
    'min': 0,
    'max': 1E3
}, 'distance', False)
Map.addLayer(rpj(concavityBounds), {}, 'bounds', False)

# Reduce the pixels according to the concavity boundaries,
# and set the value to SWORD node ID.  Note that focalMode is used
# to fill in the empty pixels that were the boundaries.
swordImg = ee.Image(0).paint(sword, 'node_id').rename('node_id') \
    .clip(aoi)
nodePixels = concavityBounds.addBands(swordImg) \
    .reduceConnectedComponents({
        'reducer': ee.Reducer.max(),
        'labelBand': 'bounds'
    }).focalMode({
        'radius': 3,
        'iterations': 2
    })
Map.addLayer(rpj(nodePixels).randomVisualizer(),
    {},
    'node assignments',
    False)

# Set up a custom reducing function to summarize the data.
def groupReduce(dataImg, nodeIds, reducer):
    # Create a grouped reducer for each band in the data image.
    groupReducer = reducer.forEach(dataImg.bandNames()) \
        .group({
            'groupField': dataImg.bandNames().length(),
            'groupName': 'node_id'
        })

    # Apply the grouped reducer.
    statsList = dataImg.addBands(nodeIds).clip(aoi) \
        .reduceRegion({
            'reducer': groupReducer,
            'scale': 30,
        }).get('groups')

    # Convert list of dictionaries to FeatureCollection.

def func_hhz(dict):
        return ee.Feature(None, dict)

    statsOut = ee.List(statsList).map(func_hhz)



    return ee.FeatureCollection(statsOut)


dataMask = masks1.addBands(masks2).reduce(ee.Reducer \
    .anyNonZero())

sumBands = ['watermask', 'channelmask', 'bankLength']
sumImg = erosion \
    .addBands(masks1, sumBands) \
    .addBands(masks2, sumBands)
sumStats = groupReduce(sumImg, nodePixels, ee.Reducer.sum())

angleImg = erosionDirection \
    .addBands(masks1, ['bankAspect']) \
    .addBands(masks2, ['bankAspect'])
angleStats = groupReduce(angleImg, nodePixels, ee.Reducer \
    .circularMean())


def func_kqd(feat):
    nodeFilter = ee.Filter.eq('node_id', feat.get(
        'node_id'))
    sumFeat = sumStats.filter(nodeFilter).first()
    angleFeat = angleStats.filter(nodeFilter).first()
    return feat.copyProperties(sumFeat).copyProperties(
        angleFeat)

vectorData = sword.filterBounds(aoi).map(func_kqd)









print(vectorData)
Map.addLayer(vectorData, {}, 'final data')

# ------------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------------
Map
