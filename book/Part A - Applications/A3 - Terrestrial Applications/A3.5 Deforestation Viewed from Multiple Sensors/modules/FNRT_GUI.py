import ee
import geemap

Map = geemap.Map()

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
testArea =

    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[-66.73156878460787, -8.662236005089952],
          [-66.73156878460787, -8.916025640576244],
          [-66.44867083538912, -8.916025640576244],
          [-66.44867083538912, -8.662236005089952]]], None, False)
#**** End of imports. If edited, may not auto-convert in the playground. ****#
# Fusion Near Real-time (GUI)
# Near real-time monitoring of forest disturbance by fusion of
# multi-sensor data.  @author Xiaojing Tang (xjtang@bu.edu).

# ---------------------------------------------------------------
# Model Parameters:
trainPeriod = ee.Dictionary({'start': '2017-01-01', 'end': '2020-01-01'})
monitorPeriod = ee.Dictionary({'start': '2020-01-01', 'end': '2021-01-01'})
fullPeriod = ee.Dictionary({
     'start': trainPeriod.get('start'),
     'end': monitorPeriod.get('end')})
nrtParam = {'z': 2, 'n': 4, 'm': 5, 'maxZ': 10}
optParam = {
  'band': 'NDFI',
  'minRMSE': 0.05,
  'strikeOnly': False,
  'vis': '{bands': ['SWIR1',  'NIR',  'Red'], 'min': 0, 'max': 5000}
}
radParam = {
  'band': 'VV',
  'minRMSE': 0.01,
  'strikeOnly': True,
  'vis': '{bands': ['VV',  'VH',  'ratio'], 'min': 10, 'max': 30}
}
mskVisParam = {'min': 0, 'max': 1, 'palette': ['blue', 'green']}
altVisParam = {'min': 2020.4, 'max': 2021,
                    'palette': ['FF0080', 'EC1280', 'DA2480', 'C83680', 'B64880', 'A35B80', '916D80',
                              '7F7F80', '6D9180', '5BA380', '48B680', '36C880', '24DA80', '12EC80',
                              '00FF80', '00EB89', '00D793', '00C49D', '00B0A7', '009CB0', '0089BA',
                              '0075C4', '0062CE', '004ED7', '003AE1', '0027EB', '0013F5', '0000FF']}

# ---------------------------------------------------------------
# Imports and predefined variables:
listener = 0
ut = require('users/xjtang/fnrt:Lite/Utilities')
hansen = ee.Image('UMD/hansen/global_forest_change_2020_v1_8').unmask()
forestMask = hansen.select('treecover2000').gt(50) \
                  .add(hansen.select('gain')) \
                  .subtract(hansen.select('loss')) \
                  .add(hansen.select('lossyear').eq(20)) \
                  .gt(0)
alerts = None
ccd = ee.ImageCollection('projects/gee-book/assets/A3-5/ccd')

# ---------------------------------------------------------------
# Main functions:
  # run and plot CCD result for a pixel
def chartCCD(coords):
  resetTSPanel()
  sensor = ccdSelect.getValue()
  pixel = ee.Geometry.Point([coords.lon, coords.lat])
  tsPanel.add(ui.Label('Running CCD on ' + sensor + ' data...'))
  addPixel(coords)
  param = None
  if (sensor == 'Sentinel-1') {
    param = radParam
  } else {
    param = optParam
  }
  trainData = ut.getData(pixel, trainPeriod, sensor)
  monitorData = ut.getData(pixel, monitorPeriod, sensor)
  ccdModel = ee.Image(ee.Algorithms.If(
                  ccd.filterMetadata('sensor', 'equals', sensor).first(),
                  ccd.filterMetadata('sensor', 'equals', sensor).first(),
                  ut.runCCD(trainData, trainPeriod, param.band)
                ))
  ccdTS = ut.getTimeSeries(trainData, monitorData, ccdModel, pixel, param.band, 0.1)
  ccdTable = ut.transformToTable(ccdTS, ['dateString', 'train', 'monitor', 'fit'])
  ccdTable.evaluate(function(t, e) {
    chart = ut.createCCDChart(t, param.band, coords.lat, coords.lon)
    chart.onClick(
      def function(date):
        if (date === None) {
          removeLayer('_')
        } else {
          img = ee.Image(ut.getImage(pixel, date, sensor))
          mapPanel.addLayer(img, param.vis, img.get('system:index').getInfo())
          removeLayer('Clicked')
          addPixel(coords)
        }

    )
    tsPanel.clear()
    tsPanel.add(chart)
  })


  # run near-real-time monitoring for one sensor for one pixel
