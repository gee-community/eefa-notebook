import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.5 Heat Islands
#  Checkpoint:   A15e
#  Author:       TC Chakraborty
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load feature collection of New Haven's census tracts from user assets.
regionInt = ee.FeatureCollection(
    'projects/gee-book/assets/A1-5/TC_NewHaven')

# Get dissolved feature collection using an error margin of 50 meters.
regionInt = regionInt.union(50)

# Set map center and zoom level (Zoom level varies from 1 to 20).
Map.setCenter(-72.9, 41.3, 12)

# Add layer to map.
Map.addLayer(regionInt, {}, 'New Haven boundary')

# Load MODIS image collection from the Earth Engine data catalog.
modisLst = ee.ImageCollection('MODIS/006/MYD11A2')

# Select the band of interest (in this case: Daytime LST).
landSurfTemperature = modisLst.select('LST_Day_1km')

# Create a summer filter.
sumFilter = ee.Filter.dayOfYear(152, 243)

#Filter the date range of interest using a date filter.
lstDateInt = landSurfTemperature \
    .filterDate('2014-01-01', '2019-01-01').filter(sumFilter)

# Take pixel-wise mean of all the images in the collection.
lstMean = lstDateInt.mean()

# Multiply each pixel by scaling factor to get the LST values.
lstFinal = lstMean.multiply(0.02)

# Generate a water mask.
water = ee.Image('JRC/GSW1_0/GlobalSurfaceWater').select(
    'occurrence')
notWater = water.mask().Not()

# Clip data to region of interest, convert to degree Celsius, and mask water pixels.
lstNewHaven = lstFinal.clip(regionInt).subtract(273.15) \
    .updateMask(notWater)

# Add layer to map.
Map.addLayer(lstNewHaven, {
        'palette': ['blue', 'white', 'red'],
        'min': 25,
        'max': 38
    },
    'LST_MODIS')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Function to filter out cloudy pixels.
def cloudMask(cloudyScene):
    # Add a cloud score band to the image.
    scored = ee.Algorithms.Landsat.simpleCloudScore(cloudyScene)

    # Create an image mask from the cloud score band and specify threshold.
    mask = scored.select(['cloud']).lte(10)

    # Apply the mask to the original image and return the masked image.
    return cloudyScene.updateMask(mask)


# Load the collection, apply cloud mask, and filter to date and region of interest.
col = ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA') \
    .filterBounds(regionInt) \
    .filterDate('2014-01-01', '2019-01-01') \
    .filter(sumFilter) \
    .map(cloudMask)

print('Landsat collection', col)

# Generate median composite.
image = col.median()

# Select thermal band 10 (with brightness temperature).
thermal = image.select('B10') \
    .clip(regionInt) \
    .updateMask(notWater)

Map.addLayer(thermal, {
        'min': 295,
        'max': 310,
        'palette': ['blue', 'white', 'red']
    },
    'Landsat_BT')

# Calculate Normalized Difference Vegetation Index (NDVI)
# from Landsat surface reflectance.
ndvi = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') \
    .filterBounds(regionInt) \
    .filterDate('2014-01-01', '2019-01-01') \
    .filter(sumFilter) \
    .median() \
    .normalizedDifference(['SR_B5', 'SR_B4']).rename('NDVI') \
    .clip(regionInt) \
    .updateMask(notWater)

Map.addLayer(ndvi, {
        'min': 0,
        'max': 1,
        'palette': ['blue', 'white', 'green']
    },
    'ndvi')

# Find the minimum and maximum of NDVI.  Combine the reducers
# for efficiency (single pass over the data).
minMax = ndvi.reduceRegion({
    'reducer': ee.Reducer.min().combine({
        'reducer2': ee.Reducer.max(),
        'sharedInputs': True
    }),
    'geometry': regionInt,
    'scale': 30,
    'maxPixels': 1e9
})
print('minMax', minMax)

min = ee.Number(minMax.get('NDVI_min'))
max = ee.Number(minMax.get('NDVI_max'))

# Calculate fractional vegetation.
fv = ndvi.subtract(min).divide(max.subtract(min)).rename('FV')
Map.addLayer(fv, {
    'min': 0,
    'max': 1,
    'palette': ['blue', 'white', 'green']
}, 'fv')

# Emissivity calculations.
a = ee.Number(0.004)
b = ee.Number(0.986)
em = fv.multiply(a).add(b).rename('EMM').updateMask(notWater)

