import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F5.1 Raster/Vector Conversions
#  Checkpoint:   F51b
#  Authors:      Keiko Nomura, Samuel Bowers
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# -------------#
# Section 1.3 #
# -------------#

# Read input data.
# Note: these datasets are periodically updated.
# Consider searching the Data Catalog for newer versions.
gfc = ee.Image("UMD/hansen/global_forest_change_2020_v1_8")
wdpa = ee.FeatureCollection("WCMC/WDPA/current/polygons")

# Print assets to show available layers and properties.
print(gfc)
print(wdpa.limit(10))
# Show first 10 records.


# Display deforestation.
deforestation = gfc.select("lossyear")

Map.addLayer(
    deforestation,
    {"min": 1, "max": 20, "palette": ["yellow", "orange", "red"]},
    "Deforestation raster",
)

# Display WDPA data.
protectedArea = wdpa.filter(ee.Filter.equals("NAME", "La Paya"))

# Display protected area as an outline (see F5.3 for paint()).
protectedAreaOutline = (
    ee.Image()
    .byte()
    .paint({"featureCollection": protectedArea, "color": 1, "width": 3})
)

Map.addLayer(protectedAreaOutline, {"palette": "white"}, "Protected area")

# Set up map display.
Map.centerObject(protectedArea)
Map.setOptions("SATELLITE")

# Convert from a deforestation raster to vector.
deforestationVector = deforestation.reduceToVectors(
    {
        "scale": deforestation.projection().nominalScale(),
        "geometry": protectedArea.geometry(),
        "labelProperty": "lossyear",  # Label polygons with a change year.
        "maxPixels": 1e13,
    }
)

# Count the number of individual change events
print("Number of change events:", deforestationVector.size())

# Display deforestation polygons. Color outline by change year.
deforestationVectorOutline = (
    ee.Image()
    .byte()
    .paint({"featureCollection": deforestationVector, "color": "lossyear", "width": 1})
)

Map.addLayer(
    deforestationVectorOutline,
    {"palette": ["yellow", "orange", "red"], "min": 1, "max": 20},
    "Deforestation vector",
)

chart = ui.Chart.feature.histogram(
    {"features": deforestationVector, "property": "lossyear"}
).setOptions(
    {
        "hAxis": {"title": "Year"},
        "vAxis": {"title": "Number of deforestation events"},
        "legend": {"position": "none"},
    }
)

print(chart)

# Generate deforestation point locations.


def func_hoz(feat):
    return feat.centroid()


deforestationCentroids = deforestationVector.map(func_hoz)


Map.addLayer(deforestationCentroids, {"color": "darkblue"}, "Deforestation centroids")

# Add a new property to the deforestation FeatureCollection
# describing the area of the change polygon.


def func_opk(feat):
    return feat.set("area", feat.geometry().area({"maxError": 10}).divide(10000))
    # Convert m^2 to hectare.


deforestationVector = deforestationVector.map(func_opk)


# Filter the deforestation FeatureCollection for only large-scale (>10 ha) changes
deforestationLarge = deforestationVector.filter(ee.Filter.gt("area", 10))

# Display deforestation area outline by year.
deforestationLargeOutline = (
    ee.Image()
    .byte()
    .paint({"featureCollection": deforestationLarge, "color": "lossyear", "width": 1})
)

Map.addLayer(
    deforestationLargeOutline,
    {"palette": ["yellow", "orange", "red"], "min": 1, "max": 20},
    "Deforestation (>10 ha)",
)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
