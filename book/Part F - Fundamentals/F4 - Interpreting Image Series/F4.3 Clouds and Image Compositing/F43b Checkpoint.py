import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F4.3 Clouds and Image Compositing
#  Checkpoint:   F43b
#  Authors:      Txomin Hermosilla, Saverio Francini, Andréa P. Nicolau,
#                Michael A. Wulder, Joanne C. White, Nicholas C. Coops,
#                Gherardo Chirici
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ---------- Section 1 -----------------

# Define the AOI.
country = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017").filter(
    ee.Filter.equals("country_na", "Colombia")
)

# Center the Map. The second parameter is zoom level.
Map.centerObject(country, 5)

# Define time variables.
startDate = "2019-01-01"
endDate = "2019-12-31"

# Load and filter the Landsat 8 collection.
landsat8 = (
    ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
    .filterBounds(country)
    .filterDate(startDate, endDate)
)


# Apply scaling factors.
def applyScaleFactors(image):
    opticalBands = image.select("SR_B.").multiply(0.0000275).add(-0.2)
    thermalBands = image.select("ST_B.*").multiply(0.00341802).add(149.0)
    return image.addBands(opticalBands, None, True).addBands(thermalBands, None, True)


landsat8 = landsat8.map(applyScaleFactors)

# Create composite.
composite = landsat8.median().clip(country)

visParams = {"bands": ["SR_B4", "SR_B3", "SR_B2"], "min": 0, "max": 0.2}
Map.addLayer(composite, visParams, "L8 Composite")

# Filter by the CLOUD_COVER property.
landsat8FiltClouds = (
    landsat8.filterBounds(country)
    .filterDate(startDate, endDate)
    .filter(ee.Filter.lessThan("CLOUD_COVER", 50))
)

# Create a composite from the filtered imagery.
compositeFiltClouds = landsat8FiltClouds.median().clip(country)

Map.addLayer(compositeFiltClouds, visParams, "L8 Composite cloud filter")

# Print size of collections, for comparison.
print("Size landsat8 collection", landsat8.size())
print("Size landsat8FiltClouds collection", landsat8FiltClouds.size())


# Define the cloud mask function.
def maskSrClouds(image):
    # Bit 0 - Fill
    # Bit 1 - Dilated Cloud
    # Bit 2 - Cirrus
    # Bit 3 - Cloud
    # Bit 4 - Cloud Shadow
    qaMask = image.select("QA_PIXEL").bitwiseAnd(parseInt("11111", 2)).eq(0)
    saturationMask = image.select("QA_RADSAT").eq(0)

    return image.updateMask(qaMask).updateMask(saturationMask)


# Apply the cloud mask to the collection.
landsat8FiltMasked = landsat8FiltClouds.map(maskSrClouds)

# Create a composite.
landsat8compositeMasked = landsat8FiltMasked.median().clip(country)

Map.addLayer(landsat8compositeMasked, visParams, "L8 composite masked")

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# ---------- Section 2 -----------------

# Define Landsat 7 Level 2, Collection 2, Tier 1 collection.
landsat7 = ee.ImageCollection("LANDSAT/LE07/C02/T1_L2")


# Scaling factors for L7.
def applyScaleFactorsL7(image):
    opticalBands = image.select("SR_B.").multiply(0.0000275).add(-0.2)
    thermalBand = image.select("ST_B6").multiply(0.00341802).add(149.0)
    return image.addBands(opticalBands, None, True).addBands(thermalBand, None, True)


# Filter collection, apply cloud mask, and scaling factors.
landsat7FiltMasked = (
    landsat7.filterBounds(country)
    .filterDate(startDate, endDate)
    .filter(ee.Filter.lessThan("CLOUD_COVER", 50))
    .map(maskSrClouds)
    .map(applyScaleFactorsL7)
)

# Create composite.
landsat7compositeMasked = landsat7FiltMasked.median().clip(country)

Map.addLayer(
    landsat7compositeMasked,
    {"bands": ["SR_B3", "SR_B2", "SR_B1"], "min": 0, "max": 0.2},
    "L7 composite masked",
)


# Since Landsat 7 and 8 have different band designations,
# let's create a function to rename L7 bands to match to L8.
def rename(image):
    return image.select(
        ["SR_B1", "SR_B2", "SR_B3", "SR_B4", "SR_B5", "SR_B7"],
        ["SR_B2", "SR_B3", "SR_B4", "SR_B5", "SR_B6", "SR_B7"],
    )


# Apply the rename function.
landsat7FiltMaskedRenamed = landsat7FiltMasked.map(rename)

# Merge Landsat collections.
landsat78 = landsat7FiltMaskedRenamed.merge(
    landsat8FiltMasked.select(["SR_B2", "SR_B3", "SR_B4", "SR_B5", "SR_B6", "SR_B7"])
)


def func_fpu(img):
    return img.toFloat().map(func_fpu)


print("Merged collections", landsat78)

# Create Landsat 7 and 8 image composite and add to the Map.
landsat78composite = landsat78.median().clip(country)
Map.addLayer(landsat78composite, visParams, "L7 and L8 composite")

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
