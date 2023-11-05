/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var testArea = 
    /* color: #d63000 */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[-66.73156878460787, -8.662236005089952],
          [-66.73156878460787, -8.916025640576244],
          [-66.44867083538912, -8.916025640576244],
          [-66.44867083538912, -8.662236005089952]]], null, false);
/***** End of imports. If edited, may not auto-convert in the playground. *****/
// Fusion Near Real-time (GUI)
// Near real-time monitoring of forest disturbance by fusion of 
// multi-sensor data.  @author Xiaojing Tang (xjtang@bu.edu).

// ---------------------------------------------------------------
// Model Parameters:
var trainPeriod = ee.Dictionary({'start': '2017-01-01', 'end': '2020-01-01'});
var monitorPeriod = ee.Dictionary({'start': '2020-01-01', 'end': '2021-01-01'});
var fullPeriod = ee.Dictionary({
     'start': trainPeriod.get('start'),
     'end': monitorPeriod.get('end')});
var nrtParam = {z: 2, n: 4, m: 5, maxZ: 10};
var optParam = {
  band: 'NDFI', 
  minRMSE: 0.05,
  strikeOnly: false,
  vis: {bands: ['SWIR1', 'NIR', 'Red'], min: 0, max: 5000}
};
var radParam = {
  band: 'VV', 
  minRMSE: 0.01,
  strikeOnly: true,
  vis: {bands: ['VV', 'VH', 'ratio'], min: 10, max: 30}
};
var mskVisParam = {min: 0, max: 1, palette: ['blue', 'green']};
var altVisParam = {min: 2020.4, max: 2021,
                    palette: ['FF0080', 'EC1280', 'DA2480', 'C83680', 'B64880', 'A35B80', '916D80', 
                              '7F7F80', '6D9180', '5BA380', '48B680', '36C880', '24DA80', '12EC80',
                              '00FF80', '00EB89', '00D793', '00C49D', '00B0A7', '009CB0', '0089BA', 
                              '0075C4', '0062CE', '004ED7', '003AE1', '0027EB', '0013F5', '0000FF']};

// ---------------------------------------------------------------
// Imports and predefined variables:
var listener = 0;
var ut = require('users/xjtang/fnrt:Lite/Utilities');
var hansen = ee.Image('UMD/hansen/global_forest_change_2020_v1_8').unmask();
var forestMask = hansen.select('treecover2000').gt(50)
                  .add(hansen.select('gain'))
                  .subtract(hansen.select('loss'))
                  .add(hansen.select('lossyear').eq(20))
                  .gt(0);
var alerts = null;
var ccd = ee.ImageCollection('projects/gee-book/assets/A3-5/ccd');

// ---------------------------------------------------------------
// Main functions:
  // run and plot CCD result for a pixel
var chartCCD = function(coords) {
  resetTSPanel();
  var sensor = ccdSelect.getValue();
  var pixel = ee.Geometry.Point([coords.lon, coords.lat]);
  tsPanel.add(ui.Label('Running CCD on ' + sensor + ' data...'));
  addPixel(coords);
  var param = null;
  if (sensor == 'Sentinel-1') {
    param = radParam;
  } else {
    param = optParam;
  }
  var trainData = ut.getData(pixel, trainPeriod, sensor);
  var monitorData = ut.getData(pixel, monitorPeriod, sensor);
  var ccdModel = ee.Image(ee.Algorithms.If(
                  ccd.filterMetadata('sensor', 'equals', sensor).first(),
                  ccd.filterMetadata('sensor', 'equals', sensor).first(),
                  ut.runCCD(trainData, trainPeriod, param.band)
                ));
  var ccdTS = ut.getTimeSeries(trainData, monitorData, ccdModel, pixel, param.band, 0.1);
  var ccdTable = ut.transformToTable(ccdTS, ['dateString', 'train', 'monitor', 'fit']);
  ccdTable.evaluate(function(t, e) {
    var chart = ut.createCCDChart(t, param.band, coords.lat, coords.lon);
    chart.onClick(
      function(date) {
        if (date === null) {
          removeLayer('_');
        } else {
          var img = ee.Image(ut.getImage(pixel, date, sensor));
          mapPanel.addLayer(img, param.vis, img.get('system:index').getInfo());
          removeLayer('Clicked');
          addPixel(coords);
        }
      }
    );
    tsPanel.clear();
    tsPanel.add(chart);
  });
};

  // run near-real-time monitoring for one sensor for one pixel
