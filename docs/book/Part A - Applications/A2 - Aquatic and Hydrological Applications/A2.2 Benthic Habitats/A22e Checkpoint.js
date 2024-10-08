/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var DIVsand = /* color: #fbff00 */ee.Geometry.MultiPolygon(
        [[[[23.85533614379952, 35.525671008126785],
           [23.85808272583077, 35.52511217612521],
           [23.860142662354207, 35.53880243984323],
           [23.85653777343819, 35.539500860050644]]],
         [[[23.783753349610066, 35.54863600968416],
           [23.801091148682332, 35.55114998568017],
           [23.799546196289754, 35.55464148823767],
           [23.782723381348347, 35.551289648702024]]]]),
    land = /* color: #ff0000 */ee.FeatureCollection(
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
    water = /* color: #0d9ad6 */ee.FeatureCollection(
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
    sunglint = /* color: #f5a400 */ee.Geometry.MultiPolygon(
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
           [23.87978919172529, 35.547464792297085]]]], null, false);
/***** End of imports. If edited, may not auto-convert in the playground. *****/

//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  Chapter:      A2.2 Benthic Habitats
//  Checkpoint:   A22e
//  Authors:      Dimitris Poursanidis, Aurélie C. Shapiro, Spyros Christofilakos
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

// Section 1
// Import and display satellite image.
var planet = ee.Image('projects/gee-book/assets/A2-2/20200505_N2000')
    .divide(10000);

Map.centerObject(planet, 12);
var visParams = {
    bands: ['b3', 'b2', 'b1'],
    min: 0.17,
    max: 0.68,
    gamma: 0.8
};
Map.addLayer({
    eeObject: planet,
    visParams: visParams,
    name: 'planet initial',
    shown: true
});
// ------------------------------------------------------------------------------
// CHECKPOINT
// ------------------------------------------------------------------------------

// Section 2
// Mask based to NDWI and RF.
function landmask(img) {
    var ndwi = img.normalizedDifference(['b2', 'b4']);
    var training = ndwi.sampleRegions(land.merge(water), ['class'],
        3);
    var trained = ee.Classifier.smileRandomForest(10)
        .train(training, 'class');
    var classified = ndwi.classify(trained);
    var mask = classified.eq(1);

    return img.updateMask(mask);
}

var maskedImg = landmask(planet);

Map.addLayer(maskedImg, visParams, 'maskedImg', false);

// Sun-glint correction.
function sunglintRemoval(img) {
    var linearFit1 = img.select(['b4', 'b1']).reduceRegion({
        reducer: ee.Reducer.linearFit(),
        geometry: sunglint,
        scale: 3,
        maxPixels: 1e12,
        bestEffort: true,
    });
    var linearFit2 = img.select(['b4', 'b2']).reduceRegion({
        reducer: ee.Reducer.linearFit(),
        geometry: sunglint,
        scale: 3,
        maxPixels: 1e12,
        bestEffort: true,
    });
    var linearFit3 = img.select(['b4', 'b3']).reduceRegion({
        reducer: ee.Reducer.linearFit(),
        geometry: sunglint,
        scale: 3,
        maxPixels: 1e12,
        bestEffort: true,
    });

    var slopeImage = ee.Dictionary({
        'b1': linearFit1.get('scale'),
        'b2': linearFit2.get('scale'),
        'b3': linearFit3.get('scale')
    }).toImage();

    var minNIR = img.select('b4').reduceRegion({
        reducer: ee.Reducer.min(),
        geometry: sunglint,
        scale: 3,
        maxPixels: 1e12,
        bestEffort: true,
    }).toImage(['b4']);

    return img.select(['b1', 'b2', 'b3'])
        .subtract(slopeImage.multiply((img.select('b4')).subtract(
            minNIR)))
        .addBands(img.select('b4'));
}
var sgImg = sunglintRemoval(maskedImg);
Map.addLayer(sgImg, visParams, 'sgImg', false);

// DIV procedure.
function kernel(img) {
    var boxcar = ee.Kernel.square({
        radius: 2,
        units: 'pixels',
        normalize: true
    });
    return img.convolve(boxcar);
}

function makePositive(img) {
    return img.where(img.lte(0), 0.0001);
}

