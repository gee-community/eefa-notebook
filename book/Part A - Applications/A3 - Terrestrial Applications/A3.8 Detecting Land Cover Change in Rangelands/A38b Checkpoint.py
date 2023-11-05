import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A3.8 Detecting Land Cover Change in Rangelands
#  Checkpoint:   A38b
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

Map.addLayer(modis01.randomVisualizer(), {}, 'modis 2001', False)
Map.addLayer(modis09.randomVisualizer(), {}, 'modis 2009', False)
Map.addLayer(modis16.randomVisualizer(), {}, 'modis 2016', False)

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



# Load a function that will combine the Precipitation and Greenness collections,
# run a regression, then predict NDVI and calculate the residuals.

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
Map