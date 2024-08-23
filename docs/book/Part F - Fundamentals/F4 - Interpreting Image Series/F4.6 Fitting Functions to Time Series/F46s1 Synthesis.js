//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  Chapter:      F4.6 Fitting Functions to Time Series
//  Checkpoint:   F46s1
//  Authors:      Andréa Puzzi Nicolau, Karen Dyson, Biplov Bhandari, David Saah,
//                Nicholas Clinton
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

// Satellite basemap.
Map.setOptions('SATELLITE');

// Define roi, a point over the Brazilian Amazon.
var roi = ee.Geometry.Point([-59.985146, -2.871413]);

// Add the point to the map.
Map.addLayer(roi, {
    color: 'red'
}, 'roi');
Map.centerObject(roi, 16);

// The dependent variable we are modeling.
var dependent = 'NDVI';

// The number of cycles per year to model.
var harmonics = 1;

// Make a list of harmonic frequencies to model.
// These also serve as band name suffixes.
var harmonicFrequencies = ee.List.sequence(1, harmonics);

// Function to get a sequence of band names for harmonic terms.
var getNames = function(base, list) {
    return ee.List(list).map(function(i) {
        return ee.String(base).cat(ee.Number(i).int());
    });
};

// Construct lists of names for the harmonic terms.
var cosNames = getNames('cos_', harmonicFrequencies);
var sinNames = getNames('sin_', harmonicFrequencies);

// Independent variables.
var independents = ee.List(['constant', 't'])
    .cat(cosNames).cat(sinNames);

// Define function to mask clouds, scale, and add variables
// (NDVI, time and a constant) to Landsat 8 imagery.
function maskScaleAndAddVariable(image) {
    // Bit 0 - Fill
    // Bit 1 - Dilated Cloud
    // Bit 2 - Cirrus
    // Bit 3 - Cloud
    // Bit 4 - Cloud Shadow
    var qaMask = image.select('QA_PIXEL').bitwiseAnd(parseInt('11111',
        2)).eq(0);
    var saturationMask = image.select('QA_RADSAT').eq(0);

    // Apply the scaling factors to the appropriate bands.
    var opticalBands = image.select('SR_B.').multiply(0.0000275).add(-
        0.2);
    var thermalBands = image.select('ST_B.*').multiply(0.00341802)
        .add(149.0);

    // Replace the original bands with the scaled ones and apply the masks.
    var img = image.addBands(opticalBands, null, true)
        .addBands(thermalBands, null, true)
        .updateMask(qaMask)
        .updateMask(saturationMask);
    var imgScaled = image.addBands(img, null, true);

    // Now we start to add variables of interest.
    // Compute time in fractional years since the epoch.
    var date = ee.Date(image.get('system:time_start'));
    var years = date.difference(ee.Date('1970-01-01'), 'year');
    var timeRadians = ee.Image(years.multiply(2 * Math.PI));
    // Return the image with the added bands.
    return imgScaled
        // Add an NDVI band.
        .addBands(imgScaled.normalizedDifference(['SR_B5', 'SR_B4'])
            .rename('NDVI'))
        // Add a time band.
        .addBands(timeRadians.rename('t'))
        .float()
        // Add a constant band.
        .addBands(ee.Image.constant(1));
}

// Function to compute the specified number of harmonics
// and add them as bands.  Assumes the time band is present.
var addHarmonics = function(freqs) {
    return function(image) {
        // Make an image of frequencies.
        var frequencies = ee.Image.constant(freqs);
        // This band should represent time in radians.
        var time = ee.Image(image).select('t');
        // Get the cosine terms.
        var cosines = time.multiply(frequencies).cos()
            .rename(cosNames);
        // Get the sin terms.
        var sines = time.multiply(frequencies).sin()
            .rename(sinNames);
        return image.addBands(cosines).addBands(sines);
    };
};

// Import the USGS Landsat 8 Level 2, Collection 2, Tier 1 image collection),
// and map functions.
var harmonicLandsat = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
    .filterBounds(roi)
    .map(maskScaleAndAddVariable)
    .map(addHarmonics(harmonicFrequencies));

//  -----------------------------------------------------------------------
//  CHECKPOINT
//  -----------------------------------------------------------------------
