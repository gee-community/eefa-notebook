/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var point =
    /* color: #d63000 */
    /* shown: false */
    ee.Geometry.Point([-122.19174741047361, 46.20040199038881]);
/***** End of imports. If edited, may not auto-convert in the playground. *****/
var landsat2 = ee.ImageCollection('LANDSAT/LM02/C02/T2')
    .select(['B4', 'B5', 'B6', 'B7'],
            ['green', 'red', 'nir1', 'nir2']);

var preImage = landsat2
    .filterBounds(point)
    .filterDate('1979-08-01', '1979-10-30')
    .sort('CLOUD_COVER', true)
    .first();
var postImage = landsat2
    .filterBounds(point)
    .filterDate('1980-04-01', '1981-10-30')
    .sort('CLOUD_COVER', true)
    .first();

var visParam = {
  'opacity': 1,
  'bands': ['nir1', 'red', 'green'],
  'min': 0,
  'max': 128,
  'gamma':1
};

Map.centerObject(point, 10);
Map.addLayer(preImage, visParam, 'pre');
Map.addLayer(postImage, visParam, 'post');

