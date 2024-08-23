import ee
import geemap

Map = geemap.Map()

# *** Start of imports. If edited, may not auto-convert in the playground. ***#
NLCD = ee.ImageCollection("USGS/NLCD_RELEASES/2019_REL/NLCD")
# **** End of imports. If edited, may not auto-convert in the playground. ****#
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.2 Urban Environments
#  Checkpoint:   A12d
#  Authors:      Michelle Stuhlmacher and Ran Goldblatt
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# NLCD (Chicago)
# Center over Chicago.
Map.setCenter(-87.6324, 41.8799, 10)

# Select the land cover band.
NLCD_lc = NLCD.select("landcover")

# Filter NLCD collection to 2016.
NLCD_2016 = NLCD_lc.filter(ee.Filter.eq("system:index", "2016")).first()
Map.addLayer(NLCD_2016, {}, "NLCD 2016")

# Calculate the total area of the 'Developed high intensity' class (24) in Chicago.
Chicago = ee.FeatureCollection("projects/gee-book/assets/A1-2/Chicago")

# Clip classification to Chicago
NLCD_2016_chi = NLCD_2016.clip(Chicago)

# Set class 24 pixels to 1 and mask the rest.
NLCD_2016_chi_24 = NLCD_2016_chi.eq(24).selfMask()
Map.addLayer(NLCD_2016_chi_24, {}, "Chicago developed high intensity")

# Area calculation.
areaDev = (
    NLCD_2016_chi_24.multiply(ee.Image.pixelArea())
    .reduceRegion(
        {"reducer": ee.Reducer.sum(), "geometry": Chicago.geometry(), "scale": 30}
    )
    .get("landcover")
)
print(areaDev)

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map