function div(img) {
    var band1 = ee.List(['b1', 'b2', 'b3', 'b1', 'b2']);
    var band2 = ee.List(['b3', 'b3', 'b2', 'b2', 'b1']);
    var nband = ee.List(['b1b3', 'b2b3', 'b3b2', 'b1b2', 'b2b1']);

    for (var i = 0; i < 5; i += 1) {
        var x = band1.get(i);
        var y = band2.get(i);
        var z = nband.get(i);

        var imageLog = img.select([x, y]).log();

        var covariance = imageLog.toArray().reduceRegion({
            reducer: ee.Reducer.covariance(),
            geometry: DIVsand,
            scale: 3,
            maxPixels: 1e12,
            bestEffort: true,
        });

        var covarMatrix = ee.Array(covariance.get('array'));
        var var1 = covarMatrix.get([0, 0]);
        var var2 = covarMatrix.get([1, 1]);
        var covar = covarMatrix.get([0, 1]);

        var a = var1.subtract(var2).divide(covar.multiply(2));
        var attenCoeffRatio = a.add(((a.pow(2)).add(1)).sqrt());

        var depthInvariantIndex = img.expression(
            'image1 - (image2 * coeff)', {
                'image1': imageLog.select([x]),
                'image2': imageLog.select([y]),
                'coeff': attenCoeffRatio
            });

        img = ee.Image.cat([img, depthInvariantIndex.select([x], [
            z
        ])]);
    }
    return img;
}

var divImg = div(kernel(makePositive(sgImg))).select('b[1-3]',
    'b1b2');
var vivVisParams = {
    bands: ['b1b2'],
    min: -0.81,
    max: -0.04,
    gamma: 0.75
};
Map.addLayer(divImg, vivVisParams, 'divImg', false);

// ------------------------------------------------------------------------------
// CHECKPOINT
// ------------------------------------------------------------------------------

// Section 3, classification
// Import of reference data and split.
var softBottom = ee.FeatureCollection(
    'projects/gee-book/assets/A2-2/SoftBottom');
var rockyBottom = ee.FeatureCollection(
    'projects/gee-book/assets/A2-2/RockyBottom');
var pO = ee.FeatureCollection('projects/gee-book/assets/A2-2/PO');

var sand = ee.FeatureCollection.randomPoints(softBottom, 150).map(
    function(s) {
        return s.set('class', 0);
    }).randomColumn();
var sandT = sand.filter(ee.Filter.lte('random', 0.7)).aside(print,
    'sand training');
var sandV = sand.filter(ee.Filter.gt('random', 0.7)).aside(print,
    'sand validation');
Map.addLayer(sandT, {
    color: 'yellow'
}, 'Sand Training', false);
Map.addLayer(sandV, {
    color: 'yellow'
}, 'Sand Validation', false);

var hard = ee.FeatureCollection.randomPoints(rockyBottom, 79).map(
    function(s) {
        return s.set('class', 1);
    }).randomColumn();
var hardT = hard.filter(ee.Filter.lte('random', 0.7)).aside(print,
    'hard training');
var hardV = hard.filter(ee.Filter.gt('random', 0.7)).aside(print,
    'hard validation');
Map.addLayer(hardT, {
    color: 'red'
}, 'Rock Training', false);
Map.addLayer(hardV, {
    color: 'red'
}, 'Rock Validation', false);

var posi = pO.map(function(s) {
        return s.set('class', 2);
    })
    .randomColumn('random');
var posiT = posi.filter(ee.Filter.lte('random', 0.7)).aside(print,
    'posi training');
var posiV = posi.filter(ee.Filter.gt('random', 0.7)).aside(print,
    'posi validation');
Map.addLayer(posiT, {
    color: 'green'
}, 'Posidonia Training', false);
Map.addLayer(posiV, {
    color: 'green'
}, 'Posidonia Validation', false);

// Classification procedure.
function classify(img) {
    var mergedT = ee.FeatureCollection([sandT, hardT, posiT])
        .flatten();
    var training = img.sampleRegions(mergedT, ['class'], 3);
    var trained = ee.Classifier.libsvm({
        kernelType: 'RBF',
        gamma: 1,
        cost: 500
    }).train(training, 'class');
    var classified = img.classify(trained);

    var mergedV = ee.FeatureCollection([sandV, hardV, posiV])
        .flatten();
    var accuracyCol = classified.unmask().reduceRegions({
        collection: mergedV,
        reducer: ee.Reducer.first(),
        scale: 10
    });
    var classificationErrorMatrix = accuracyCol.errorMatrix({
        actual: 'class',
        predicted: 'first',
        order: [0, 1, 2]
    });
    var classNames = ['soft_bot', 'hard_bot', 'seagrass'];
    var accuracyOA = classificationErrorMatrix.accuracy();
    var accuraccyCons = ee.Dictionary.fromLists({
        keys: classNames,
        values: classificationErrorMatrix.consumersAccuracy()
            .toList()
            .flatten()
    });
    var accuracyProd = ee.Dictionary.fromLists({
        keys: classNames,
        values: classificationErrorMatrix.producersAccuracy()
            .toList()
            .flatten()
    });

    var classificationErrormatrixArray = classificationErrorMatrix
        .array();

    var arrayToDatatable = function(array) {
        var classesNames = ee.List(classNames);

        function toTableColumns(s) {
            return {
                id: s,
                label: s,
                type: 'number'
            };
        }
        var columns = classesNames.map(toTableColumns);

        function featureToTableRow(f) {
            return {
                c: ee.List(f).map(function(c) {
                    return {
                        v: c
                    };
                })
            };
        }
        var rows = array.toList().map(featureToTableRow);
        return ee.Dictionary({
            cols: columns,
            rows: rows
        });
    };

    var dataTable = arrayToDatatable(classificationErrormatrixArray)
        .evaluate(function(dataTable) {
            print('------------- Error matrix -------------',
                ui.Chart(dataTable, 'Table')
                .setOptions({
                    pageSize: 15
                }),
                'rows: reference, cols: mapped');
        });
    print('Overall Accuracy', accuracyOA);
    print('Users accuracy', accuraccyCons);
    print('Producers accuracy', accuracyProd);
    return classified;
}

