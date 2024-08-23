import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A2.5 Water Balance and Drought
#  Checkpoint:   A25d
#  Authors:      Ate Poortinga, Quyen Nguyen, Nyein Soe Thwal, Andréa Puzzi Nicolau
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import the Lower Mekong boundary.
mekongBasin = ee.FeatureCollection(
    'projects/gee-book/assets/A2-5/lowerMekongBasin')

# Center the map.
Map.centerObject(mekongBasin, 5)

# Add the Lower Mekong Basin boundary to the map.
Map.addLayer(mekongBasin, {}, 'Lower Mekong basin')

# Set start and end years.
startYear = 2010
endYear = 2020

# Create two date objects for start and end years.
startDate = ee.Date.fromYMD(startYear, 1, 1)
endDate = ee.Date.fromYMD(endYear + 1, 1, 1)

# Make a list with years.
years = ee.List.sequence(startYear, endYear)

# Make a list with months.
months = ee.List.sequence(1, 12)

# Import the CHIRPS dataset.
CHIRPS = ee.ImageCollection('UCSB-CHG/CHIRPS/PENTAD')

# Filter for relevant time period.
CHIRPS = CHIRPS.filterDate(startDate, endDate)

# Import the MOD16 dataset.
mod16 = ee.ImageCollection('MODIS/006/MOD16A2').select('ET')

# Filter for relevant time period.
mod16 = mod16.filterDate(startDate, endDate)

# Import and filter the MOD13 dataset.
mod13 = ee.ImageCollection('MODIS/006/MOD13A1')
mod13 = mod13.filterDate(startDate, endDate)

# Select the EVI.
EVI = mod13.select('EVI')

# Import and filter the MODIS Terra surface reflectance dataset.
mod09 = ee.ImageCollection('MODIS/006/MOD09A1')
mod09 = mod09.filterDate(startDate, endDate)

# We use a function to remove clouds and cloud shadows.
# We map over the mod09 image collection and select the StateQA band.
# We mask pixels and return the image with clouds and cloud shadows masked.

def func_rzy(image):
    quality = image.select('StateQA')
    mask = image.And(quality.bitwiseAnd(1).eq(
            0)) # No clouds. \
        .And(quality.bitwiseAnd(2).eq(0));

    return image.updateMask(mask)

mod09 = mod09.map(func_rzy)









# We use a function to calculate the Moisture Stress Index.
# We map over the mod09 image collection and select the NIR and SWIR bands
# We set the timestamp and return the MSI.

def func_fjo(image):
    nirband = image.select('sur_refl_b02')
    swirband = image.select('sur_refl_b06')

    msi = swirband.divide(nirband).rename('MSI') \
        .set('system:time_start', image.get(
            'system:time_start'))
    return msi

MSI = mod09.map(func_fjo)










# We apply a nested loop where we first iterate over
# the relevant years and then iterate over the relevant
# months. The function returns an image with bands for
# water balance (wb), rainfall (P), evapotranspiration (ET),
# EVI and MSI for each month. A flatten is applied to
# convert an collection of collections
# into a single collection.
ic = ee.ImageCollection.fromImages(

def func_gjw(y):
        return months.map(function(m) {
            # Calculate rainfall.
            P = CHIRPS.filter(ee.Filter \
                    .calendarRange(y, y, 'year')) \
                .filter(ee.Filter.calendarRange(m, m,
                    'month')) \
                .sum()

            # Calculate evapotranspiration.
            ET = mod16.filter(ee.Filter \
                    .calendarRange(y, y, 'year')) \
                .filter(ee.Filter.calendarRange(m, m,
                    'month')) \
                .sum() \
                .multiply(0.1)

            # Calculate EVI.
            evi = EVI.filter(ee.Filter \
                    .calendarRange(y, y, 'year')) \
                .filter(ee.Filter.calendarRange(m, m,
                    'month')) \
                .mean() \
                .multiply(0.0001)

            # Calculate MSI.
            msi = MSI.filter(ee.Filter \
                    .calendarRange(y, y, 'year')) \
                .filter(ee.Filter.calendarRange(m, m,
                    'month')) \
                .mean()

            # Calculate monthly water balance.
            wb = P.subtract(ET).rename('wb')

            # Return an image with all images as bands.
            return ee.Image.cat([wb, P, ET, evi, msi]) \
                .set('year', y) \
                .set('month', m) \
                .set('system:time_start', ee.Date \
                    .fromYMD(y, m, 1))

        })

    years.map(func_gjw
).flatten()










































).flatten()
)

# Add the mean monthly EVI and MSI to the map.
eviVis = {
    'min': 0,
    'max': 0.7,
    'palette': 'red, orange, yellow, green, darkgreen'
}

Map.addLayer(ic.select('EVI').mean().clip(mekongBasin),
    eviVis,
    'EVI')

msiVis = {
    'min': 0.25,
    'max': 1,
    'palette': 'darkblue, blue, yellow, orange, red'
}

Map.addLayer(ic.select('MSI').mean().clip(mekongBasin),
    msiVis,
    'MSI')

# Define the water balance chart and print it to the console.
chartWB =
    ui.Chart.image.series({
        'imageCollection': ic.select(['wb', 'precipitation', 'ET']),
        'region': mekongBasin,
        'reducer': ee.Reducer.mean(),
        'scale': 5000,
        'xProperty': 'system:time_start'
    }) \
    .setSeriesNames(['wb', 'P', 'ET']) \
    .setOptions({
        'title': 'water balance',
        'hAxis': {
            'title': 'Date',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'vAxis': {
            'title': 'Water (mm)',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'lineWidth': 1,
        'colors': ['green', 'blue', 'red'],
        'curveType': 'function'
    })

# Print the water balance chart.
print(chartWB)

# Define the indices chart and print it to the console.
chartIndices =
    ui.Chart.image.series({
        'imageCollection': ic.select(['EVI', 'MSI']),
        'region': mekongBasin,
        'reducer': ee.Reducer.mean(),
        'scale': 5000,
        'xProperty': 'system:time_start'
    }) \
    .setSeriesNames(['EVI', 'MSI']) \
    .setOptions({
        'title': 'Monthly indices',
        'hAxis': {
            'title': 'Date',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'vAxis': {
            'title': 'Index',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'lineWidth': 1,
        'colors': ['darkgreen', 'brown'],
        'curveType': 'function'
    })

# Print the indices chart.
print(chartIndices)

# -----------------------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------------------
Map
