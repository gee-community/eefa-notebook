import ee
import geemap

Map = geemap.Map()

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
roi =

    # shown: False #
    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[-108.01888227338851, 39.04480287274028],
          [-108.01888227338851, 38.98931938880467],
          [-107.85031080122054, 38.98931938880467],
          [-107.85031080122054, 39.04480287274028]]], None, False),
    sampleArea =

    # shown: False #
    ee.Geometry.Polygon(
        [[[-107.97587902754866, 39.00939572571298],
          [-107.96866924971663, 38.99685612090398],
          [-107.94566662520491, 39.00512717360476],
          [-107.88558514327131, 39.00325960105985],
          [-107.87597210616194, 39.02033271471843],
          [-107.93639691084944, 39.024066908916005]]]),
presence = ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-107.95965702742659, 39.00752826586067]),
            {
              "Presence": 1,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.93244869917952, 39.013330568999095]),
            {
              "Presence": 1,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.912364318076, 39.013330568999095]),
            {
              "Presence": 1,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.90558369368635, 39.00992927661494]),
            {
              "Presence": 1,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.89511234969221, 39.00979588926677]),
            {
              "Presence": 1,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.89888889998518, 39.00686130396482]),
            {
              "Presence": 1,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.91262181014143, 39.01146321303844]),
            {
              "Presence": 1,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.93116123885237, 39.01919908102596]),
            {
              "Presence": 1,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.96480686873518, 39.012196823046]),
            {
              "Presence": 1,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.95090229720198, 39.0153312528143]),
            {
              "Presence": 1,
              "system:index": "9"
            })]),
absence = ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-107.95794041365706, 39.00439349027048]),
            {
              "presence": 0,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.95588047713362, 39.01413084931735]),
            {
              "presence": 0,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.93905766219221, 39.0132638785638]),
            {
              "presence": 0,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.9175141593846, 39.009862582972296]),
            {
              "presence": 0,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.91511090010725, 39.01266366181606]),
            {
              "presence": 0,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.90352375716292, 39.01599813484129]),
            {
              "presence": 0,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.89622814864241, 39.0170651330031]),
            {
              "presence": 0,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.921548201743, 39.00559405903748]),
            {
              "presence": 0,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.93622524947249, 39.00746156995408]),
            {
              "presence": 0,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-107.92566807478987, 39.00832861183457]),
            {
              "presence": 0,
              "system:index": "9"
            })])
#**** End of imports. If edited, may not auto-convert in the playground. ****#
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A3.7 Creating Presence and Absence Points
#  Checkpoint:   A37b
#  Authors:      Peder Engelstad, Daniel Carver, Nicholas E. Young
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Call in NAIP imagery as an image collection.
naip = ee.ImageCollection('USDA/NAIP/DOQQ') \
    .filterBounds(roi) \
    .filterDate('2015-01-01', '2017-12-31')

Map.centerObject(naip)

print(naip)

# Filter the data based on date.
naip2017 = naip \
    .filterDate('2017-01-01', '2017-12-31')

naip2015 = naip \
    .filterDate('2015-01-01', '2015-12-31')

# Define viewing parameters for multi band images.
visParamsFalse = {
    'bands': ['N', 'R', 'G']
}
visParamsTrue = {
    'bands': ['R', 'G', 'B']
}

# Add both sets of NAIP imagery to the map to compare coverage.
Map.addLayer(naip2015, visParamsTrue, '2015_True', False)
Map.addLayer(naip2017, visParamsTrue, '2017_True', False)

# Add 2015 False color imagery.
Map.addLayer(naip2015, visParamsFalse, '2015_False', False)

# Creating a geometry feature.
exclosure = ee.Geometry.MultiPolygon([
    [
        [-107.91079184, 39.012553345],
        [-107.90828129, 39.012553345],
        [-107.90828129, 39.014070552],
        [-107.91079184, 39.014070552],
        [-107.91079184, 39.012553345]
    ],
    [
        [-107.9512176, 39.00870162],
        [-107.9496834, 39.00870162],
        [-107.9496834, 39.00950196],
        [-107.95121765, 39.00950196],
        [-107.95121765, 39.00870162]
    ]
])

print(exclosure)

Map.addLayer(exclosure, {}, 'exclosures')

# Load in elevation dataset; clip it to general area.
elev = ee.Image('USGS/NED') \
    .clip(roi)

