import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F2.0 Image Manipulation: Bands, Arithmetic, Thresholds, and Masks
#  Checkpoint:   F20a
#  Authors:      Karen Dyson, Andrea Puzzi Nicolau, David Saah, and Nicholas Clinton
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##/
# Band Arithmetic
##/

# Calculate NDVI using Sentinel 2

# Import and filter imagery by location and date.
sfoPoint = ee.Geometry.Point(-122.3774, 37.6194)
sfoImage = (
    ee.ImageCollection("COPERNICUS/S2")
    .filterBounds(sfoPoint)
    .filterDate("2020-02-01", "2020-04-01")
    .first()
)

# Display the image as a False color composite.
Map.centerObject(sfoImage, 11)
Map.addLayer(
    sfoImage, {"bands": ["B8", "B4", "B3"], "min": 0, "max": 2000}, "False color"
)

# Extract the near infrared and red bands.
nir = sfoImage.select("B8")
red = sfoImage.select("B4")

# Calculate the numerator and the denominator using subtraction and addition respectively.
numerator = nir.subtract(red)
denominator = nir.add(red)

# Now calculate NDVI.
ndvi = numerator.divide(denominator)

# Add the layer to our map with a palette.
vegPalette = ["red", "white", "green"]
Map.addLayer(ndvi, {"min": -1, "max": 1, "palette": vegPalette}, "NDVI Manual")

# Now use the built-in normalizedDifference function to achieve the same outcome.
ndviND = sfoImage.normalizedDifference(["B8", "B4"])
Map.addLayer(
    ndviND, {"min": -1, "max": 1, "palette": vegPalette}, "NDVI normalizedDiff"
)

# Use normalizedDifference to calculate NDWI
ndwi = sfoImage.normalizedDifference(["B8", "B11"])
waterPalette = ["white", "blue"]
Map.addLayer(ndwi, {"min": -0.5, "max": 1, "palette": waterPalette}, "NDWI")

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

Map
