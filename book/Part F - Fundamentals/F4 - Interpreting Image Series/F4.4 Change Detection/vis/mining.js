/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var point = /* color: #d63000 */ee.Geometry.Point([-70.54473946976444, -13.046675490210111]),
    mininPostVis = {"opacity":1,"bands":["swir2","nir","red"],"min":7749,"max":22215,"gamma":1},
    miningPreVis = {"opacity":1,"bands":["swir2","nir","red"],"min":569.5106854708367,"max":3002.543077970024,"gamma":0.649};
/***** End of imports. If edited, may not auto-convert in the playground. *****/
var landsat8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
    .select(
      ['SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
      ['blue', 'green', 'red', 'nir', 'swir1', 'swir2']);
var landsat5 = ee.ImageCollection('LANDSAT/LT05/C01/T2_SR')
    .select(
      ['B1', 'B2', 'B3', 'B4', 'B5', 'B7'], 
      ['blue', 'green', 'red', 'nir', 'swir1', 'swir2']);

var preImage = landsat5
    .filterBounds(point)
    .filterDate('1985-01-01', '2002-12-30')
    .sort('CLOUD_COVER', true)
    .first();
var postImage = landsat8
    .filterBounds(point)
    .filterDate('2020-01-01', '2020-12-30')
    .sort('CLOUD_COVER', true)
    .first();

Map.centerObject(point, 10);
Map.addLayer(preImage, miningPreVis, 'pre');
Map.addLayer(postImage, mininPostVis, 'post');