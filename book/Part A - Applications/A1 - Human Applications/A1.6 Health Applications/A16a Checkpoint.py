import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.6 Health Applications
#  Checkpoint:   A16a
#  Author:       Dawn Nekorchuk
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Section 1: Data Import
woredas = ee.FeatureCollection("projects/gee-book/assets/A1-6/amhara_woreda_20170207")
# Create region outer boundary to filter products on.
amhara = woredas.geometry().bounds()
gpm = ee.ImageCollection("NASA/GPM_L3/IMERG_V06")
LSTTerra8 = ee.ImageCollection("MODIS/061/MOD11A2").filterDate("2001-06-26", Date.now())
brdfReflect = ee.ImageCollection("MODIS/006/MCD43A4")
brdfQa = ee.ImageCollection("MODIS/006/MCD43A2")

# Visualize woredas with black borders and no fill.
# Create an empty image into which to paint the features, cast to byte.
empty = ee.Image().byte()
# Paint all the polygon edges with the same number and width.
outline = empty.paint({"featureCollection": woredas, "color": 1, "width": 1})
# Add woreda boundaries to the map.
Map.setCenter(38, 11.5, 7)
Map.addLayer(outline, {"palette": "000000"}, "Woredas")

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map
