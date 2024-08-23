import ee
import geemap

Map = geemap.Map()

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
res_table = ee.FeatureCollection("projects/gee-book/assets/A2-1/SW/reservoir_anoms_km3"),
    sm2003 = ee.Image("projects/gee-book/assets/A2-1/SM/sm2003"),
    sm2004 = ee.Image("projects/gee-book/assets/A2-1/SM/sm2004"),
    sm2005 = ee.Image("projects/gee-book/assets/A2-1/SM/sm2005"),
    sm2006 = ee.Image("projects/gee-book/assets/A2-1/SM/sm2006"),
    sm2007 = ee.Image("projects/gee-book/assets/A2-1/SM/sm2007"),
    sm2008 = ee.Image("projects/gee-book/assets/A2-1/SM/sm2008"),
    sm2009 = ee.Image("projects/gee-book/assets/A2-1/SM/sm2009"),
    sm2010 = ee.Image("projects/gee-book/assets/A2-1/SM/sm2010"),
    sm2011 = ee.Image("projects/gee-book/assets/A2-1/SM/sm2011"),
    sm2012 = ee.Image("projects/gee-book/assets/A2-1/SM/sm2012"),
    sm2013 = ee.Image("projects/gee-book/assets/A2-1/SM/sm2013"),
    sm2014 = ee.Image("projects/gee-book/assets/A2-1/SM/sm2014"),
    sm2015 = ee.Image("projects/gee-book/assets/A2-1/SM/sm2015"),
    sm2016 = ee.Image("projects/gee-book/assets/A2-1/SM/sm2016"),
    swe2003 = ee.Image("projects/gee-book/assets/A2-1/SWE/swe2003"),
    swe2004 = ee.Image("projects/gee-book/assets/A2-1/SWE/swe2004"),
    swe2005 = ee.Image("projects/gee-book/assets/A2-1/SWE/swe2005"),
    swe2006 = ee.Image("projects/gee-book/assets/A2-1/SWE/swe2006"),
    swe2007 = ee.Image("projects/gee-book/assets/A2-1/SWE/swe2007"),
    swe2008 = ee.Image("projects/gee-book/assets/A2-1/SWE/swe2008"),
    swe2009 = ee.Image("projects/gee-book/assets/A2-1/SWE/swe2009"),
    swe2010 = ee.Image("projects/gee-book/assets/A2-1/SWE/swe2010"),
    swe2011 = ee.Image("projects/gee-book/assets/A2-1/SWE/swe2011"),
    swe2012 = ee.Image("projects/gee-book/assets/A2-1/SWE/swe2012"),
    swe2013 = ee.Image("projects/gee-book/assets/A2-1/SWE/swe2013"),
    swe2014 = ee.Image("projects/gee-book/assets/A2-1/SWE/swe2014"),
    swe2015 = ee.Image("projects/gee-book/assets/A2-1/SWE/swe2015"),
    swe2016 = ee.Image("projects/gee-book/assets/A2-1/SWE/swe2016")
#**** End of imports. If edited, may not auto-convert in the playground. ****#
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A2.1 Groundwater Monitoring with GRACE
#  Checkpoint:   A21d
#  Authors:      A.J. Purdy, J.S. Famiglietti
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import Basins
basins = ee.FeatureCollection('USGS/WBD/2017/HUC04')

# Extract the 3 HUC 04 basins for the Central Valley.
codes = ['1802', '1803', '1804']
basin = basins.filter(ee.Filter.inList('huc4', codes))

# Add the basin to the map to show the extent of our analysis.
Map.centerObject(basin, 6)
Map.addLayer(basin, {
    'color': 'green'
}, 'Central Valley Basins', True, 0.5)

# This table was generated using the index from the CDEC website
res = ee.FeatureCollection(
    'projects/gee-book/assets/A2-1/ca_reservoirs_index')
# Filter reservoir locations by the Central Valley geometry
res_cv = res.filterBounds(basin)
Map.addLayer(res_cv, {
    'color': 'blue'
}, 'Reservoirs')

# Import GRACE groundwater.
GRACE = ee.ImageCollection('NASA/GRACE/MASS_GRIDS/MASCON_CRI')
# Get Liquid Water Equivalent thickness.
basinTWSa = GRACE.select('lwe_thickness')

# Make plot of TWSa for Basin Boundary
TWSaChart = ui.Chart.image.series({
        'imageCollection': basinTWSa.filter(ee.Filter.date(
            '2003-01-01', '2016-12-31')),
        'region': basin,
        'reducer': ee.Reducer.mean(),
    }) \
    .setOptions({
        'title': 'TWSa',
        'hAxis': {
            format: 'MM-yyyy'
        },
        'vAxis': {
            'title': 'TWSa (cm)'
        },
        'lineWidth': 1,
    })
print(TWSaChart)

# Set start and end years to annualize the data.
yrStart = 2003
yrEnd = 2016
years = ee.List.sequence(yrStart, yrEnd)

def func_wng(y):
    date = ee.Date.fromYMD(y, 1, 1)
    return basinTWSa.filter(ee.Filter.calendarRange(y, y,
            'year')) \
        .mean() \
        .set('system:time_start', date) \
        .rename('TWSa')

