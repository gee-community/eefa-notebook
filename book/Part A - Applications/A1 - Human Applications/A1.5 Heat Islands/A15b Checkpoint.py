import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.5 Heat Islands
#  Checkpoint:   A15b
#  Author:       TC Chakraborty
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load feature collection of New Haven's census tracts from user assets.
regionInt = ee.FeatureCollection("projects/gee-book/assets/A1-5/TC_NewHaven")

# Get dissolved feature collection using an error margin of 50 meters.
regionInt = regionInt.union(50)

# Set map center and zoom level (Zoom level varies from 1 to 20).
Map.setCenter(-72.9, 41.3, 12)

# Add layer to map.
Map.addLayer(regionInt, {}, "New Haven boundary")

# Load MODIS image collection from the Earth Engine data catalog.
modisLst = ee.ImageCollection("MODIS/006/MYD11A2")

# Select the band of interest (in this case: Daytime LST).
landSurfTemperature = modisLst.select("LST_Day_1km")

# Create a summer filter.
sumFilter = ee.Filter.dayOfYear(152, 243)

# Filter the date range of interest using a date filter.
lstDateInt = landSurfTemperature.filterDate("2014-01-01", "2019-01-01").filter(
    sumFilter
)

# Take pixel-wise mean of all the images in the collection.
lstMean = lstDateInt.mean()

# Multiply each pixel by scaling factor to get the LST values.
lstFinal = lstMean.multiply(0.02)

# Generate a water mask.
water = ee.Image("JRC/GSW1_0/GlobalSurfaceWater").select("occurrence")
notWater = water.mask().Not()

# Clip data to region of interest, convert to degree Celsius, and mask water pixels.
lstNewHaven = lstFinal.clip(regionInt).subtract(273.15).updateMask(notWater)

# Add layer to map.
Map.addLayer(
    lstNewHaven,
    {"palette": ["blue", "white", "red"], "min": 25, "max": 38},
    "LST_MODIS",
)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------


# Function to filter out cloudy pixels.
def cloudMask(cloudyScene):
    # Add a cloud score band to the image.
    scored = ee.Algorithms.Landsat.simpleCloudScore(cloudyScene)

    # Create an image mask from the cloud score band and specify threshold.
    mask = scored.select(["cloud"]).lte(10)

    # Apply the mask to the original image and return the masked image.
    return cloudyScene.updateMask(mask)


# Load the collection, apply cloud mask, and filter to date and region of interest.
col = (
    ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA")
    .filterBounds(regionInt)
    .filterDate("2014-01-01", "2019-01-01")
    .filter(sumFilter)
    .map(cloudMask)
)

print("Landsat collection", col)

# Generate median composite.
image = col.median()

# Select thermal band 10 (with brightness temperature).
thermal = image.select("B10").clip(regionInt).updateMask(notWater)

Map.addLayer(
    thermal, {"min": 295, "max": 310, "palette": ["blue", "white", "red"]}, "Landsat_BT"
)

# Calculate Normalized Difference Vegetation Index (NDVI)
# from Landsat surface reflectance.
ndvi = (
    ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
    .filterBounds(regionInt)
    .filterDate("2014-01-01", "2019-01-01")
    .filter(sumFilter)
    .median()
    .normalizedDifference(["SR_B5", "SR_B4"])
    .rename("NDVI")
    .clip(regionInt)
    .updateMask(notWater)
)

Map.addLayer(ndvi, {"min": 0, "max": 1, "palette": ["blue", "white", "green"]}, "ndvi")

# Find the minimum and maximum of NDVI.  Combine the reducers
# for efficiency (single pass over the data).
minMax = ndvi.reduceRegion(
    {
        "reducer": ee.Reducer.min().combine(
            {"reducer2": ee.Reducer.max(), "sharedInputs": True}
        ),
        "geometry": regionInt,
        "scale": 30,
        "maxPixels": 1e9,
    }
)
print("minMax", minMax)

min = ee.Number(minMax.get("NDVI_min"))
max = ee.Number(minMax.get("NDVI_max"))

# Calculate fractional vegetation.
fv = ndvi.subtract(min).divide(max.subtract(min)).rename("FV")
Map.addLayer(fv, {"min": 0, "max": 1, "palette": ["blue", "white", "green"]}, "fv")

# Emissivity calculations.
a = ee.Number(0.004)
b = ee.Number(0.986)
em = fv.multiply(a).add(b).rename("EMM").updateMask(notWater)

Map.addLayer(
    em, {"min": 0.98, "max": 0.99, "palette": ["blue", "white", "green"]}, "EMM"
)

# Calculate LST from emissivity and brightness temperature.
lstLandsat = thermal.expression(
    "(Tb/(1 + (0.001145* (Tb / 1.438))*log(Ep)))-273.15",
    {"Tb": thermal.select("B10"), "Ep": em.select("EMM")},
).updateMask(notWater)

Map.addLayer(
    lstLandsat,
    {
        "min": 25,
        "max": 35,
        "palette": ["blue", "white", "red"],
    },
    "LST_Landsat",
)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