Map.addLayer(em, {
        'min': 0.98,
        'max': 0.99,
        'palette': ['blue', 'white', 'green']
    },
    'EMM')

# Calculate LST from emissivity and brightness temperature.
lstLandsat = thermal.expression(
    '(Tb/(1 + (0.001145* (Tb / 1.438))*log(Ep)))-273.15', {
        'Tb': thermal.select('B10'),
        'Ep': em.select('EMM')
    }).updateMask(notWater)

Map.addLayer(lstLandsat, {
        'min': 25,
        'max': 35,
        'palette': ['blue', 'white', 'red'],
    },
    'LST_Landsat')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Link to the module that computes the Landsat LST.
landsatLST = require(
    'projects/gee-edu/book:Part A - Applications/A1 - Human Applications/A1.5 Heat Islands/modules/Landsat_LST.js')

# Select region of interest, date range, and Landsat satellite.
geometry = regionInt.geometry()
satellite = 'L8'
dateStart = '2014-01-01'
dateEnd = '2019-01-01'
useNdvi = True

# Get Landsat collection with additional necessary variables.
landsatColl = landsatLST.collection(satellite, dateStart, dateEnd,
    geometry, useNdvi)

# Create composite, clip, filter to summer, mask, and convert to degree Celsius.
landsatComp = landsatColl \
    .select('LST') \
    .filter(sumFilter) \
    .median() \
    .clip(regionInt) \
    .updateMask(notWater) \
    .subtract(273.15)

Map.addLayer(landsatComp, {
        'min': 25,
        'max': 38,
        'palette': ['blue', 'white', 'red']
    },
    'LST_SMW')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Function to subtract the original urban cluster from the buffered cluster
# to generate rural references.
def bufferSubtract(feature):
    return ee.Feature(feature.geometry() \
        .buffer(2000) \
        .difference(feature.geometry()))


ruralRef = regionInt.map(bufferSubtract)

Map.addLayer(ruralRef, {
    'color': 'green'
}, 'Buffer_ref')

# Define sequence of buffer widths to be tested.
buffWidths = ee.List.sequence(30, 3000, 30)

# Function to generate standardized buffers (approximately comparable to area of urban cluster).
def bufferOptimize(feature):
    def buff(buffLength):
        buffedPolygon = ee.Feature(feature.geometry() \
                .buffer(ee.Number(buffLength))) \
            .set({
                'Buffer_width': ee.Number(buffLength)
            })
        area = buffedPolygon.geometry().difference(feature \
            .geometry()).area()
        diffFeature = ee.Feature(
            buffedPolygon.geometry().difference(feature \
                .geometry()))
        return diffFeature.set({
            'Buffer_diff': area.subtract(feature.geometry() \
                .area()).abs(),
            'Buffer_area': area,
            'Buffer_width': buffedPolygon.get('Buffer_width')
        })


    buffed = ee.FeatureCollection(buffWidths.map(buff))
    sortedByBuffer = buffed.sort({
        'property': 'Buffer_diff'
    })
    firstFeature = ee.Feature(sortedByBuffer.first())
    return firstFeature.set({
        'Urban_Area': feature.get('Area'),
        'Buffer_width': firstFeature.get('Buffer_width')
    })


# Map function over urban feature collection.
ruralRefStd = regionInt.map(bufferOptimize)

Map.addLayer(ruralRefStd, {
    'color': 'brown'
}, 'Buffer_ref_std')

print('ruralRefStd', ruralRefStd)

# Select the NLCD land cover data.
landCover = ee.Image('USGS/NLCD/NLCD2016').select('landcover')
urban = landCover

# Select urban pixels in image.
urbanUrban = urban.updateMask(urban.eq(23).Or(urban.eq(24)))

# Select background reference pixels in the image.
nonUrbanVals = [41, 42, 43, 51, 52, 71, 72, 73, 74, 81, 82]
nonUrbanPixels = urban.eq(ee.Image(nonUrbanVals)).reduce('max')
urbanNonUrban = urban.updateMask(nonUrbanPixels)

