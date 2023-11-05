import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A3.8 Detecting Land Cover Change in Rangelands
#  Checkpoint:   A38c
#  Authors:      Ginger Allington, Natalie Kreitzer
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load the shapefile asset for the AOI as a Feature Collection
aoi = ee.FeatureCollection(
    'projects/gee-book/assets/A3-8/GEE_Ch_AOI')
Map.centerObject(aoi, 11)
Map.addLayer(aoi, {}, 'Subset of Naiman Banner')

# Filter the MODIS Collection
MODIS_LC = ee.ImageCollection('MODIS/006/MCD12Q1').select(
    'LC_Type1')

# Function to clip an image from the collection and set the year
def clipCol(img):
    date = ee.String(img.get('system:index'))
    date = date.slice(0, 4)
    return img.select('LC_Type1').clip(aoi) # .clip(aoi) \
        .set('year', date)


# Generate images for diff years you want to compare
modis01 = MODIS_LC.filterDate('2001-01-01', '2002-01-01').map(
    clipCol)
modis09 = MODIS_LC.filterDate('2009-01-01', '2010-01-01').map(
    clipCol)
modis16 = MODIS_LC.filterDate('2016-01-01', '2017-01-01').map(
    clipCol)
# Create an Image for each of the years
modis01 = modis01.first()
modis09 = modis09.first()
modis16 = modis16.first()

#Map.addLayer(modis01.randomVisualizer(), {}, 'modis 2001', False)
#Map.addLayer(modis09.randomVisualizer(), {}, 'modis 2009', False)
#Map.addLayer(modis16.randomVisualizer(), {}, 'modis 2016', False)

# Add and clip the WorldCover data
wCov = ee.ImageCollection('ESA/WorldCover/v100').first()
landcover20 = wCov.clip(aoi)
Map.addLayer(landcover20, {}, 'Landcover 2020')

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------

greennessColl = ee.ImageCollection(
    'projects/gee-book/assets/A3-8/GreennessCollection_aoi')
precipColl = ee.ImageCollection(
    'projects/gee-book/assets/A3-8/PrecipCollection')
print(greennessColl, 'Greenness Image Collection')
print(precipColl, 'Precip Image Collection')

greennessParams = {
    'bands': ['greenness'],
    'max': 0.5,
    'min': 0.06,
    'opacity': 1,
    'palette': ['e70808', 'ffffff', '1de22c']
}

greenness1985 = greennessColl.filterDate('1985-01-01',
    '1986-01-01').select('greenness')
greenness1999 = greennessColl.filterDate('1999-01-01',
    '2000-01-01').select('greenness')

print(greenness1999)
greenness2019 = greennessColl.filterDate('2019-01-01',
    '2020-01-01').select('greenness')

Map.addLayer(greenness1985, greennessParams, 'Greenness 1985', False)
Map.addLayer(greenness1999, greennessParams, 'Greenness 1999', False)
Map.addLayer(greenness2019, greennessParams, 'Greenness 2019', False)



# Load a function that will combine the Precipitation and Greenness collections, run a regression, then predict NDVI and calculate the residuals.

# Load the module
residFunctions = require(
    'projects/gee-edu/book:Part A - Applications/A3 - Terrestrial Applications/A3.8 Detecting Land Cover Change in Rangelands/modules/calcResid'
)

# Call the function we want that is in that module
# It requires three input parameters:
# the greenness collection, the precipitation collection and the aoi
residualColl = (residFunctions.createResidColl(greennessColl,
    precipColl, aoi))

# Now inspect what you have generated:
print('Module output of residuals', residualColl)

resids = residualColl.first()
res1 = resids.select(['residual'])
print(res1.getInfo(), 'residual image')
Map.addLayer(res1, {
    'min': -0.2,
    'max': 0.2,
    'palette': ['red', 'white', 'green']
}, 'residuals 1985', False)

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------

#---- DEFINE RUN PARAMETERS---#
# LandTrendr run parameters
runParams = {
    'maxSegments': 6,
    'spikeThreshold': 0.9, #
    'vertexCountOvershoot': 3,
    'preventOneYearRecovery': True,
    'recoveryThreshold': 0.25, #
    'pvalThreshold': 0.05, #
    'bestModelProportion': 0.75,
    'minObservationsNeeded': 10 #
}

# Append the image collection to the LandTrendr run parameter dictionary
srCollection = residualColl
runParams.timeSeries = srCollection

# Run LandTrendr
lt = ee.Algorithms.TemporalSegmentation.LandTrendr(runParams)
# Explore the output from running LT
ltlt = lt.select('LandTrendr')
print(ltlt)

#---- SLICING OUT DATA -----------------#

# Select the LandTrendr band.
ltlt = lt.select('LandTrendr')
# Observation Year.
years = ltlt.arraySlice(0, 0, 1)
# Slice out observed Residual value.
observed = ltlt.arraySlice(0, 1, 2)
# Slice out fitted Residual values (predicted residual from final LT model).
fitted = ltlt.arraySlice(0, 2, 3)
# Slice out the 'Is Vertex' row - yes(1)/no(0).
vertexMask = ltlt.arraySlice(0, 3, 4)
# Use the 'Is Vertex' row as a mask for all rows.
vertices = ltlt.arrayMask(vertexMask)

# Define a few params we'll need next:
startYear_Num = 1985
endYear_Num = 2019
numYears = endYear_Num - startYear_Num
startMonth = '-01-01'
endMonth = '-12-31'

# Extract fitted residual value per year, per pixel and aggregate into an Image with one band per year
years = []
for (i = startYear_Num; i <= endYear_Num; ++i) years.push(i \
    .toString())
fittedStack = fitted.arrayFlatten([
    ['fittedResidual'], years
]).toFloat()
print(fittedStack, 'fitted stack')

Map.addLayer(fittedStack, {
    'bands': ['fittedResidual_1985'],
    'min': -0.2,
    'max': 0.2,
    'palette': ['red', 'white', 'green']
}, 'Fitted Residuals 1985')

# Extract boolean 'Is Vertex?' value per year, per pixel and aggregate into image w/ boolean band per year
years = []
for (i = startYear_Num; i <= endYear_Num; ++i) years.push(i \
    .toString())

vertexStack = vertexMask.arrayFlatten([
    ['bools'], years
]).toFloat()

print(vertexStack.getInfo(), 'vertex Stack')

# Load an Asset that has the booleans converted to Collection
booleanColl = ee.ImageCollection(
    'projects/gee-book/assets/A3-8/BooleanCollection')

chartBooleanMean = ui.Chart.image \
    .series({
        'imageCollection': booleanColl.select('bools'),
        'region': aoi,
        'reducer': ee.Reducer.mean(),
        'scale': 60,
        'xProperty': 'system:time_start'
    }) \
    .setChartType('ScatterChart') \
    .setOptions({
        'title': 'Naiman Boolean Mean Per Year',
        'vAxis': {
            'title': 'Boolean Mean Per Year'
        },
        'lineWidth': 1
    })

print(chartBooleanMean)

# Plot individual years to see the spatial patterns in the vertices.
boolParams = {
    # change this for the year you want to view
    'bands': 'bools_1997',
    'min': 0,
    # no vertex
    'max': 1,
    # vertex identified by LT for that year
    'palette': ['white', 'red']
}

Map.addLayer(vertexStack, boolParams, 'vertex 1997', False)
# this visualizes all pixels with a vertex in that year.

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map