var runPixelSensorNRT = function(pixel, sensor) {
  var trainData = ut.getData(pixel, trainPeriod, sensor);
  var monitorData = ut.getData(pixel, monitorPeriod, sensor);
  var param = null;
  if (sensor == 'Sentinel-1') {
    param = radParam;
  } else {
    param = optParam;
  }
  var ccdModel = ee.Image(ee.Algorithms.If(
              ccd.filterMetadata('sensor', 'equals', sensor).first(),
              ccd.filterMetadata('sensor', 'equals', sensor).first(),
              ut.runCCD(trainData, trainPeriod, param.band)
            ));
  var ccdTS = ut.getTimeSeries(trainData, monitorData, ccdModel, pixel, param.band);
  var Z = ee.FeatureCollection(ut.addPixelZScore(ccdTS, nrtParam.maxZ, param.minRMSE));
  var checked = ut.checkPixelZScore(Z, nrtParam.z);
  if ((S2Check.getValue() | LSTCheck.getValue()) & param.strikeOnly) {
    checked = checked.filterMetadata('Ball', 'equals', null);
  }
  return checked;
};

  // run and plot NRT for a pixel
var chartNRT = function(coords) {
  resetTSPanel();
  tsPanel.add(ui.Label('Running NRT...'));
  var pixel = ee.Geometry.Point([coords.lon, coords.lat]);
  addPixel(coords);
  var nrtTS = ee.FeatureCollection([]);
  if (S2Check.getValue()) {nrtTS = nrtTS.merge(runPixelSensorNRT(pixel, 'Sentinel-2'))}
  if (S1Check.getValue()) {nrtTS = nrtTS.merge(runPixelSensorNRT(pixel, 'Sentinel-1'))}
  if (LSTCheck.getValue()) {nrtTS = nrtTS.merge(runPixelSensorNRT(pixel, 'Landsat'))}
  nrtTS = nrtTS.filterMetadata('x', 'not_equals', null);
  if (nrtTS.size().gt(0)) {
    var nrtMonitor = ee.FeatureCollection(ut.monitorPixelChange(nrtTS.sort('fitTime'), nrtParam));
    var nrt = ut.transformToTable(nrtMonitor, ['dateString', 'Z_train', 'Ball', 'Strike', 'StrikeOut']);
    nrt.evaluate(function(t, e) {
      var chart = ut.createNRTChart(t, coords.lat, coords.lon);
      tsPanel.clear();
      tsPanel.add(chart);
    });
  } else {
    tsPanel.add(ui.Label('No sensor was selected.'));
  }
};

  // run near-real-time monitoring for one sensor for an area
var runAreaSensorNRT = function(area, sensor) {
  var param = null;
  if (sensor == 'Sentinel-1') {
    param = radParam;
  } else {
    param = optParam;
  }
  var monitorData = ut.getData(area, monitorPeriod, sensor);
  var ccdModel = ccd.filterMetadata('sensor', 'equals', sensor).first().updateMask(forestMask);
  var ccdImg = ut.getCCDImage(ccdModel, param.band);
  var synthetics = ut.addSynthetic(monitorData, ccdImg, param.band, sensor);
  var monitorRes = ut.getResiduals(synthetics, param.band);
  return ut.getChangeScores(monitorRes, ccdImg.select('.*rmse'), 
                            synthetics.select(param.band).mean(), 
                            param.minRMSE, nrtParam.z, param.strikeOnly);
};

  // run near real time
var runNRT = function(area) {
  var nrtTS = ee.ImageCollection([]);
  if (S2Check.getValue()) {nrtTS = nrtTS.merge(runAreaSensorNRT(area, 'Sentinel-2'))}
  if (S1Check.getValue()) {nrtTS = nrtTS.merge(runAreaSensorNRT(area, 'Sentinel-1'))}
  if (LSTCheck.getValue()) {nrtTS = nrtTS.merge(runAreaSensorNRT(area, 'Landsat'))}
  if (nrtTS.size().gt(0)) {
    nrtTS = nrtTS.sort('system:time_start');
    return ut.monitorChange(nrtTS, nrtParam);
  } else {
    print('Nothing was selected.');
    return ee.Image(0);
  }
};

  // add pixel location
var addPixel = function(coords) {
  var pSize = 0.000135;
  var pixel = ee.Geometry.Rectangle([coords.lon - pSize, coords.lat - pSize, 
                                      coords.lon + pSize, coords.lat + pSize]);
  mapPanel.addLayer(pixel, {color: '0000FF'}, 'Clicked');
};

  // remove a layer
var removeLayer = function(name) {
  var layers = mapPanel.layers();
  var nLayer = layers.length();
  for (var i = nLayer-1; i >= 0; i--) {
    var layer = layers.get(i);
    if (layer.getName().match(name)) {
      layers.remove(layer);
    }
  }
};

  // reset the time series panel