Map.addLayer(urbanUrban.clip(regionInt), {
    'palette': 'red'
}, 'Urban pixels')
Map.addLayer(urbanNonUrban.clip(regionInt), {
    'palette': 'blue'
}, 'Non-urban pixels')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Define function to reduce regions and summarize pixel values
# to get mean LST for different cases.
def polygonMean(feature):

    # Calculate spatial mean value of LST for each case
    # making sure the pixel values are converted to °C from Kelvin.
    reducedLstUrb = lstFinal.subtract(273.15).updateMask(notWater) \
        .reduceRegion({
            'reducer': ee.Reducer.mean(),
            'geometry': feature.geometry(),
            'scale': 30
        })
    reducedLstUrbMask = lstFinal.subtract(273.15).updateMask(
            notWater) \
        .updateMask(urbanUrban) \
        .reduceRegion({
            'reducer': ee.Reducer.mean(),
            'geometry': feature.geometry(),
            'scale': 30
        })
    reducedLstUrbPix = lstFinal.subtract(273.15).updateMask(
            notWater) \
        .updateMask(urbanUrban) \
        .reduceRegion({
            'reducer': ee.Reducer.mean(),
            'geometry': feature.geometry(),
            'scale': 500
        })
    reducedLstLandsatUrbPix = landsatComp.updateMask(notWater) \
        .updateMask(urbanUrban) \
        .reduceRegion({
            'reducer': ee.Reducer.mean(),
            'geometry': feature.geometry(),
            'scale': 30
        })
    reducedLstRurPix = lstFinal.subtract(273.15).updateMask(
            notWater) \
        .updateMask(urbanNonUrban) \
        .reduceRegion({
            'reducer': ee.Reducer.mean(),
            'geometry': feature.geometry(),
            'scale': 500
        })
    reducedLstLandsatRurPix = landsatComp.updateMask(notWater) \
        .updateMask(urbanNonUrban) \
        .reduceRegion({
            'reducer': ee.Reducer.mean(),
            'geometry': feature.geometry(),
            'scale': 30
        })

    # Return each feature with the summarized LSY values as properties.
    return feature.set({
        'MODIS_LST_urb': reducedLstUrb.get('LST_Day_1km'),
        'MODIS_LST_urb_mask': reducedLstUrbMask.get(
            'LST_Day_1km'),
        'MODIS_LST_urb_pix': reducedLstUrbPix.get(
            'LST_Day_1km'),
        'MODIS_LST_rur_pix': reducedLstRurPix.get(
            'LST_Day_1km'),
        'Landsat_LST_urb_pix': reducedLstLandsatUrbPix.get(
            'LST'),
        'Landsat_LST_rur_pix': reducedLstLandsatRurPix.get(
            'LST')
    })


# Map the function over the urban boundary to get mean urban and rural LST
# for cases without any explicit buffer-based boundaries.
reduced = regionInt.map(polygonMean)

# Define a function to reduce region and summarize pixel values
# to get mean LST for different cases.
def refMean(feature):
    # Calculate spatial mean value of LST for each case
    # making sure the pixel values are converted to °C from Kelvin.
    reducedLstRur = lstFinal.subtract(273.15).updateMask(notWater) \
        .reduceRegion({
            'reducer': ee.Reducer.mean(),
            'geometry': feature.geometry(),
            'scale': 30
        })
    reducedLstRurMask = lstFinal.subtract(273.15).updateMask(
            notWater) \
        .updateMask(urbanNonUrban) \
        .reduceRegion({
            'reducer': ee.Reducer.mean(),
            'geometry': feature.geometry(),
            'scale': 30
        })
    return feature.set({
        'MODIS_LST_rur': reducedLstRur.get('LST_Day_1km'),
        'MODIS_LST_rur_mask': reducedLstRurMask.get(
            'LST_Day_1km'),
    })


# Map the function over the constant buffer rural reference boundary one.
reducedRural = ee.FeatureCollection(ruralRef).map(refMean)

# Map the function over the standardized rural reference boundary.
reducedRuralStd = ruralRefStd.map(refMean)

print('reduced', reduced)
print('reducedRural', reducedRural)
print('reducedRuralStd', reducedRuralStd)

# Display SUHI variability within the city.
suhi = landsatComp \
    .updateMask(urbanUrban) \
    .subtract(ee.Number(ee.Feature(reduced.first()) \
        .get('Landsat_LST_rur_pix')))

Map.addLayer(suhi, {
    'palette': ['blue', 'white', 'red'],
    'min': 2,
    'max': 8
}, 'SUHI')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map