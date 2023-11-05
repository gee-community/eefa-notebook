import ee 
import geemap

Map = geemap.Map()

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
DIVsand = ee.Geometry.MultiPolygon(
        [[[[23.85533614379952, 35.525671008126785],
           [23.85808272583077, 35.52511217612521],
           [23.860142662354207, 35.53880243984323],
           [23.85653777343819, 35.539500860050644]]],
         [[[23.783753349610066, 35.54863600968416],
           [23.801091148682332, 35.55114998568017],
           [23.799546196289754, 35.55464148823767],
           [23.782723381348347, 35.551289648702024]]]]),
land = ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.LineString(
                [[23.813750501438804, 35.53087476744296],
                 [23.834178205296226, 35.52696311538223],
                 [23.81306385593099, 35.53269082679277],
                 [23.836753125950523, 35.52863956104383],
                 [23.81684040622396, 35.53310991157428],
                 [23.835208173557945, 35.53073506886724],
                 [23.820273633763023, 35.53422746028901],
                 [23.83160328464193, 35.53324960601498]]),
            {
              "class": 0,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.LineString(
                [[23.77461170749349, 35.550849159238616],
                 [23.776328321263023, 35.53967528733693],
                 [23.791262861057945, 35.53478622880854],
                 [23.778044935032554, 35.540373699944034],
                 [23.775984998509117, 35.550988822784504],
                 [23.779589887425132, 35.5414911474658],
                 [23.792464490696617, 35.53646251101553],
                 [23.774783368870445, 35.543027612387064],
                 [23.777014966770835, 35.54959217637752],
                 [23.77667164401693, 35.53716095159702],
                 [23.79315113620443, 35.53855781451608]]),
            {
              "class": 0,
              "system:index": "1"
            })]),
water = ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.LineString(
                [[23.815368450747332, 35.53525030188046],
                 [23.82712725506862, 35.538463126752895],
                 [23.813823498354754, 35.53629797630387],
                 [23.826955593691668, 35.53972028406574],
                 [23.813051022158465, 35.53720594973632],
                 [23.826268948183856, 35.54104726207508],
                 [23.81339434491237, 35.5381139128914],
                 [23.825582302676043, 35.54230437888493],
                 [23.81313685284694, 35.53951075921525],
                 [23.827213085757098, 35.53769485425075],
                 [23.823264874087176, 35.543421799507115]]),
            {
              "class": 1,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.LineString(
                [[23.93656138287624, 35.520162273141004],
                 [23.922656811343035, 35.52700811924147],
                 [23.939651287661395, 35.52114028690721],
                 [23.920596874819598, 35.529662473875746],
                 [23.938449658022723, 35.52379483562914]]),
            {
              "class": 1,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.LineString(
                [[23.789275921450457, 35.5804973627026],
                 [23.79768732892116, 35.57972949300953],
                 [23.786357678042254, 35.579589879547086],
                 [23.798631466494403, 35.578577674666],
                 [23.78446940289577, 35.578752193661586],
                 [23.798502720461688, 35.577670169758946],
                 [23.78292445050319, 35.57791449901465],
                 [23.79210841193106, 35.5772866256402],
                 [23.79923228131374, 35.57651832180017]]),
            {
              "class": 1,
              "system:index": "2"
            })]),
sunglint = ee.Geometry.MultiPolygon(
        [[[[23.786748725416697, 35.55612383758693],
           [23.786748725416697, 35.54634742800967],
           [23.802541572096384, 35.54634742800967],
           [23.802541572096384, 35.55612383758693]]],
         [[[23.829664069654978, 35.550537463803785],
           [23.829664069654978, 35.5441126527256],
           [23.842710334303415, 35.5441126527256],
           [23.842710334303415, 35.550537463803785]]],
         [[[23.871206122877634, 35.547464792297085],
           [23.871206122877634, 35.54271588654758],
           [23.87978919172529, 35.54271588654758],
           [23.87978919172529, 35.547464792297085]]]], None, False)