def runPixelSensorNRT(pixel, sensor):
  trainData = ut.getData(pixel, trainPeriod, sensor)
  monitorData = ut.getData(pixel, monitorPeriod, sensor)
  param = None
  if (sensor == 'Sentinel-1') {
    param = radParam
  } else {
    param = optParam
  }
  ccdModel = ee.Image(ee.Algorithms.If(
              ccd.filterMetadata('sensor', 'equals', sensor).first(),
              ccd.filterMetadata('sensor', 'equals', sensor).first(),
              ut.runCCD(trainData, trainPeriod, param.band)
            ))
  ccdTS = ut.getTimeSeries(trainData, monitorData, ccdModel, pixel, param.band)
  Z = ee.FeatureCollection(ut.addPixelZScore(ccdTS, nrtParam.maxZ, param.minRMSE))
  checked = ut.checkPixelZScore(Z, nrtParam.z)
  if ((S2Check.getValue() | LSTCheck.getValue()) & param.strikeOnly) {
    checked = checked.filterMetadata('Ball', 'equals', None)
  }
  return checked


  # run and plot NRT for a pixel
def chartNRT(coords):
  resetTSPanel()
  tsPanel.add(ui.Label('Running NRT...'))
  pixel = ee.Geometry.Point([coords.lon, coords.lat])
  addPixel(coords)
  nrtTS = ee.FeatureCollection([])
  if (S2Check.getValue()) {nrtTS = nrtTS.merge(runPixelSensorNRT(pixel, 'Sentinel-2'))}
  if (S1Check.getValue()) {nrtTS = nrtTS.merge(runPixelSensorNRT(pixel, 'Sentinel-1'))}
  if (LSTCheck.getValue()) {nrtTS = nrtTS.merge(runPixelSensorNRT(pixel, 'Landsat'))}
  nrtTS = nrtTS.filterMetadata('x', 'not_equals', None)
  if (nrtTS.size().gt(0)) {
    nrtMonitor = ee.FeatureCollection(ut.monitorPixelChange(nrtTS.sort('fitTime'), nrtParam))
    nrt = ut.transformToTable(nrtMonitor, ['dateString', 'Z_train', 'Ball', 'Strike', 'StrikeOut'])
    nrt.evaluate(function(t, e) {
      chart = ut.createNRTChart(t, coords.lat, coords.lon)
      tsPanel.clear()
      tsPanel.add(chart)
    })
  } else {
    tsPanel.add(ui.Label('No sensor was selected.'))
  }


  # run near-real-time monitoring for one sensor for an area
def runAreaSensorNRT(area, sensor):
  param = None
  if (sensor == 'Sentinel-1') {
    param = radParam
  } else {
    param = optParam
  }
  monitorData = ut.getData(area, monitorPeriod, sensor)
  ccdModel = ccd.filterMetadata('sensor', 'equals', sensor).first().updateMask(forestMask)
  ccdImg = ut.getCCDImage(ccdModel, param.band)
  synthetics = ut.addSynthetic(monitorData, ccdImg, param.band, sensor)
  monitorRes = ut.getResiduals(synthetics, param.band)
  return ut.getChangeScores(monitorRes, ccdImg.select('.*rmse'),
                            synthetics.select(param.band).mean(),
                            param.minRMSE, nrtParam.z, param.strikeOnly)


  # run near real time
def runNRT(area):
  nrtTS = ee.ImageCollection([])
  if (S2Check.getValue()) {nrtTS = nrtTS.merge(runAreaSensorNRT(area, 'Sentinel-2'))}
  if (S1Check.getValue()) {nrtTS = nrtTS.merge(runAreaSensorNRT(area, 'Sentinel-1'))}
  if (LSTCheck.getValue()) {nrtTS = nrtTS.merge(runAreaSensorNRT(area, 'Landsat'))}
  if (nrtTS.size().gt(0)) {
    nrtTS = nrtTS.sort('system:time_start')
    return ut.monitorChange(nrtTS, nrtParam)
  } else {
    print('Nothing was selected.')
    return ee.Image(0)
  }


  # add pixel location
def addPixel(coords):
  pSize = 0.000135
  pixel = ee.Geometry.Rectangle([coords.lon - pSize, coords.lat - pSize,
                                      coords.lon + pSize, coords.lat + pSize])
  mapPanel.addLayer(pixel, {'color': '0000FF'}, 'Clicked')


  # remove a layer
def removeLayer(name):
  layers = mapPanel.layers()
  nLayer = layers.length()
  for i in range(nLayer-1, 0, -1):
    layer = layers.get(i)
    if (layer.getName().match(name)) {
      layers.remove(layer)
    }



  # reset the time series panel
def resetTSPanel():
  tsPanel.clear()
  removeLayer('_')
  removeLayer('Clicked')


