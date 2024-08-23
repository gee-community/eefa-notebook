import ee
import math
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A3.5 Deforestation Viewed from Multiple Sensors
#  Checkpoint:   A35e
#  Author:       Xiaojing Tang
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

testArea = ee.Geometry.Polygon(
    [
        [
            [-66.73156878460787, -8.662236005089952],
            [-66.73156878460787, -8.916025640576244],
            [-66.44867083538912, -8.916025640576244],
            [-66.44867083538912, -8.662236005089952]
        ]
    ])

Map.centerObject(testArea)

# Start and end of the training and monitoring period.
trainPeriod = ee.Dictionary({
    'start': '2017-01-01',
    'end': '2020-01-01'
})
monitorPeriod = ee.Dictionary({
    'start': '2020-01-01',
    'end': '2021-01-01'
})

# Near-real-time monitoring parameters.
nrtParam = {
    'z': 2,
    'm': 5,
    'n': 4
}

# Sensor specific parameters.
lstParam = {
    'band': 'NDFI',
    'minRMSE': 0.05,
    'strikeOnly': False
}
s2Param = {
    'band': 'NDFI',
    'minRMSE': 0.05,
    'strikeOnly': False
}
s1Param = {
    'band': 'VV',
    'minRMSE': 0.01,
    'strikeOnly': True
}

# ------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------

def unmixing(col):

    # Define endmembers and cloud fraction threshold.
    gv = [500, 900, 400, 6100, 3000, 1000]
    npv = [1400, 1700, 2200, 3000, 5500, 3000]
    soil = [2000, 3000, 3400, 5800, 6000, 5800]
    shade = [0, 0, 0, 0, 0, 0]
    cloud = [9000, 9600, 8000, 7800, 7200, 6500]
    cfThreshold = 0.05


def func_hwr(img):
        # Select the spectral bands and perform unmixing
        unmixed = img.select(['Blue', 'Green', 'Red',
                'NIR',
                'SWIR1', 'SWIR2'
            ]) \
            .unmix([gv, shade, npv, soil, cloud], True,
                True) \
            .rename(['GV', 'Shade', 'NPV', 'Soil',
                'Cloud'
            ])

        # Calculate Normalized Difference Fraction Index.+ \
        NDFI = unmixed.expression(
            '10000 * ((GV / (1 - SHADE)) - (NPV + SOIL)) / ' + \
            '((GV / (1 - SHADE)) + (NPV + SOIL))', {
                'GV': unmixed.select('GV'),
                'SHADE': unmixed.select('Shade'),
                'NPV': unmixed.select('NPV'),
                'SOIL': unmixed.select('Soil')
            }).rename('NDFI')

        # Mask cloudy pixel.
        maskCloud = unmixed.select('Cloud').lt(
            cfThreshold)
        # Mask all shade pixel.
        maskShade = unmixed.select('Shade').lt(1)
        # Mask pixel where NDFI cannot be calculated.
        maskNDFI = unmixed.expression(
            '(GV / (1 - SHADE)) + (NPV + SOIL)', {
                'GV': unmixed.select('GV'),
                'SHADE': unmixed.select('Shade'),
                'NPV': unmixed.select('NPV'),
                'SOIL': unmixed.select('Soil')
            }).gt(0)

        # Scale fractions to 0-10000 and apply masks.
        return img \
            .addBands(unmixed.select(['GV', 'Shade',
                    'NPV', 'Soil'
                ]) \
                .multiply(10000)) \
            .addBands(NDFI) \
            .updateMask(maskCloud) \
            .updateMask(maskNDFI) \
            .updateMask(maskShade)

    return col.map(func_hwr)

















































input = require(
    'projects/gee-edu/book:Part A - Applications/A3 - Terrestrial Applications/A3.5 Deforestation Viewed from Multiple Sensors/modules/Inputs'
)
lstTraining = unmixing(input.loadLandsatData(testArea,
    trainPeriod))
lstMonitoring = unmixing(input.loadLandsatData(testArea,
    monitorPeriod))