#**** End of imports. If edited, may not auto-convert in the playground. ****#

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A2.2 Benthic Habitats
#  Checkpoint:   A22e
#  Authors:      Dimitris Poursanidis, Aurélie C. Shapiro, Spyros Christofilakos
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Section 1
# Import and display satellite image.
planet = ee.Image('projects/gee-book/assets/A2-2/20200505_N2000') \
    .divide(10000)

Map.centerObject(planet, 12)
visParams = {
    'bands': ['b3', 'b2', 'b1'],
    'min': 0.17,
    'max': 0.68,
    'gamma': 0.8
}
Map.addLayer({
    'eeObject': planet,
    'visParams': visParams,
    'name': 'planet initial',
    'shown': True
})
# ------------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------------

# Section 2
# Mask based to NDWI and RF.
def landmask(img):
    ndwi = img.normalizedDifference(['b2', 'b4'])
    training = ndwi.sampleRegions(land.merge(water), ['class'],
        3)
    trained = ee.Classifier.smileRandomForest(10) \
        .train(training, 'class')
    classified = ndwi.classify(trained)
    mask = classified.eq(1)

    return img.updateMask(mask)


maskedImg = landmask(planet)

Map.addLayer(maskedImg, visParams, 'maskedImg', False)

# Sun-glint correction.
def sunglintRemoval(img):
    linearFit1 = img.select(['b4', 'b1']).reduceRegion({
        'reducer': ee.Reducer.linearFit(),
        'geometry': sunglint,
        'scale': 3,
        'maxPixels': 1e12,
        'bestEffort': True,
    })
    linearFit2 = img.select(['b4', 'b2']).reduceRegion({
        'reducer': ee.Reducer.linearFit(),
        'geometry': sunglint,
        'scale': 3,
        'maxPixels': 1e12,
        'bestEffort': True,
    })
    linearFit3 = img.select(['b4', 'b3']).reduceRegion({
        'reducer': ee.Reducer.linearFit(),
        'geometry': sunglint,
        'scale': 3,
        'maxPixels': 1e12,
        'bestEffort': True,
    })

    slopeImage = ee.Dictionary({
        'b1': linearFit1.get('scale'),
        'b2': linearFit2.get('scale'),
        'b3': linearFit3.get('scale')
    }).toImage()

    minNIR = img.select('b4').reduceRegion({
        'reducer': ee.Reducer.min(),
        'geometry': sunglint,
        'scale': 3,
        'maxPixels': 1e12,
        'bestEffort': True,
    }).toImage(['b4'])

    return img.select(['b1', 'b2', 'b3']) \
        .subtract(slopeImage.multiply((img.select('b4')).subtract(
            minNIR))) \
        .addBands(img.select('b4'))

sgImg = sunglintRemoval(maskedImg)
Map.addLayer(sgImg, visParams, 'sgImg', False)

# DIV procedure.
def kernel(img):
    boxcar = ee.Kernel.square({
        'radius': 2,
        'units': 'pixels',
        'normalize': True
    })
    return img.convolve(boxcar)


def makePositive(img):
    return img.where(img.lte(0), 0.0001)


def div(img):
    band1 = ee.List(['b1', 'b2', 'b3', 'b1', 'b2'])
    band2 = ee.List(['b3', 'b3', 'b2', 'b2', 'b1'])
    nband = ee.List(['b1b3', 'b2b3', 'b3b2', 'b1b2', 'b2b1'])

    for i in range(0, 5, 1):
        x = band1.get(i)
        y = band2.get(i)
        z = nband.get(i)

        imageLog = img.select([x, y]).log()

        covariance = imageLog.toArray().reduceRegion({
            'reducer': ee.Reducer.covariance(),
            'geometry': DIVsand,
            'scale': 3,
            'maxPixels': 1e12,
            'bestEffort': True,
        })

        covarMatrix = ee.Array(covariance.get('array'))
        var1 = covarMatrix.get([0, 0])
        var2 = covarMatrix.get([1, 1])
        covar = covarMatrix.get([0, 1])

        a = var1.subtract(var2).divide(covar.multiply(2))
        attenCoeffRatio = a.add(((a.pow(2)).add(1)).sqrt())

        depthInvariantIndex = img.expression(
            'image1 - (image2 * coeff)', {
                'image1': imageLog.select([x]),
                'image2': imageLog.select([y]),
                'coeff': attenCoeffRatio
            })

        img = ee.Image.cat([img, depthInvariantIndex.select([x], [
            z
        ])])

    return img


