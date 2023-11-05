import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A3.8 Detecting Land Cover Change in Rangelands
#  Checkpoint:   A38a
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
Map