s2Training = unmixing(input.loadS2Data(testArea, trainPeriod))
s2Monitoring = unmixing(input.loadS2Data(testArea,
    monitorPeriod))
s1Training = input.loadS1Data(testArea, trainPeriod)
s1Monitoring = input.loadS1Data(testArea, monitorPeriod)

hansen = ee.Image('UMD/hansen/global_forest_change_2020_v1_8') \
    .unmask()
forestMask = hansen.select('treecover2000') \
    .gt(50) \
    .add(hansen.select('gain')) \
    .subtract(hansen.select('loss')) \
    .add(hansen.select('lossyear') \
        .eq(20)) \
    .gt(0) \
    .clip(testArea)

maskVis = {
    'min': 0,
    'max': 1,
    'palette': ['blue', 'green']
}
Map.addLayer(forestMask, maskVis, 'Forest Mask')
print('lstTraining', lstTraining)
print('lstMonitoring', lstMonitoring)
print('s2Training', s2Training)
print('s2Monitoring', s2Monitoring)
print('s1Training', s1Training)
print('s1Monitoring', s1Monitoring)

# ------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------

def toFracYear(date):
    year = date.get('year')
    fYear = date.difference(
        ee.Date.fromYMD(year, 1, 1), 'year')
    return year.add(fYear)


def fitHarmonicModel(col, band):
    # Function to add dependent variables to an image.
    def addDependents(img):
        # Transform time variable to fractional year.
        t = ee.Number(toFracYear(
            ee.Date(img.get('system:time_start')), 1))
        omega = 2.0 * math.pi
        # Construct dependent variables image.
        dependents = ee.Image.constant([
                1, t,
                t.multiply(omega).cos(),
                t.multiply(omega).sin(),
                t.multiply(omega * 2).cos(),
                t.multiply(omega * 2).sin(),
                t.multiply(omega * 3).cos(),
                t.multiply(omega * 3).sin()
            ]) \
            .float() \
            .rename(['INTP', 'SLP', 'COS', 'SIN',
                'COS2', 'SIN2', 'COS3', 'SIN3'
            ])
        return img.addBands(dependents)


    # Function to add dependent variable images to all images.
    def prepareData(col, band):

def func_lzm(img):
            return addDependents(img.select(band)) \
                .select(['INTP', 'SLP', 'COS',
                    'SIN',
                    'COS2', 'SIN2', 'COS3',
                    'SIN3',
                    band
                ]) \
                .updateMask(img.select(band) \
                    .mask())

        return ee.ImageCollection(col.map(func_lzm
))









))


    col2 = prepareData(col, band)
    # Fit model to data using robust linear regression.
    ccd = col2 \
        .reduce(ee.Reducer.robustLinearRegression(8, 1), 4) \
        .rename([band + '_coefs', band + '_rmse'])

    # Return model coefficients and model rmse.
    return ccd.select(band + '_coefs').arrayTranspose() \
        .addBands(ccd.select(band + '_rmse'))


# Fit harmonic models to training data of all sensors.
lstModel = fitHarmonicModel(lstTraining, lstParam.band) \
    .set({
        'region': 'test',
        'sensor': 'Landsat'
    })
s2Model = fitHarmonicModel(s2Training, s2Param.band) \
    .set({
        'region': 'test',
        'sensor': 'Sentinel-2'
    })
s1Model = fitHarmonicModel(s1Training, s2Param.band) \
    .set({
        'region': 'test',
        'sensor': 'Sentinel-1'
    })

# Define function to save the results.
def saveModel(model, prefix):
    Export.image.toAsset({
        'image': model,
        'scale': 30,
        'assetId': prefix + '_CCD',
        'description': 'Save_' + prefix + '_CCD',
        'region': testArea,
        'maxPixels': 1e13,
        'pyramidingPolicy': {
            '.default': 'sample'
        }
    })


# Run the saving function.
saveModel(lstModel, 'LST')
saveModel(s2Model, 'S2')
saveModel(s1Model, 'S1')

