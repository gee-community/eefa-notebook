import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.6 Health Applications
#  Checkpoint:   A16d
#  Author:       Dawn Nekorchuk
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Section 1: Data Import
woredas = ee.FeatureCollection(
    'projects/gee-book/assets/A1-6/amhara_woreda_20170207')
# Create region outer boundary to filter products on.
amhara = woredas.geometry().bounds()
gpm = ee.ImageCollection('NASA/GPM_L3/IMERG_V06')
LSTTerra8 = ee.ImageCollection('MODIS/061/MOD11A2') \
    .filterDate('2001-06-26', Date.now())
brdfReflect = ee.ImageCollection('MODIS/006/MCD43A4')
brdfQa = ee.ImageCollection('MODIS/006/MCD43A2')

# Visualize woredas with black borders and no fill.
# Create an empty image into which to paint the features, cast to byte.
empty = ee.Image().byte()
# Paint all the polygon edges with the same number and width.
outline = empty.paint({
    'featureCollection': woredas,
    'color': 1,
    'width': 1
})
# Add woreda boundaries to the map.
Map.setCenter(38, 11.5, 7)
Map.addLayer(outline, {
    'palette': '000000'
}, 'Woredas')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Section 2: Handling of dates

# 2.1 Requested start and end dates.
reqStartDate = ee.Date('2021-10-01')
reqEndDate = ee.Date('2021-11-30')

# 2.2 LST Dates
# LST MODIS is every 8 days, and a user-requested date will likely not match.
# We want to get the latest previous image date,
#  i.e. the date the closest, but prior to, the requested date.
# We will filter later.
# Get date of first image.
LSTEarliestDate = LSTTerra8.first().date()
# Filter collection to dates from beginning to requested start date.
priorLstImgCol = LSTTerra8.filterDate(LSTEarliestDate,
    reqStartDate)
# Get the latest (max) date of this collection of earlier images.
LSTPrevMax = priorLstImgCol.reduceColumns({
    'reducer': ee.Reducer.max(),
    'selectors': ['system:time_start']
})
LSTStartDate = ee.Date(LSTPrevMax.get('max'))
print('LSTStartDate', LSTStartDate)

# 2.3 Last available data dates
# Different variables have different data lags.
# Data may not be available in user range.
# To prevent errors from stopping script,
#  grab last available (if relevant) & filter at end.

# 2.3.1 Precipitation
# Calculate date of most recent measurement for gpm (of all time).
gpmAllMax = gpm.reduceColumns(ee.Reducer.max(), [
    'system:time_start'
])
gpmAllEndDateTime = ee.Date(gpmAllMax.get('max'))
# GPM every 30 minutes, so get just date part.
gpmAllEndDate = ee.Date.fromYMD({
    'year': gpmAllEndDateTime.get('year'),
    'month': gpmAllEndDateTime.get('month'),
    'day': gpmAllEndDateTime.get('day')
})

# If data ends before requested start, take last data date,
# otherwise use requested date.
precipStartDate = ee.Date(gpmAllEndDate.millis() \
    .min(reqStartDate.millis()))
print('precipStartDate', precipStartDate)

# 2.3.2 BRDF
# Calculate date of most recent measurement for brdf (of all time).
brdfAllMax = brdfReflect.reduceColumns({
    'reducer': ee.Reducer.max(),
    'selectors': ['system:time_start']
})
brdfAllEndDate = ee.Date(brdfAllMax.get('max'))
# If data ends before requested start, take last data date,
# otherwise use the requested date.
brdfStartDate = ee.Date(brdfAllEndDate.millis() \
    .min(reqStartDate.millis()))
print('brdfStartDate', brdfStartDate)
print('brdfEndDate', brdfAllEndDate)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Section 3: Precipitation

# Section 3.1: Precipitation filtering and dates

# Filter gpm by date, using modified start if necessary.
gpmFiltered = gpm \
    .filterDate(precipStartDate, reqEndDate.advance(1, 'day')) \
    .filterBounds(amhara) \
    .select('precipitationCal')

# Calculate date of most recent measurement for gpm
# (in the modified requested window).
gpmMax = gpmFiltered.reduceColumns({
    'reducer': ee.Reducer.max(),
    'selectors': ['system:time_start']
})
gpmEndDate = ee.Date(gpmMax.get('max'))
precipEndDate = gpmEndDate
print('precipEndDate ', precipEndDate)

# Create a list of dates for the precipitation time series.
precipDays = precipEndDate.difference(precipStartDate, 'day')
precipDatesPrep = ee.List.sequence(0, precipDays, 1)

def makePrecipDates(n):
    return precipStartDate.advance(n, 'day')

precipDates = precipDatesPrep.map(makePrecipDates)

# Section 3.2: Calculate daily precipitation

# Function to calculate daily precipitation:
def calcDailyPrecip(curdate):
    curdate = ee.Date(curdate)
    curyear = curdate.get('year')
    curdoy = curdate.getRelative('day', 'year').add(1)
    totprec = gpmFiltered \
        .filterDate(curdate, curdate.advance(1, 'day')) \
        .select('precipitationCal') \
        .sum() \
        .multiply(0.5) \
        .rename('totprec')

    return totprec \
        .set('doy', curdoy) \
        .set('year', curyear) \
        .set('system:time_start', curdate)

# Map function over list of dates.
dailyPrecipExtended =
    ee.ImageCollection.fromImages(precipDates.map(calcDailyPrecip))

# Filter back to the original user requested start date.
dailyPrecip = dailyPrecipExtended \
    .filterDate(reqStartDate, precipEndDate.advance(1, 'day'))

# Section 3.3: Summarize daily precipitation by woreda

# Filter precip data for zonal summaries.
precipSummary = dailyPrecip \
    .filterDate(reqStartDate, reqEndDate.advance(1, 'day'))

