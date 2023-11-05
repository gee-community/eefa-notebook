import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A2.1 Groundwater Monitoring with GRACE
#  Checkpoint:   A21b
#  Authors:      A.J. Purdy, J.S. Famiglietti
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import Basins.
basins = ee.FeatureCollection('USGS/WBD/2017/HUC04')

# Extract the 3 HUC 04 basins for the Central Valley.
codes = ['1802', '1803', '1804']
basin = basins.filter(ee.Filter.inList('huc4', codes))

# Add the basin to the map to show the extent of our analysis.
Map.centerObject(basin, 6)
Map.addLayer(basin, {
    'color': 'green'
}, 'Central Valley Basins', True, 0.5)

landcover = ee.ImageCollection('USDA/NASS/CDL') \
    .filter(ee.Filter.date('2019-01-01', '2019-12-31')) \
    .select('cultivated')

Map.addLayer(landcover.first().clip(basin), {}, 'Cropland', True,
    0.5)

# This table was generated using the index from the CDEC website
res = ee.FeatureCollection(
    'projects/gee-book/assets/A2-1/ca_reservoirs_index')
# Filter reservoir locations by the Central Valley geometry
res_cv = res.filterBounds(basin)
Map.addLayer(res_cv, {
    'color': 'blue'
}, 'Reservoirs')

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------

GRACE = ee.ImageCollection('NASA/GRACE/MASS_GRIDS/MASCON_CRI')
# Subset GRACE for liquid water equivalent dataset
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

# Compute Trend for each pixel to map regions of most change
def addVariables(image):
    # Compute time in fractional years since the epoch.
    date = ee.Date(image.get('system:time_start'))
    years = date.difference(ee.Date('2003-01-01'), 'year')
    # Return the image with the added bands.
    return image \
        .addBands(ee.Image(years).rename('t').float()) \
        .addBands(ee.Image.constant(1))

cvTWSa = basinTWSa.filterBounds(basin).map(addVariables)
print(cvTWSa)
# List of the independent variable names
independents = ee.List(['constant', 't'])

# Name of the dependent variable.
dependent = ee.String('lwe_thickness')
# Compute a linear trend.  This will have two bands: 'residuals' and
# a 2x1 band called coefficients (columns are for dependent variables).
trend = cvTWSa.select(independents.add(dependent)) \
    .reduce(ee.Reducer.linearRegression(independents.length(), 1))

# Flatten the coefficients into a 2-band image
coefficients = trend.select('coefficients') \
    .arrayProject([0]) \
    .arrayFlatten([independents])

# Create a layer of the TWSa slope to add to the map
slope = coefficients.select('t')
# Set visualization parameters to represent positive (blue) & negative (red) trends
slopeParams = {
    'min': -3.5,
    'max': 3.5,
    'palette': ['red', 'white', 'blue']
}
Map.addLayer(slope.clip(basin), slopeParams, 'TWSa Trend', True,
    0.75)

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map