# ------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------

models = ee.ImageCollection('projects/gee-book/assets/A3-5/ccd')
lstModel = models \
    .filterMetadata('sensor', 'equals', 'Landsat').first()
s2Model = models \
    .filterMetadata('sensor', 'equals', 'Sentinel-2').first()
s1Model = models \
    .filterMetadata('sensor', 'equals', 'Sentinel-1').first()

def dearrayModel(model, band):
    band = band + '_'

    # Function to extract a non-harmonic coefficients.
    def genCoefImg(model, band, coef):
        zeros = ee.Array(0).repeat(0, 1)
        coefImg = model.select(band + coef) \
            .arrayCat(zeros, 0).float() \
            .arraySlice(0, 0, 1)
        return ee.Image(coefImg \
            .arrayFlatten([
                [ee.String('S1_') \
                    .cat(band).cat(coef)
                ]
            ]))


    # Function to extract harmonic coefficients.
    def genHarmImg(model, band):
        harms = ['INTP', 'SLP', 'COS', 'SIN',
            'COS2', 'SIN2', 'COS3', 'SIN3'
        ]
        zeros = ee.Image(ee.Array([
                ee.List.repeat(0, harms.length)
            ])) \
            .arrayRepeat(0, 1)
        coefImg = model.select(band + 'coefs') \
            .arrayCat(zeros, 0).float() \
            .arraySlice(0, 0, 1)
        return ee.Image(coefImg \
            .arrayFlatten([
                [ee.String(band).cat('coef')], harms
            ]))


    # Extract harmonic coefficients and rmse.
    rmse = genCoefImg(model, band, 'rmse')
    coef = genHarmImg(model, band)
    return ee.Image.cat(rmse, coef)


def createPredImg(modelImg, img, band, sensor):
    # Reformat date.
    date = toFracYear(ee.Date(img.get('system:time_start')))
    dateString = ee.Date(img.get('system:time_start')) \
        .format('yyyyMMdd')
    # List of coefficients .
    coefs = ['INTP', 'SLP', 'COS', 'SIN',
        'COS2', 'SIN2', 'COS3', 'SIN3'
    ]
    # Get coefficients images from model image.

def func_lyy(coef):
        return modelImg.select(".*".concat(coef))

    coef = ee.Image(coefs.map(func_lyy
)).rename(coefs)

)).rename(coefs)
    t = ee.Number(date)
    omega = 2.0 * math.pi
    # Construct dependent variables.
    pred = ee.Image.constant([
            1, t,
            t.multiply(omega).cos(),
            t.multiply(omega).sin(),
            t.multiply(omega * 2).cos(),
            t.multiply(omega * 2).sin(),
            t.multiply(omega * 3).cos(),
            t.multiply(omega * 3).sin()
        ]) \
        .float()
    # Matrix multiply dependent variables with coefficients.
    return pred.multiply(coef).reduce('sum') \
        .addBands(img, [band]).rename(['predicted', band]) \
        .set({
            'sensor': sensor,
            'system:time_start': img.get('system:time_start'),
            'dateString': dateString
        })


def addPredicted(data, modelImg, band, sensor):

def func_cfe(img):
        return createPredImg(modelImg, img, band,
            sensor)

    return ee.ImageCollection(data.map(func_cfe
))


))


# Convert models to non-array images.
lstModelImg = dearrayModel(lstModel, lstParam.band)
s2ModelImg = dearrayModel(s2Model, s2Param.band)
s1ModelImg = dearrayModel(s1Model, s1Param.band)

# Add predicted image to each real image.
lstPredicted = addPredicted(lstMonitoring, lstModelImg,
    lstParam.band, 'Landsat')
s2Predicted = addPredicted(s2Monitoring, s2ModelImg,
    s2Param.band, 'Sentinel-2')
s1Predicted = addPredicted(s1Monitoring, s1ModelImg,
    s1Param.band, 'Sentinel-1')

print('lstPredicted', lstPredicted)

# ------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------
Map
