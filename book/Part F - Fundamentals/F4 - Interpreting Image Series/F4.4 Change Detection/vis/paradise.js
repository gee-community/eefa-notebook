/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var imageVisParam = {"opacity":1,"bands":["swir2","nir","red"],"min":7749,"max":22215,"gamma":1},
    point = 
    /* color: #0b4a8b */
    /* shown: false */
    ee.Geometry.Point([-121.55188822809693, 39.794570152006976]);
/***** End of imports. If edited, may not auto-convert in the playground. *****/
var landsat8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
    .select(
      ['SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'], 
      ['blue', 'green', 'red', 'nir', 'swir1', 'swir2']);

var preImage = landsat8
    .filterBounds(point)
    .filterDate('2018-10-01', '2018-10-30')
    .sort('CLOUD_COVER', true)
    .first();
var postImage = landsat8
    .filterBounds(point)
    .filterDate('2018-12-01', '2019-04-30')
    .sort('CLOUD_COVER', true)
    .first();

Map.centerObject(point, 10);
Map.addLayer(preImage, imageVisParam, 'pre');
Map.addLayer(postImage, imageVisParam, 'post');