var resetTSPanel = function() {
  tsPanel.clear();
  removeLayer('_');
  removeLayer('Clicked');
};

// ---------------------------------------------------------------
// UIs:
  // map panel
var mapPanel = ui.Map({style: {cursor: 'crosshair'}});
mapPanel.centerObject(testArea, 10);
mapPanel.setOptions('SATELLITE');
mapPanel.addLayer(testArea, {color: 'red'}, 'Test Area');
mapPanel.addLayer(forestMask, mskVisParam, 'Forest Mask', false);

  // menu panel
var trainButton = ui.Button('Train');
var ccdButton = ui.Button('Fit');
var nrtButton = ui.Button('Monitor');
var runButton = ui.Button('Run');
var saveButton = ui.Button('Save');
var menuSet = ui.Panel([ccdButton, nrtButton, runButton], 
                        ui.Panel.Layout.Flow('vertical'));
var ccdSelect = ui.Select(['Landsat', 'Sentinel-2', 'Sentinel-1'], 'Select sensor for CCD.', 'Landsat');
var LSTCheck = ui.Checkbox('Landsat', true);
var S2Check = ui.Checkbox('Sentinel-2', true);
var S1Check = ui.Checkbox('Sentinel-1', false);
var selectSet = ui.Panel([ccdSelect, LSTCheck, S2Check, S1Check], 
                        ui.Panel.Layout.Flow('vertical'));
var menuUISet = ui.Panel([menuSet, selectSet], ui.Panel.Layout.Flow('horizontal'));
var menuPanel = ui.Panel({
  widgets: [ui.Label('Menu'), menuUISet],
  layout: ui.Panel.Layout.Flow('vertical'),
  style: {width: '20%'}});

  // ts panel
var tsPanel = ui.Panel({
  widgets: [],
  style: {position: 'bottom-right', width: '80%'}});

  // ui panel
var controlPanel = ui.Panel({
  style: {height: '30%'},
  widgets:[ui.SplitPanel(tsPanel, menuPanel, 'horizontal', false)]});
var mapPanel2 = ui.Panel({
  style: {height: '70%'},
  widgets:[mapPanel]});
var uiPanel = ui.SplitPanel(mapPanel2, controlPanel, 'vertical');

// ---------------------------------------------------------------
// Runtime functions:
trainButton.onClick(function() {
  var saveCCD = function(ccd, sensor) {
    Export.image.toAsset({
          image: ccd,
          scale: 30,
          assetId: 'projects/bu-nearrealtime/lite/ccd/' + sensor + '_CCD',
          description: 'Save_' + sensor + '_CCD',
          region: testArea,
          maxPixels: 1e13,
          pyramidingPolicy: {'.default': 'sample'}
    });
  };
  var LST = ut.getData(testArea, trainPeriod, 'Landsat');
  saveCCD(ut.runCCD(LST, trainPeriod, 'NDFI').set({region: 'test', sensor: 'Landsat'}), 'LST');
  var S2 = ut.getData(testArea, trainPeriod, 'Sentinel-2');
  saveCCD(ut.runCCD(S2, trainPeriod, 'NDFI').set({region: 'test', sensor: 'Sentinel-2'}), 'S2');
  var S1 = ut.getData(testArea, trainPeriod, 'Sentinel-1');
  saveCCD(ut.runCCD(S1, trainPeriod, 'VV').set({region: 'test', sensor: 'Sentinel-1'}), 'S1');
});

ccdButton.onClick(function() {
  if (listener == 1) {
    ccdButton.setLabel('Fit');
    listener = 0;
  } else {
    nrtButton.setLabel('Monitor');
    ccdButton.setLabel('Cancel');
    listener = 1;
  }
});

nrtButton.onClick(function() {
  if (listener == 2) {
    nrtButton.setLabel('Monitor');
    listener = 0;
  } else {
    nrtButton.setLabel('Cancel');
    ccdButton.setLabel('Fit');
    listener = 2;
  }
});

saveButton.onClick(function() {
  Export.image.toAsset({
        image: alerts,
        scale: 30,
        description: 'SaveAlerts',
        assetId: 'Alerts',
        region: testArea,
        maxPixels: 1e13});
});

runButton.onClick(function() {
  alerts = runNRT(testArea);
  mapPanel.addLayer(alerts, altVisParam, 'Forest Disturbance Alerts');
  saveButton.setDisabled(false);
});

mapPanel.onClick(function(coords) {
  if (listener == 1) {
    chartCCD(coords);
  } else if (listener == 2) {
    chartNRT(coords);
  }
});

// ---------------------------------------------------------------
// Initialization:
//saveButton.setDisabled(true);
ui.root.clear();
ui.root.add(uiPanel);

// End