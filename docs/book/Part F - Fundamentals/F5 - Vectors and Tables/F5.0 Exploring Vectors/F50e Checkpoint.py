import ee
import geemap

Map = geemap.Map()

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
usf_building =

    # shown: False #
    ee.Geometry.Polygon(
        [[[-122.45136729605188, 37.77692986089728],
          [-122.45126000769129, 37.77633201208984],
          [-122.45136193163385, 37.77631505176946],
          [-122.45131901628962, 37.776132728079645],
          [-122.45086840517511, 37.776187849242575],
          [-122.4509005916833, 37.77637017279647],
          [-122.45101860887995, 37.77635321248484],
          [-122.45112053282251, 37.776789939269314],
          [-122.4506484640359, 37.776849299992314],
          [-122.45067528612604, 37.777014661755025]]]),
    usf_campus =

    # shown: False #
    ee.Geometry.MultiPolygon(
        [[[[-122.45387746358996, 37.78025485651328],
           [-122.4534697678197, 37.77791441971873],
           [-122.4489851143468, 37.77849105595329],
           [-122.44962884451037, 37.78076363731525]]],
         [[[-122.45295922018377, 37.775902746563965],
           [-122.45270172811834, 37.77512256326928],
           [-122.44941870428411, 37.77552113619849],
           [-122.44960109449713, 37.77630979544932],
           [-122.44678009874097, 37.776725234224465],
           [-122.44701613313428, 37.777590200803616],
           [-122.45311011201612, 37.776860915925724]]],
         [[[-122.45492520933641, 37.77589822903132],
           [-122.45316568022264, 37.7761356745013],
           [-122.45350900297655, 37.77776385146553],
           [-122.45511832838548, 37.77756033130608]]]]),
    usf_point =

    # shown: False #
    ee.Geometry.Point([-122.45124246920876, 37.77652242316423])
#**** End of imports. If edited, may not auto-convert in the playground. ****#
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F5.0 Exploring Vectors
#  Checkpoint:   F50e
#  Authors:      AJ Purdy, Ellen Brock, David Saah
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import the Census Tiger Boundaries from GEE.
tiger = ee.FeatureCollection('TIGER/2010/Blocks')

# Add the new feature collection to the map, but do not display.
Map.addLayer(tiger, {
    'color': 'black'
}, 'Tiger', False)

# Assign the feature collection to the variable sfNeighborhoods.
sfNeighborhoods = ee.FeatureCollection(
    'path/to/your/asset/assetname')

# Note: if you are unable to load the feature collection, you
# can access the data by uncommenting out the following two lines:
# tablePath = 'projects/gee-book/assets/F5-0/SFneighborhoods'
# sfNeighborhoods = ee.FeatureCollection(tablePath)



# Print the size of the feature collection.
# (Answers the question: how many features?)
print(sfNeighborhoods.size())
Map.addLayer(sfNeighborhoods, {
    'color': 'blue'
}, 'sfNeighborhoods')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Filter sfNeighborhoods by USF.
usfNeighborhood = sfNeighborhoods.filterBounds(usf_point)

# Filter the Census blocks by the boundary of the neighborhood layer.
usfTiger = tiger.filterBounds(usfNeighborhood)
Map.addLayer(usfTiger, {}, 'usf_Tiger')

print(usfTiger)

# Filter for census blocks by housing units
housing10_l250 = usfTiger \
    .filter(ee.Filter.lt('housing10', 250))

housing10_g50_l250 = housing10_l250.filter(ee.Filter.gt(
    'housing10', 50))

Map.addLayer(housing10_g50_l250, {
    'color': 'Magenta'
}, 'housing')

housing_area = housing10_g50_l250.geometry().area()
print('housing_area:', housing_area)

housing10_mean = usfTiger.reduceColumns({
  'reducer': ee.Reducer.mean(),
  'selectors': ['housing10']
})

print('housing10_mean', housing10_mean)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Import the Landsat 8 TOA image collection.
landsat8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')

# Get the least cloudy image in 2015.
image = ee.Image(landsat8 \
    .filterBounds(usf_point) \
    .filterDate('2015-01-01', '2015-12-31') \
    .sort('CLOUD_COVER') \
    .first())

nir = image.select('B5')
red = image.select('B4')
ndvi = nir.subtract(red).divide(nir.add(red)).rename('NDVI')

ndviParams = {
    'min': -1,
    'max': 1,
    'palette': ['blue', 'white', 'green']
}

ndviUSFblocks = ndvi.clip(housing10_g50_l250)
Map.addLayer(ndviUSFblocks, ndviParams, 'NDVI image')
Map.centerObject(usf_point, 14)

# Reduce image by feature to compute a statistic e.g. mean, max, min etc.
ndviPerBlock = ndviUSFblocks.reduceRegions({
    'collection': housing10_g50_l250,
    'reducer': ee.Reducer.mean(),
    'scale': 30,
})

# Get a table of data out of Google Earth Engine.
Export.table.toDrive({
    'collection': ndviPerBlock,
    'description': 'NDVI_by_block_near_USF'
})

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

ndviPerBlock = ndviPerBlock.select(['blockid10', 'mean'])
print('ndviPerBlock', ndviPerBlock)
ndviPerBlockSorted = ndviPerBlock.sort('mean', False)
ndviPerBlockSortedFirst = ee.Feature(ndviPerBlock.sort('mean',
        False) # Sort by NDVI mean in descending order. \
    .first());
print('ndviPerBlockSortedFirst', ndviPerBlockSortedFirst)

# Now filter by block and show on map!
GreenHousing = usfTiger.filter(ee.Filter.eq('blockid10',
'#####')); #< Put your id here prepend a 0!
Map.addLayer(GreenHousing, {
    'color': 'yellow'
}, 'Green Housing!')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