# ---------------------------------------------------------------
# UIs:
  # map panel
mapPanel = ui.Map({'style': '{cursor': 'crosshair'}})
mapPanel.centerObject(testArea, 10)
mapPanel.setOptions('SATELLITE')
mapPanel.addLayer(testArea, {'color': 'red'}, 'Test Area')
mapPanel.addLayer(forestMask, mskVisParam, 'Forest Mask', False)

  # menu panel
trainButton = ui.Button('Train')
ccdButton = ui.Button('Fit')
nrtButton = ui.Button('Monitor')
runButton = ui.Button('Run')
saveButton = ui.Button('Save')
menuSet = ui.Panel([ccdButton, nrtButton, runButton],
                        ui.Panel.Layout.Flow('vertical'))
ccdSelect = ui.Select(['Landsat', 'Sentinel-2', 'Sentinel-1'], 'Select sensor for CCD.', 'Landsat')
LSTCheck = ui.Checkbox('Landsat', True)
S2Check = ui.Checkbox('Sentinel-2', True)
S1Check = ui.Checkbox('Sentinel-1', False)
selectSet = ui.Panel([ccdSelect, LSTCheck, S2Check, S1Check],
                        ui.Panel.Layout.Flow('vertical'))
menuUISet = ui.Panel([menuSet, selectSet], ui.Panel.Layout.Flow('horizontal'))
menuPanel = ui.Panel({
  'widgets': [ui.Label('Menu'), menuUISet],
  'layout': ui.Panel.Layout.Flow('vertical'),
  'style': '{width': '20%'}})

  # ts panel
tsPanel = ui.Panel({
  'widgets': [],
  'style': '{position': 'bottom-right', 'width': '80%'}})

  # ui panel
controlPanel = ui.Panel({
  'style': '{height': '30%'},
  'widgets':[ui.SplitPanel(tsPanel, menuPanel, 'horizontal', False)]})
mapPanel2 = ui.Panel({
  'style': '{height': '70%'},
  'widgets':[mapPanel]})
uiPanel = ui.SplitPanel(mapPanel2, controlPanel, 'vertical')

# ---------------------------------------------------------------
# Runtime functions:
trainButton.onClick(function() {
  def saveCCD(ccd, sensor):
    Export.image.toAsset({
          'image': ccd,
          'scale': 30,
          'assetId': 'projects/bu-nearrealtime/lite/ccd/' + sensor + '_CCD',
          'description': 'Save_' + sensor + '_CCD',
          'region': testArea,
          'maxPixels': 1e13,
          'pyramidingPolicy': {'.default': 'sample'}
    })

  LST = ut.getData(testArea, trainPeriod, 'Landsat')
  saveCCD(ut.runCCD(LST, trainPeriod, 'NDFI').set({'region': 'test', 'sensor': 'Landsat'}), 'LST')
  S2 = ut.getData(testArea, trainPeriod, 'Sentinel-2')
  saveCCD(ut.runCCD(S2, trainPeriod, 'NDFI').set({'region': 'test', 'sensor': 'Sentinel-2'}), 'S2')
  S1 = ut.getData(testArea, trainPeriod, 'Sentinel-1')
  saveCCD(ut.runCCD(S1, trainPeriod, 'VV').set({'region': 'test', 'sensor': 'Sentinel-1'}), 'S1')
})

ccdButton.onClick(function() {
  if (listener == 1) {
    ccdButton.setLabel('Fit')
    listener = 0
  } else {
    nrtButton.setLabel('Monitor')
    ccdButton.setLabel('Cancel')
    listener = 1
  }
})

nrtButton.onClick(function() {
  if (listener == 2) {
    nrtButton.setLabel('Monitor')
    listener = 0
  } else {
    nrtButton.setLabel('Cancel')
    ccdButton.setLabel('Fit')
    listener = 2
  }
})

saveButton.onClick(function() {
  Export.image.toAsset({
        'image': alerts,
        'scale': 30,
        'description': 'SaveAlerts',
        'assetId': 'Alerts',
        'region': testArea,
        'maxPixels': 1e13})
})

runButton.onClick(function() {
  alerts = runNRT(testArea)
  mapPanel.addLayer(alerts, altVisParam, 'Forest Disturbance Alerts')
  saveButton.setDisabled(False)
})

mapPanel.onClick(function(coords) {
  if (listener == 1) {
    chartCCD(coords)
  } else if (listener == 2) {
    chartNRT(coords)
  }
})

# ---------------------------------------------------------------
# Initialization:
#saveButton.setDisabled(True)
ui.root.clear()
ui.root.add(uiPanel)

# End
Map
