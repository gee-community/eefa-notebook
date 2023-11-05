import ee 
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
#  Checkpoint:   A24e
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


# ------------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------------
Map