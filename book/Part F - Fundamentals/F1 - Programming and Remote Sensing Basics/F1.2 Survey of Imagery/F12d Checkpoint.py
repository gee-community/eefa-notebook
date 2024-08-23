import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F1.2 Survey of Raster Datasets
#  Checkpoint:   F12d
#  Authors:      Andréa, Karen, Nick Clinton, David Saah
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##/
# Collections of single images - Landsat 8 Surface Reflectance
##/

# Create and Earth Engine Point object over San Francisco.
pointSF = ee.Geometry.Point([-122.44, 37.76])

# Import the Landsat 8 Surface Reflectance collection.
landsat8SR = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")

# Filter the collection and select the first image.
landsat8SRimage = (
    landsat8SR.filterDate("2014-03-18", "2014-03-19").filterBounds(pointSF).first()
)


print("Landsat 8 Surface Reflectance image", landsat8SRimage)

# Center map to the first image.
Map.centerObject(landsat8SRimage, 8)

# Add first image to the map.
Map.addLayer(
    landsat8SRimage,
    {"bands": ["SR_B4", "SR_B3", "SR_B2"], "min": 7000, "max": 13000},
    "Landsat 8 SR",
)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

##/
# Pre-made composites
##/

# Import a MODIS dataset of daily BRDF-corrected reflectance.
modisDaily = ee.ImageCollection("MODIS/006/MCD43A4")

# Filter the dataset to a recent date.
modisDailyRecent = modisDaily.filterDate("2021-11-01")

# Add the dataset to the map.
modisVis = {
    "bands": [
        "Nadir_Reflectance_Band1",
        "Nadir_Reflectance_Band4",
        "Nadir_Reflectance_Band3",
    ],
    "min": 0,
    "max": 4000,
}
Map.addLayer(modisDailyRecent, modisVis, "MODIS Daily Composite")


# Import the MODIS monthly burned areas dataset.
modisMonthly = ee.ImageCollection("MODIS/006/MCD64A1")

# Filter the dataset to a recent month during fire season.
modisMonthlyRecent = modisMonthly.filterDate("2021-08-01")

# Add the dataset to the map.
Map.addLayer(modisMonthlyRecent, {}, "MODIS Monthly Burn")

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
