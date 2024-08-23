import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A3.2 Mangroves
#  Checkpoint:   A32a
#  Author:       Aurélie Shapiro
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create an ee.Geometry.
aoi = ee.Geometry.Polygon([[[88.3, 22.61], [90, 22.61], [90, 21.47], [88.3, 21.47]]])

# Locate a coordinate in the aoi with land and water.
point = ee.Geometry.Point([89.2595, 21.7317])

# Position the map.
Map.centerObject(point, 13)
Map.addLayer(aoi, {}, "AOI")

# Sentinel-1 wet season data.
wetS1 = ee.Image("projects/gee-book/assets/A3-2/wet_season_tscan_2020")
# Sentinel-1 dry season data.
dryS1 = ee.Image("projects/gee-book/assets/A3-2/dry_season_tscan_2020")
# Sentinel-2 mosaic.
S2 = ee.Image("projects/gee-book/assets/A3-2/Sundarbans_S2_2020")

# Visualize the input data.
s1VisParams = {"bands": ["VV_min", "VH_min", "VVVH_ratio_min"], "min": -36, "max": 3}
s2VisParams = {"bands": ["swir1", "nir", "red"], "min": 82, "max": 3236}

Map.addLayer(dryS1, s1VisParams, "S1 dry", False)
Map.addLayer(wetS1, s1VisParams, "S1 wet", False)
Map.addLayer(S2, s2VisParams, "S2 2020")

NDVI = S2.normalizedDifference(["nir", "red"]).rename(["NDVI"])

ratio_swir1_nir = S2.expression(
    "swir1/(nir+0.1)", {"swir1": S2.select("swir1"), "nir": S2.select("nir")}
).rename("ratio_swir1_nir_wet")

data_stack = S2.addBands(NDVI).addBands(ratio_swir1_nir).addBands(dryS1).addBands(wetS1)

print(data_stack)
# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map