# Function to calculate zonal statistics for precipitation by woreda.
def sumZonalPrecip(image):
    # To get the doy and year,
    # convert the metadata to grids and then summarize.
    image2 = image.addBands([
        image.metadata('doy').int(),
        image.metadata('year').int()
    ])
    # Reduce by regions to get zonal means for each county.
    output = image2.select(['year', 'doy', 'totprec']) \
        .reduceRegions({
            'collection': woredas,
            'reducer': ee.Reducer.mean(),
            'scale': 1000
        })
    return output

# Map the zonal statistics function over the filtered precip data.
precipWoreda = precipSummary.map(sumZonalPrecip)
# Flatten the results for export.
precipFlat = precipWoreda.flatten()

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Section 4: Land surface temperature

# Section 4.1: Calculate LST variables

# Filter Terra LST by altered LST start date.
# Rarely, but at the end of the year if the last image is late in the year
#  with only a few days in its period, it will sometimes not grab
#  the next image. Add extra padding to reqEndDate and
#  it will be trimmed at the end.
LSTFiltered = LSTTerra8 \
    .filterDate(LSTStartDate, reqEndDate.advance(8, 'day')) \
    .filterBounds(amhara) \
    .select('LST_Day_1km', 'QC_Day', 'LST_Night_1km', 'QC_Night')

# Filter Terra LST by QA information.
def filterLstQa(image):
    qaday = image.select(['QC_Day'])
    qanight = image.select(['QC_Night'])
    dayshift = qaday.rightShift(6)
    nightshift = qanight.rightShift(6)
    daymask = dayshift.lte(2)
    nightmask = nightshift.lte(2)
    outimage = ee.Image(image.select(['LST_Day_1km',
        'LST_Night_1km'
    ]))
    outmask = ee.Image([daymask, nightmask])
    return outimage.updateMask(outmask)

LSTFilteredQa = LSTFiltered.map(filterLstQa)

# Rescale temperature data and convert to degrees Celsius (C).
def rescaleLst(image):
    LST_day = image.select('LST_Day_1km') \
        .multiply(0.02) \
        .subtract(273.15) \
        .rename('LST_day')
    LST_night = image.select('LST_Night_1km') \
        .multiply(0.02) \
        .subtract(273.15) \
        .rename('LST_night')
    LST_mean = image.expression(
        '(day + night) / 2', {
            'day': LST_day.select('LST_day'),
            'night': LST_night.select('LST_night')
        }
    ).rename('LST_mean')
    return image.addBands(LST_day) \
        .addBands(LST_night) \
        .addBands(LST_mean)

LSTVars = LSTFilteredQa.map(rescaleLst)

# Section 4.2: Calculate daily LST

# Create list of dates for time series.
LSTRange = LSTVars.reduceColumns({
    'reducer': ee.Reducer.max(),
    'selectors': ['system:time_start']
})
LSTEndDate = ee.Date(LSTRange.get('max')).advance(7, 'day')
LSTDays = LSTEndDate.difference(LSTStartDate, 'day')
LSTDatesPrep = ee.List.sequence(0, LSTDays, 1)

def makeLstDates(n):
    return LSTStartDate.advance(n, 'day')

LSTDates = LSTDatesPrep.map(makeLstDates)

# Function to calculate daily LST by assigning the 8-day composite summary
# to each day in the composite period:
def calcDailyLst(curdate):
    curyear = ee.Date(curdate).get('year')
    curdoy = ee.Date(curdate).getRelative('day', 'year').add(1)
    moddoy = curdoy.divide(8).ceil().subtract(1).multiply(8).add(
        1)
    basedate = ee.Date.fromYMD(curyear, 1, 1)
    moddate = basedate.advance(moddoy.subtract(1), 'day')
    LST_day = LSTVars \
        .select('LST_day') \
        .filterDate(moddate, moddate.advance(1, 'day')) \
        .first() \
        .rename('LST_day')
    LST_night = LSTVars \
        .select('LST_night') \
        .filterDate(moddate, moddate.advance(1, 'day')) \
        .first() \
        .rename('LST_night')
    LST_mean = LSTVars \
        .select('LST_mean') \
        .filterDate(moddate, moddate.advance(1, 'day')) \
        .first() \
        .rename('LST_mean')
    return LST_day \
        .addBands(LST_night) \
        .addBands(LST_mean) \
        .set('doy', curdoy) \
        .set('year', curyear) \
        .set('system:time_start', curdate)

# Map the function over the image collection
dailyLstExtended =
    ee.ImageCollection.fromImages(LSTDates.map(calcDailyLst))

# Filter back to original user requested start date
dailyLst = dailyLstExtended \
    .filterDate(reqStartDate, LSTEndDate.advance(1, 'day'))

# Section 4.3: Summarize daily LST by woreda

# Filter LST data for zonal summaries.
LSTSummary = dailyLst \
    .filterDate(reqStartDate, reqEndDate.advance(1, 'day'))
# Function to calculate zonal statistics for LST by woreda:
def sumZonalLst(image):
    # To get the doy and year, we convert the metadata to grids
    #  and then summarize.
    image2 = image.addBands([
        image.metadata('doy').int(),
        image.metadata('year').int()
    ])
    # Reduce by regions to get zonal means for each county.
    output = image2 \
        .select(['doy', 'year', 'LST_day', 'LST_night', 'LST_mean']) \
        .reduceRegions({
            'collection': woredas,
            'reducer': ee.Reducer.mean(),
            'scale': 1000
        })
    return output

# Map the zonal statistics function over the filtered LST data.
LSTWoreda = LSTSummary.map(sumZonalLst)
# Flatten the results for export.
LSTFlat = LSTWoreda.flatten()

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
