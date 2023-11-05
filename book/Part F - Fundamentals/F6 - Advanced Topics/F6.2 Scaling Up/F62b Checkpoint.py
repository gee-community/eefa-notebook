import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F6.2 Scaling Up in Earth Engine
#  Checkpoint:   F62b
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
Map.addLayer(featColl)

# Specify years of interest.
startYear = 2001
endYear = 2020

# Climate dataset info.
imageCollectionName = 'IDAHO_EPSCOR/GRIDMET'
bandsWanted = ['pr', 'tmmn', 'tmmx']
scale = 4000

# Export info.
exportFolder = 'GEE_scalingUp'
filenameBase = 'Gridmet_counties_IN_IL_IA_' + scale + 'm_'

# Initiate a loop, in which the variable i takes on values of each year.
for i in range(startYear, endYear, 1):         # for each year....

  # Load climate collection for that year.
  startDate = i + '-01-01'

  endYear_adj = i + 1
  endDate = endYear_adj + '-01-01'

  imageCollection = ee.ImageCollection(imageCollectionName) \
      .select(bandsWanted) \
      .filterBounds(featColl) \
      .filterDate(startDate, endDate)

  # Get values at feature collection.

def func_rsk(image):
    return image.reduceRegions({
      'collection': featColl,
      'reducer': ee.Reducer.mean(),
      'tileScale': 1,
      'scale': scale
    }).filter(ee.Filter.NotNull(bandsWanted))  # remove rows without data \
      .map(function(f) {                  
        time_start = image.get('system:time_start')
        dte = ee.Date(time_start).format('YYYYMMdd')
        return f.set('date_ymd', dte)
    })

  sampledFeatures = imageCollection.map(func_rsk
).flatten()











).flatten()

  # Prepare export: specify properties and filename.
  columnsWanted = [uniqueID].concat(['date_ymd'], bandsWanted)
  filename = filenameBase + i

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