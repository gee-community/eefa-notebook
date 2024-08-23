import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A2.4 River Morphology
#  Checkpoint:   A24d
#  Authors:      Xiao Yang, Theodore Langhorst, Tamlin M. Pavelsky
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Include the helper function getUTMProj introduced at the beginning
# of the chapter in Code Checkpoint A24a.
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


# IMPORT AND VISUALIZE SURFACE WATER MASK
# Surface water occurrence dataset from the JRC (Pekel et al., 2016).
jrcYearly = ee.ImageCollection('JRC/GSW1_3/YearlyHistory')
poi = ee.Geometry.LineString([
    [110.77450764660864, 30.954167027937988],
    [110.77158940320044, 30.950633845897112]
])

rwcFunction = require(
    'users/eeProject/RivWidthCloudPaper:rwc_watermask.js')

# Function to identify the nearest river width to a given location.
def GetNearestClGen(poi):
    def temp(widths):

def func_kck(f):
            return f.set('dist2cl', f.distance(poi,
                30))

        widths = widths.map(func_kck)





        return ee.Feature(widths.sort('dist2cl', True) \
            .first())

    return temp

getNearestCl = GetNearestClGen(poi)

# Multitemporal width extraction.
polygon = poi.buffer(2000)
coords = poi.centroid().coordinates()
lon = coords.get(0)
lat = coords.get(1)
crs = getUTMProj(lon, lat)
scale = ee.Number(30)


def func_qhz(i):
    watermask = i.gte(2).unmask(0)

    watermask = ee.Image(watermask.rename(['waterMask']) \
        .setMulti({
            'crs': crs,
            'scale': scale,
            'image_id': i.getNumber('year')
        }))
    rwc = rwcFunction.rwGen_waterMask(2000, 333, 300,
        polygon)
    widths = rwc(watermask) \
        .filter(ee.Filter.eq('endsInWater', 0)) \
        .filter(ee.Filter.eq('endsOverEdge', 0))

    return ee.Algorithms.If(widths.size(), getNearestCl(
        widths), None)

multiwidths = ee.FeatureCollection(jrcYearly.map(func_qhz
, True))
















, True))

widthTs = ui.Chart.feature.byFeature(multiwidths, 'image_id', [
        'width'
    ]) \
    .setOptions({
        'hAxis': {
            'title': 'Year',
            format: '####'
        },
        'vAxis': {
            'title': 'Width (meter)'
        },
        'title': 'River width time series upstream of the Three Gorges Dam'
    })
print(widthTs)

Map.centerObject(polygon)
Map.addLayer(polygon, {}, 'area of width calculation')

# ------------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------------
Map
