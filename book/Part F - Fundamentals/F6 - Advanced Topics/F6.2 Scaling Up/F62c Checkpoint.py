import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F6.2 Scaling Up in Earth Engine
#  Checkpoint:   F62c
#  Authors:      Jillian M. Deines, Stefania Di Tommaso, Nicholas Clinton, Noel Gorelick
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Set the Region of Interest:Seattle, Washington, United States
roi = ee.Geometry.Point([-122.33524518034544, 47.61356183942883])

# Dates over which to create a median composite.
start = ee.Date("2019-03-01")
end = ee.Date("2019-09-01")

# Specify module with cloud mask functions.
s2mask_tools = require(
    "projects/gee-edu/book:Part F - Fundamentals/F6 - Advanced Topics/F6.2 Scaling Up/modules/s2cloudmask.js"
)


# Specify S2 collections and filter.

# Sentinel-2 surface reflectance data for the composite.
s2Sr = (
    ee.ImageCollection("COPERNICUS/S2_SR")
    .filterDate(start, end)
    .filterBounds(roi)
    .select(["B2", "B3", "B4", "B5"])
)

# Sentinel-2 Level 1C data (top-of-atmosphere).
# Bands B7, B8, B8A and B10 needed for CDI and the cloud mask function.
s2 = (
    ee.ImageCollection("COPERNICUS/S2")
    .filterBounds(roi)
    .filterDate(start, end)
    .select(["B7", "B8", "B8A", "B10"])
)

# Cloud probability dataset - used in cloud mask function
s2c = (
    ee.ImageCollection("COPERNICUS/S2_CLOUD_PROBABILITY")
    .filterDate(start, end)
    .filterBounds(roi)
)

# Apply the cloud mask.

# Join the cloud probability dataset to surface reflectance.
withCloudProbability = s2mask_tools.indexJoin(s2Sr, s2c, "cloud_probability")

# Join the L1C data to get the bands needed for CDI.
withS2L1C = s2mask_tools.indexJoin(withCloudProbability, s2, "l1c")

# Map the cloud masking function over the joined collection.
# Cast output to ImageCollection
masked = ee.ImageCollection(withS2L1C.map(s2mask_tools.maskImage))

# Take the median, specifying a tileScale to avoid memory errors.
median = masked.reduce(ee.Reducer.median(), 8)

# Display the results.
Map.centerObject(roi, 12)
Map.addLayer(roi)

viz = {"bands": ["B4_median", "B3_median", "B2_median"], "min": 0, "max": 3000}
Map.addLayer(median, viz, "median")

Map.centerObject(roi, 9)
Map.addLayer(roi)
Map.addLayer(median, viz, "median")

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------


Map