divImg = div(kernel(makePositive(sgImg))).select('b[1-3]',
    'b1b2')
vivVisParams = {
    'bands': ['b1b2'],
    'min': -0.81,
    'max': -0.04,
    'gamma': 0.75
}
Map.addLayer(divImg, vivVisParams, 'divImg', False)

# ------------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------------

# Section 3, classification
# Import of reference data and split.
softBottom = ee.FeatureCollection(
    'projects/gee-book/assets/A2-2/SoftBottom')
rockyBottom = ee.FeatureCollection(
    'projects/gee-book/assets/A2-2/RockyBottom')
pO = ee.FeatureCollection('projects/gee-book/assets/A2-2/PO')

sand = ee.FeatureCollection.randomPoints(softBottom, 150).map(
    def function(s):
        return s.set('class', 0)
    ).randomColumn()
sandT = sand.filter(ee.Filter.lte('random', 0.7)).aside(print,
    'sand training')
sandV = sand.filter(ee.Filter.gt('random', 0.7)).aside(print,
    'sand validation')
Map.addLayer(sandT, {
    'color': 'yellow'
}, 'Sand Training', False)
Map.addLayer(sandV, {
    'color': 'yellow'
}, 'Sand Validation', False)

hard = ee.FeatureCollection.randomPoints(rockyBottom, 79).map(
    def function(s):
        return s.set('class', 1)
    ).randomColumn()
hardT = hard.filter(ee.Filter.lte('random', 0.7)).aside(print,
    'hard training')
hardV = hard.filter(ee.Filter.gt('random', 0.7)).aside(print,
    'hard validation')
Map.addLayer(hardT, {
    'color': 'red'
}, 'Rock Training', False)
Map.addLayer(hardV, {
    'color': 'red'
}, 'Rock Validation', False)


def func_pym(s):
        return s.set('class', 2)

posi = pO.map(func_pym) \
    .randomColumn('random')
posiT = posi.filter(ee.Filter.lte('random', 0.7)).aside(print,
    'posi training')
posiV = posi.filter(ee.Filter.gt('random', 0.7)).aside(print,
    'posi validation')
Map.addLayer(posiT, {
    'color': 'green'
}, 'Posidonia Training', False)
Map.addLayer(posiV, {
    'color': 'green'
}, 'Posidonia Validation', False)

# Classification procedure.
def classify(img):
    mergedT = ee.FeatureCollection([sandT, hardT, posiT]) \
        .flatten()
    training = img.sampleRegions(mergedT, ['class'], 3)
    trained = ee.Classifier.libsvm({
        'kernelType': 'RBF',
        'gamma': 1,
        'cost': 500
    }).train(training, 'class')
    classified = img.classify(trained)

    mergedV = ee.FeatureCollection([sandV, hardV, posiV]) \
        .flatten()
    accuracyCol = classified.unmask().reduceRegions({
        'collection': mergedV,
        'reducer': ee.Reducer.first(),
        'scale': 10
    })
    classificationErrorMatrix = accuracyCol.errorMatrix({
        'actual': 'class',
        'predicted': 'first',
        'order': [0, 1, 2]
    })
    classNames = ['soft_bot', 'hard_bot', 'seagrass']
    accuracyOA = classificationErrorMatrix.accuracy()
    accuraccyCons = ee.Dictionary.fromLists({
        'keys': classNames,
        'values': classificationErrorMatrix.consumersAccuracy() \
            .toList() \
            .flatten()
    })
    accuracyProd = ee.Dictionary.fromLists({
        'keys': classNames,
        'values': classificationErrorMatrix.producersAccuracy() \
            .toList() \
            .flatten()
    })

    classificationErrormatrixArray = classificationErrorMatrix \
        .array()

    def arrayToDatatable(array):
        classesNames = ee.List(classNames)

        def toTableColumns(s):
            return {
                'id': s,
                'label': s,
                'type': 'number'
            }

        columns = classesNames.map(toTableColumns)

        def featureToTableRow(f):
            return {

def func_zns(c):
                    return {
                        'v': c
                    }

                'c': ee.List(f).map(func_zns)





            }

        rows = array.toList().map(featureToTableRow)
        return ee.Dictionary({
            'cols': columns,
            'rows': rows
        })
    

    dataTable = arrayToDatatable(classificationErrormatrixArray) \
        .evaluate(function(dataTable) {
            print('------------- Error matrix -------------',
                ui.Chart(dataTable, 'Table') \
                .setOptions({
                    'pageSize': 15
                }),
                'rows: reference, 'cols': mapped')
        })
    print('Overall Accuracy', accuracyOA)
    print('Users accuracy', accuraccyCons)
    print('Producers accuracy', accuracyProd)
    return classified


