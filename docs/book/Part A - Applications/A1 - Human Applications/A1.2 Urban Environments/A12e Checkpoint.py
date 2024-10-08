import ee
import geemap

Map = geemap.Map()

# *** Start of imports. If edited, may not auto-convert in the playground. ***#
L7 = ee.ImageCollection("LANDSAT/LE07/C02/T1_L2")
# **** End of imports. If edited, may not auto-convert in the playground. ****#
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.2 Urban Environments
#  Checkpoint:   A12e
#  Authors:      Michelle Stuhlmacher and Ran Goldblatt
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Surface reflectance function from example:
def maskL457sr(image):
    qaMask = image.select("QA_PIXEL").bitwiseAnd(parseInt("11111", 2)).eq(0)
    saturationMask = image.select("QA_RADSAT").eq(0)

    # Apply the scaling factors to the appropriate bands.
    opticalBands = image.select("SR_B.").multiply(0.0000275).add(-0.2)
    thermalBand = image.select("ST_B6").multiply(0.00341802).add(149.0)

    # Replace the original bands with the scaled ones and apply the masks.
    return (
        image.addBands(opticalBands, None, True)
        .addBands(thermalBand, None, True)
        .updateMask(qaMask)
        .updateMask(saturationMask)
    )


# Map the function over one year of data.
collection = L7.filterDate("2020-01-01", "2021-01-01").map(maskL457sr)
landsat7_2020 = collection.median()

Map.addLayer(
    landsat7_2020,
    {"bands": ["SR_B3", "SR_B2", "SR_B1"], "min": 0, "max": 0.3},
    "landsat 7, 2020",
)

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map