GRACE_yr = ee.ImageCollection.fromImages(years.map(func_wng
).flatten())






).flatten())

# Make plot of annualized TWSa for Basin Boundary.
TWSaChart = ui.Chart.image.series({
        'imageCollection': GRACE_yr.filter(ee.Filter.date(
            '2003-01-01', '2016-12-31')),
        'region': basin,
        'reducer': ee.Reducer.mean(),
        'scale': 25000
    }).setChartType('ScatterChart') \
    .setOptions({
        'title': 'Annualized Total Water Storage anomalies',
        'trendlines': {
            '0': {
                'color': 'CC0000'
            }
        },
        'hAxis': {
            format: 'MM-yyyy'
        },
        'vAxis': {
            'title': 'TWSa (cm)'
        },
        'lineWidth': 2,
        'pointSize': 2
    })
print(TWSaChart)

# Compute Trend for each pixel to map regions of most change.

def addVariables(image):
    # Compute time in fractional years.
    date = ee.Date(image.get('system:time_start'))
    years = date.difference(ee.Date('2003-01-01'), 'year')
    # Return the image with the added bands.
    return image \
        .addBands(ee.Image(years).rename('t').float()) \
        .addBands(ee.Image.constant(1))


cvTWSa = GRACE_yr.filterBounds(basin).map(addVariables)
print(cvTWSa)

# List of the independent variable names
independents = ee.List(['constant', 't'])

# Name of the dependent variable.
dependent = ee.String('TWSa')

# Compute a linear trend.  This will have two bands: 'residuals' and
# a 2x1 band called coefficients (columns are for dependent variables).
trend = cvTWSa.select(independents.add(dependent)) \
    .reduce(ee.Reducer.linearRegression(independents.length(), 1))

# Flatten the coefficients into a 2-band image.
coefficients = trend.select('coefficients') \
    .arrayProject([0]) \
    .arrayFlatten([independents])

# Create a layer of the TWSa slope to add to the map.
slope = coefficients.select('t')
# Set visualization parameters to represent positive (blue)
# & negative (red) trends.
slopeParams = {
    'min': -3.5,
    'max': 3.5,
    'palette': ['red', 'white', 'blue']
}
Map.addLayer(slope.clip(basin), slopeParams, 'TWSa Annualized Trend', True,
0.75)

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------

gldas_sm_list = ee.List([sm2003, sm2004, sm2005, sm2006, sm2007,
    sm2008, sm2009, sm2010, sm2011, sm2012, sm2013, sm2014,
    sm2015, sm2016
])
sm_ic = ee.ImageCollection.fromImages(gldas_sm_list)

kgm2_to_cm = 0.10

def func_vva(img):
    date = ee.Date.fromYMD(img.get('year'), 1, 1)
    return img.select('RootMoist_inst').multiply(kgm2_to_cm) \
        .rename('SMa').set('system:time_start', date)

sm_ic_ts = sm_ic.map(func_vva)






# Make plot of SMa for Basin Boundary
SMaChart = ui.Chart.image.series({
        'imageCollection': sm_ic_ts.filter(ee.Filter.date(
            '2003-01-01', '2016-12-31')),
        'region': basin,
        'reducer': ee.Reducer.mean(),
        'scale': 25000
    }) \
    .setChartType('ScatterChart') \
    .setOptions({
        'title': 'Soil Moisture anomalies',
        'trendlines': {
            '0': {
                'color': 'CC0000'
            }
        },
        'hAxis': {
            format: 'MM-yyyy'
        },
        'vAxis': {
            'title': 'SMa (cm)'
        },
        'lineWidth': 2,
        'pointSize': 2
    })
print(SMaChart)

gldas_swe_list = ee.List([swe2003, swe2004, swe2005, swe2006,
    swe2007, swe2008, swe2009, swe2010, swe2011, swe2012,
    swe2013, swe2014, swe2015, swe2016
])
swe_ic = ee.ImageCollection.fromImages(gldas_swe_list)


def func_jhw(img):
    date = ee.Date.fromYMD(img.get('year'), 1, 1)
    return img.select('SWE_inst').multiply(kgm2_to_cm).rename(
        'SWEa').set('system:time_start', date)

swe_ic_ts = swe_ic.map(func_jhw)






# Make plot of SWEa for Basin Boundary
SWEaChart = ui.Chart.image.series({
        'imageCollection': swe_ic_ts.filter(ee.Filter.date(
            '2003-01-01', '2016-12-31')),
        'region': basin,
        'reducer': ee.Reducer.mean(),
        'scale': 25000
    }) \
    .setChartType('ScatterChart') \
    .setOptions({
        'title': 'Snow Water Equivalent anomalies',
        'trendlines': {
            '0': {
                'color': 'CC0000'
            }
        },
        'hAxis': {
            format: 'MM-yyyy'
        },
        'vAxis': {
            'title': 'SWEa (cm)'
        },
        'lineWidth': 2,
        'pointSize': 2
    })
print(SWEaChart)

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map
