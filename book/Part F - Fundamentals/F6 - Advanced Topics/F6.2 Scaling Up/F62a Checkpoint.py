import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F6.2 Scaling Up in Earth Engine
#  Checkpoint:   F62a
#  Authors:      Jillian M. Deines, Stefania Di Tommaso, Nicholas Clinton, Noel Gorelick
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load county dataset.
# Filter counties in Indiana, Illinois, and Iowa by state FIPS code.
# Select only the unique ID column for simplicity.
countiesAll = ee.FeatureCollection('TIGER/2018/Counties')
states = ['17', '18', '19']
uniqueID = 'GEOID'
featColl = countiesAll.filter(ee.Filter.inList('STATEFP', states)) \
    .select(uniqueID)

print(featColl.size())
print(featColl.limit(1))

# Visualize target features (create Figure F6.2.1).
Map.centerObject(featColl, 5)
Map.addLayer(featColl)

# specify years of interest
startYear = 2020
endYear = 2020

# climate dataset info
imageCollectionName = 'IDAHO_EPSCOR/GRIDMET'
bandsWanted = ['pr', 'tmmn', 'tmmx']
scale = 4000

# Load and format climate data.
startDate = startYear + '-01-01'

endYear_adj = endYear + 1
endDate = endYear_adj + '-01-01'

imageCollection = ee.ImageCollection(imageCollectionName) \
    .select(bandsWanted) \
    .filterBounds(featColl) \
    .filterDate(startDate, endDate)

# get values at features

def func_tar(image):
    return image.reduceRegions({
            'collection': featColl,
            'reducer': ee.Reducer.mean(),
            'scale': scale
        }).filter(ee.Filter.NotNull(
        bandsWanted)) # drop rows with no data \
        .map(function(f) { 
            time_start = image.get(
                'system:time_start')
            dte = ee.Date(time_start).format(
                'YYYYMMdd')
            return f.set('date_ymd', dte)
        })

sampledFeatures = imageCollection.map(func_tar
).flatten()













).flatten()

print(sampledFeatures.limit(1))

# export info
exportFolder = 'GEE_scalingUp'
filename = 'Gridmet_counties_IN_IL_IA_' + scale + 'm_' + \
    startYear + '-' + endYear

# prepare export: specify properties/columns to include
columnsWanted = [uniqueID].concat(['date_ymd'], bandsWanted)
print(columnsWanted)

Export.table.toDrive({
    'collection': sampledFeatures,
    'description': filename,
    'folder': exportFolder,
    'fileFormat': 'CSV',
    'selectors': columnsWanted
})

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------



Map