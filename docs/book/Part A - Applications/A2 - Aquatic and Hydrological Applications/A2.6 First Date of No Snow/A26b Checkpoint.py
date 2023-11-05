import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A2.6 Defining Seasonality: First Date of No Snow
#  Checkpoint:   A26b
#  Authors:      Amanda Armstrong, Morgan Tassone, Justin Braaten
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

startDoy = 1
startYear = 2000
endYear = 2019

startDate
startYear

def addDateBands(img):
    # Get image date.
    date = img.date()
    # Get calendar day-of-year.
    calDoy = date.getRelative('day', 'year')
    # Get relative day-of-year; enumerate from user-defined startDoy.
    relDoy = date.difference(startDate, 'day')
    # Get the date as milliseconds from Unix epoch.
    millis = date.millis()
    # Add all of the above date info as bands to the snow fraction image.
    dateBands = ee.Image.constant([calDoy, relDoy, millis,
            startYear
        ]) \
        .rename(['calDoy', 'relDoy', 'millis', 'year'])
    # Cast bands to correct data type before returning the image.
    return img.addBands(dateBands) \
        .cast({
            'calDoy': 'int',
            'relDoy': 'int',
            'millis': 'long',
            'year': 'int'
        }) \
        .set('millis', millis)


waterMask = ee.Image('MODIS/MOD44W/MOD44W_005_2000_02_24') \
    .select('water_mask') \
    .Not()

completeCol = ee.ImageCollection('MODIS/006/MOD10A1') \
    .select('NDSI_Snow_Cover')

# Pixels must have been 10% snow covered for at least 2 weeks in 2018.
snowCoverEphem = completeCol.filterDate('2018-01-01',
        '2019-01-01')

def func_yvu(img):
        return img.gte(10) \
    .map(func_yvu) \
    .sum() \
    .gte(14)

# Pixels must not be 10% snow covered more than 124 days in 2018.
snowCoverConst = completeCol.filterDate('2018-01-01',
        '2019-01-01')

def func_hsm(img):
        return img.gte(10) \
    .map(func_hsm) \
    .sum() \
    .lte(124)

analysisMask = waterMask.multiply(snowCoverEphem).multiply(
    snowCoverConst)

years = ee.List.sequence(startYear, endYear)


def func_anh(year):
    # Set the global startYear variable as the year being worked on so that
    # it will be accessible to the addDateBands mapped to the collection below.
    startYear = year
    # Get the first day-of-year for this year as an ee.Date object.
    firstDoy = ee.Date.fromYMD(year, 1, 1)
    # Advance from the firstDoy to the user-defined startDay; subtract 1 since
    # firstDoy is already 1. Set the result as the global startDate variable so
    # that it is accessible to the addDateBands mapped to the collection below.
    startDate = firstDoy.advance(startDoy - 1, 'day')
    # Get endDate for this year by advancing 1 year from startDate.
    # Need to advance an extra day because end date of filterDate() function
    # is exclusive.
    endDate = startDate.advance(1, 'year').advance(1,
        'day')
    # Filter the complete collection by the start and end dates just defined.
    yearCol = completeCol.filterDate(startDate, endDate)
    # Construct an image where pixels represent the first day within the date
    # range that the lowest snow fraction is observed.
    noSnowImg = yearCol \
        .map(addDateBands)
        # Sort the images by ascending time to identify the first day without
        # snow. Alternatively, you can use .sort('millis', False) to \
        .sort('millis')
        # Make a mosaic composed of pixels from images that represent the
        # observation with the minimum percent snow cover (defined by Çthe
        # NDSI_Snow_Cover band); include all associated bands for the selected \
        .reduce(ee.Reducer.min(5)) \
        .rename(['snowCover', 'calDoy', 'relDoy', 'millis',
            'year'
        ]) \
        .updateMask(analysisMask) \
        .set('year', year)

    # Mask by minimum snow fraction - only include pixels that reach 0
    # percent cover. Return the resulting image.
    return noSnowImg.updateMask(noSnowImg.select('snowCover') \
        .eq(0))

annualList = years.map(func_anh)














































annualCol = ee.ImageCollection.fromImages(annualList)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Define a year to visualize.
thisYear = 2018

# Define visualization arguments.
visArgs = {
    'bands': ['calDoy'],
    'min': 150,
    'max': 200,
    'palette': [
        '0D0887', '5B02A3', '9A179B', 'CB4678', 'EB7852',
        'FBB32F', 'F0F921'
    ]
}

# Subset the year of interest.
firstDayNoSnowYear = annualCol.filter(ee.Filter.eq('year',
    thisYear)).first()

# Display it on the map.
Map.setCenter(-95.78, 59.451, 5)
Map.addLayer(firstDayNoSnowYear, visArgs,
    'First day of no snow, 2018')

# Define the years to difference.
firstYear = 2005
secondYear = 2015

# Calculate difference image.
firstImg = annualCol.filter(ee.Filter.eq('year', firstYear)) \
    .first().select('calDoy')
secondImg = annualCol.filter(ee.Filter.eq('year', secondYear)) \
    .first().select('calDoy')
dif = secondImg.subtract(firstImg)

# Define visualization arguments.
visArgs = {
    'min': -15,
    'max': 15,
    'palette': ['b2182b', 'ef8a62', 'fddbc7', 'f7f7f7', 'd1e5f0',
        '67a9cf', '2166ac'
    ]
}

# Display it on the map.
Map.setCenter(95.427, 29.552, 8)
Map.addLayer(dif, visArgs, '2015-2005 first day no snow dif')

# Calculate slope image.
slope = annualCol.sort('year').select(['year', 'calDoy']) \
    .reduce(ee.Reducer.linearFit()).select('scale')

# Define visualization arguments.
visArgs = {
    'min': -1,
    'max': 1,
    'palette': ['b2182b', 'ef8a62', 'fddbc7', 'f7f7f7',
        'd1e5f0', '67a9cf', '2166ac'
    ]
}

# Display it on the map.
Map.setCenter(11.25, 59.88, 6)
Map.addLayer(slope, visArgs, '2000-2019 first day no snow slope')

# Define an AOI.
aoi = ee.Geometry.Point(-94.242, 65.79).buffer(1e4)
Map.addLayer(aoi, None, 'Area of interest')

# Calculate annual mean DOY of AOI.

def func_xob(img):
    summary = img.reduceRegion({
        'reducer': ee.Reducer.mean(),
        'geometry': aoi,
        'scale': 1e3,
        'bestEffort': True,
        'maxPixels': 1e14,
        'tileScale': 4,
    })
    return ee.Feature(None, summary).set('year', img.get(
        'year'))

annualAoiMean = annualCol.select('calDoy').map(func_xob)













# Print chart to console.
chart = ui.Chart.feature.byFeature(annualAoiMean, 'year',
        'calDoy') \
    .setOptions({
        'title': 'Regional mean first day of year with no snow cover',
        'legend': {
            'position': 'none'
        },
        'hAxis': {
            'title': 'Year',
            format: '####'
        },
        'vAxis': {
            'title': 'Day-of-year'
        }
    })
print(chart)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map