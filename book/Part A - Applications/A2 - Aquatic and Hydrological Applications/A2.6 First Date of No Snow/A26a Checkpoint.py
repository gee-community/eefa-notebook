import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A2.6 Defining Seasonality: First Date of No Snow
#  Checkpoint:   A26a
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

def func_teo(img):
        return img.gte(10) \
    .map(func_teo) \
    .sum() \
    .gte(14)

# Pixels must not be 10% snow covered more than 124 days in 2018.
snowCoverConst = completeCol.filterDate('2018-01-01',
        '2019-01-01')

def func_jlk(img):
        return img.gte(10) \
    .map(func_jlk) \
    .sum() \
    .lte(124)

analysisMask = waterMask.multiply(snowCoverEphem).multiply(
    snowCoverConst)

years = ee.List.sequence(startYear, endYear)


def func_kis(year):
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
        # observation with the minimum percent snow cover (defined by the
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

annualList = years.map(func_kis)














































annualCol = ee.ImageCollection.fromImages(annualList)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