var svmClassification = classify(divImg);
var svmVis = {
    min: 0,
    max: 2,
    palette: ['ffffbf', 'fc8d59', '91cf60']
};
Map.addLayer(svmClassification, svmVis, 'classification');

// ------------------------------------------------------------------------------
// CHECKPOINT
// ------------------------------------------------------------------------------

// Section 4, Bathymetry
// Import and split training and validation data for the bathymetry.
var depth = ee.FeatureCollection(
    'projects/gee-book/assets/A2-2/DepthDataTill09072020_v2');
depth = depth.randomColumn();
var depthT = depth.filter(ee.Filter.lte('random', 0.7));
var depthV = depth.filter(ee.Filter.gt('random', 0.7));
Map.addLayer(depthT, {
    color: 'black'
}, 'Depth Training', false);
Map.addLayer(depthV, {
    color: 'gray'
}, 'Depth Validation', false);

function vector2image(vector) {
    var rasterisedVectorData = vector
        .filter(ee.Filter.neq('Depth',
            null)) // Filter out NA depth values.
        .reduceToImage({
            properties: ['Depth'],
            reducer: ee.Reducer.mean()
        });
    return (rasterisedVectorData);
}

var depthTImage = vector2image(depthT)
    .aside(Map.addLayer, {
        color: 'white'
    }, 'Depth Training2', false);
var depthVImage = vector2image(depthV)
    .aside(Map.addLayer, {
        color: 'white'
    }, 'Depth Validation2', false);

function rfbathymetry(img) {
    var training = img.sampleRegions({
        collection: depthT,
        scale: 3
    });

    var regclass = ee.Classifier.smileRandomForest(15)
        .train(training, 'Depth');
    var bathyClass = img
        .classify(regclass.setOutputMode('REGRESSION')).rename(
            'Depth');

    var sdbEstimate = bathyClass.clip(depthV);

    // Prepare data by putting SDB estimated data and in situ data
    // in one image to compare them afterwards.
    var imageI = ee.Image.cat([sdbEstimate, depthVImage]);
    // Calculate covariance.
    var covariance = imageI.toArray().reduceRegion({
        reducer: ee.Reducer.covariance(),
        geometry: depthV,
        scale: 3,
        bestEffort: true,
        maxPixels: 1e9
    });
    var covarMatrix = ee.Array(covariance.get('array'));

    var rSqr = covarMatrix.get([0, 1]).pow(2)
        .divide(covarMatrix.get([0, 0])
            .multiply(covarMatrix.get([1, 1])));

    var deviation = depthVImage.select('mean')
        .subtract(sdbEstimate.select('Depth')).pow(2);

    var rmse = ee.Number(deviation.reduceRegion({
            reducer: ee.Reducer.mean(),
            geometry: depthV,
            scale: 3,
            bestEffort: true,
            maxPixels: 1e12
        }).get('mean'))
        .sqrt();

    // Print together, so that they appear in the same output.
    print('R²', rSqr, 'RMSE', rmse);

    return bathyClass;
}

var rfBathymetry = rfbathymetry(divImg);
var bathyVis = {
    min: -50,
    max: 0,
    palette: ['084594', '2171b5', '4292c6', '6baed6',
        '9ecae1', 'c6dbef', 'deebf7', 'f7fbff'
    ]
};
Map.addLayer(rfBathymetry, bathyVis, 'bathymetry');

// ------------------------------------------------------------------------------
// CHECKPOINT
// ------------------------------------------------------------------------------