Map.addLayer(elev, {
    'min': 1500,
    'max': 3300
}, 'elevation', False)

# Apply mosaic, clip, then calculate NDVI.
ndvi = naip2015 \
    .mosaic() \
    .clip(roi) \
    .normalizedDifference(['N', 'R']) \
    .rename('ndvi')

Map.addLayer(ndvi, {
    'min': -0.8,
    'max': 0.8
}, 'NDVI', False)

print(ndvi, 'ndvi')

# Add National Land Cover Database (NLCD).
dataset = ee.ImageCollection('USGS/NLCD')

print(dataset, 'NLCD')

# Load the selected NLCD image.
landcover = ee.Image('USGS/NLCD/NLCD2016') \
    .select('landcover') \
    .clip(roi)

Map.addLayer(landcover, {}, 'Landcover', False)

# Generate random points within the sample area.
points = ee.FeatureCollection.randomPoints({
    'region': sampleArea,
    'points': 1000,
    'seed': 1234
})

print(points, 'points')

Map.addLayer(points, {}, 'Points', False)

# Add bands of elevation and NAIP.
ndviElev = ndvi \
    .addBands(elev) \
    .addBands(landcover)

print(ndviElev, 'Multi band image')

# Extract values to points.
samples = ndviElev.sampleRegions({
    'collection': points,
    'scale': 30,
    'geometries': True
})

print(samples, 'samples')

Map.addLayer(samples, {}, 'samples', False)

# Filter metadata for sites in the NLCD deciduous forest layer.
aspenSites = samples.filter(ee.Filter.equals('landcover', 41))

print(aspenSites, 'Sites')

# Set the NDVI range.
ndvi1 = ndvi \
    .reduceRegion({
        'reducer': ee.Reducer.mean(),
        'geometry': exclosure,
        'scale': 1,
        'crs': 'EPSG:4326'
    })

print(ndvi1, 'Mean NDVI')

# Generate a range of acceptable NDVI values.
ndviNumber = ee.Number(ndvi1.get('ndvi'))
ndviBuffer = ndviNumber.multiply(0.1)
ndviRange = [
    ndviNumber.subtract(ndviBuffer),
    ndviNumber.add(ndviBuffer)
]

print(ndviRange, 'NDVI Range')

#
This function is used to determine the mean value of an image within a given area.
'image': an image with a single band of ordinal or interval level data
'geom': geometry feature that overlaps with the image
'pixelSize': a number that defines the cell size of the image
Returns a dictionary with the median values of the band, the key is the band name.
#
def reduceRegionFunction(image, geom, pixelSize):
    dict = image.reduceRegion({
        'reducer': ee.Reducer.mean(),
        'geometry': geom,
        'scale': pixelSize,
        'crs': 'EPSG:4326'
    })
    return (dict)


# Call function on the NDVI dataset to compare.
ndvi_test = reduceRegionFunction(ndvi, exclosure, 1)

print(ndvi_test, 'ndvi_test')

# Call function on elevation dataset.
elev1 = reduceRegionFunction(elev, exclosure, 30)

print(elev1, 'elev1')

#
Generate a range of acceptable values.
'dictionary': a dictionary object
'key': key to the value of interest, must be a string
'proportion': a percentile to define the range of the values around the mean
Returns a list with a min and max value for the given range.
#
def effectiveRange(dictionary, key, proportion):
    number = ee.Number(dictionary.get(key))
    buffer = number.multiply(proportion)
    range = [
        number.subtract(buffer),
        number.add(buffer)
    ]
    return (range)


# Call function on elevation data.
elevRange = effectiveRange(elev1, 'elevation', 0.1)

print(elevRange)

# Apply multiple filters to get at potential locations.
combinedFilter = ee.Filter.And(
    ee.Filter.greaterThan('ndvi', ndviRange[0]),
    ee.Filter.lessThan('ndvi', ndviRange[1]),
    ee.Filter.greaterThan('elevation', elevRange[0]),
    ee.Filter.lessThan('elevation', elevRange[1])
)

aspenSites2 = aspenSites.filter(combinedFilter)

print(aspenSites2, 'aspenSites2')

Map.addLayer(aspenSites2, {}, 'aspenSites2', False)

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------

# Merge presence and absence datasets.
samples = presence.merge(absence)

print(samples, 'Samples')

Export.table.toDrive({
    'collection': samples,
    'description': 'presenceAbsencePointsForForest',
    'fileFormat': 'csv'
})

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map
