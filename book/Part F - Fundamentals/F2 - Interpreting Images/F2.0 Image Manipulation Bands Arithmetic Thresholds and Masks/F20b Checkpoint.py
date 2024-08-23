import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F2.0 Image Manipulation: Bands, Arithmetic, Thresholds, and Masks
#  Checkpoint:   F20b
#  Authors:      Karen Dyson, Andrea Puzzi Nicolau, David Saah, and Nicholas Clinton
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create an NDVI image using Sentinel 2.
seaPoint = ee.Geometry.Point(-122.2040, 47.6221)
seaImage = (
    ee.ImageCollection("COPERNICUS/S2")
    .filterBounds(seaPoint)
    .filterDate("2020-08-15", "2020-10-01")
    .first()
)

seaNDVI = seaImage.normalizedDifference(["B8", "B4"])

# And map it.
Map.centerObject(seaPoint, 10)
vegPalette = ["red", "white", "green"]
Map.addLayer(seaNDVI, {"min": -1, "max": 1, "palette": vegPalette}, "NDVI Seattle")

# Implement a threshold.
seaVeg = seaNDVI.gt(0.5)

# Map the threshold.
Map.addLayer(
    seaVeg, {"min": 0, "max": 1, "palette": ["white", "green"]}, "Non-forest vs. Forest"
)

# Implement .where.
# Create a starting image with all values = 1.
seaWhere = ee.Image(1).clip(seaNDVI.geometry())

# Make all NDVI values less than -0.1 equal 0.
seaWhere = seaWhere.where(seaNDVI.lte(-0.1), 0)

# Make all NDVI values greater than 0.5 equal 2.
seaWhere = seaWhere.where(seaNDVI.gte(0.5), 2)

# Map our layer that has been divided into three classes.
Map.addLayer(
    seaWhere,
    {"min": 0, "max": 2, "palette": ["blue", "white", "green"]},
    "Water, Non-forest, Forest",
)

# Implement masking.
# View the seaVeg layer's current mask.
Map.centerObject(seaPoint, 9)
Map.addLayer(seaVeg.mask(), {}, "seaVeg Mask")

# Create a binary mask of non-forest.
vegMask = seaVeg.eq(1)

# Update the seaVeg mask with the non-forest mask.
maskedVeg = seaVeg.updateMask(vegMask)

# Map the updated Veg layer
Map.addLayer(
    maskedVeg, {"min": 0, "max": 1, "palette": ["green"]}, "Masked Forest Layer"
)

# Map the updated mask
Map.addLayer(maskedVeg.mask(), {}, "maskedVeg Mask")

# Implement remapping.
# Remap the values from the seaWhere layer.
seaRemap = seaWhere.remap([0, 1, 2], [9, 11, 10])  # Existing values.
# Remapped values.

Map.addLayer(
    seaRemap,
    {"min": 9, "max": 11, "palette": ["blue", "green", "white"]},
    "Remapped Values",
)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------


Map