svmClassification = classify(divImg)
svmVis = {
    'min': 0,
    'max': 2,
    'palette': ['ffffbf', 'fc8d59', '91cf60']
}
Map.addLayer(svmClassification, svmVis, 'classification')

# ------------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------------

# Section 4, Bathymetry
# Import and split training and validation data for the bathymetry.
depth = ee.FeatureCollection(
    'projects/gee-book/assets/A2-2/DepthDataTill09072020_v2')
depth = depth.randomColumn()
depthT = depth.filter(ee.Filter.lte('random', 0.7))
depthV = depth.filter(ee.Filter.gt('random', 0.7))
Map.addLayer(depthT, {
    'color': 'black'
}, 'Depth Training', False)
Map.addLayer(depthV, {
    'color': 'gray'
}, 'Depth Validation', False)

def vector2image(vector):
    rasterisedVectorData = vector \
        .filter(ee.Filter.neq('Depth',
            None)) # Filter out NA depth values. \
        .reduceToImage({
            'properties': ['Depth'],
            'reducer': ee.Reducer.mean()
        })
    return (rasterisedVectorData)


depthTImage = vector2image(depthT) \
    .aside(Map.addLayer, {
        'color': 'white'
    }, 'Depth Training2', False)
depthVImage = vector2image(depthV) \
    .aside(Map.addLayer, {
        'color': 'white'
    }, 'Depth Validation2', False)

def rfbathymetry(img):
    training = img.sampleRegions({
        'collection': depthT,
        'scale': 3
    })

    regclass = ee.Classifier.smileRandomForest(15) \
        .train(training, 'Depth')
    bathyClass = img \
        .classify(regclass.setOutputMode('REGRESSION')).rename(
            'Depth')

    sdbEstimate = bathyClass.clip(depthV)

    # Prepare data by putting SDB estimated data and in situ data
    # in one image to compare them afterwards.
    imageI = ee.Image.cat([sdbEstimate, depthVImage])
    # Calculate covariance.
    covariance = imageI.toArray().reduceRegion({
        'reducer': ee.Reducer.covariance(),
        'geometry': depthV,
        'scale': 3,
        'bestEffort': True,
        'maxPixels': 1e9
    })
    covarMatrix = ee.Array(covariance.get('array'))

    rSqr = covarMatrix.get([0, 1]).pow(2) \
        .divide(covarMatrix.get([0, 0]) \
            .multiply(covarMatrix.get([1, 1])))

    deviation = depthVImage.select('mean') \
        .subtract(sdbEstimate.select('Depth')).pow(2)

    rmse = ee.Number(deviation.reduceRegion({
            'reducer': ee.Reducer.mean(),
            'geometry': depthV,
            'scale': 3,
            'bestEffort': True,
            'maxPixels': 1e12
        }).get('mean')) \
        .sqrt()

    # Print together, so that they appear in the same output.
    print('R²', rSqr, 'RMSE', rmse)

    return bathyClass


rfBathymetry = rfbathymetry(divImg)
bathyVis = {
    'min': -50,
    'max': 0,
    'palette': ['084594', '2171b5', '4292c6', '6baed6',
        '9ecae1', 'c6dbef', 'deebf7', 'f7fbff'
    ]
}
Map.addLayer(rfBathymetry, bathyVis, 'bathymetry')

# ------------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------------
Map