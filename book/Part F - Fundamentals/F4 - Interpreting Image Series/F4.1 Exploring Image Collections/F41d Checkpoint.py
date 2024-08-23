import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F4.1 Exploring Image Collections
#  Checkpoint:   F41d
#  Author:       Gennadii Donchyts
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define a region of interest as a point in Lisbon, Portugal.
lisbonPoint = ee.Geometry.Point(-9.179473, 38.763948)

# Center the map at that point.
Map.centerObject(lisbonPoint, 16)

# filter the large ImageCollection to be just images from 2020
# around Lisbon. From each image, select True-color bands to draw
filteredIC = (
    ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA")
    .filterDate("2020-01-01", "2021-01-01")
    .filterBounds(lisbonPoint)
    .select(["B6", "B5", "B4"])
)

# Add the filtered ImageCollection so that we can inspect values
# via the Inspector tool
Map.addLayer(filteredIC, {}, "TOA image collection")

# Construct a chart using values queried from image collection.
chart = ui.Chart.image.series(
    {
        "imageCollection": filteredIC,
        "region": lisbonPoint,
        "reducer": ee.Reducer.first(),
        "scale": 10,
    }
)

# Show the chart in the Console.
print(chart)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# compute and show the number of observations in an image collection
count = (
    ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA")
    .filterDate("2020-01-01", "2021-01-01")
    .select(["B6"])
    .count()
)

# add white background and switch to HYBRID basemap
Map.addLayer(ee.Image(1), {"palette": ["white"]}, "white", True, 0.5)
Map.setOptions("HYBRID")

# show image count
Map.addLayer(
    count,
    {
        "min": 0,
        "max": 50,
        "palette": ["d7191c", "fdae61", "ffffbf", "a6d96a", "1a9641"],
    },
    "landsat 8 image count (2020)",
)

# Center the map at that point.
Map.centerObject(lisbonPoint, 5)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Zoom to an informative scale for the code that follows.
Map.centerObject(lisbonPoint, 10)

# Add a mean composite image.
meanFilteredIC = filteredIC.reduce(ee.Reducer.mean())
Map.addLayer(meanFilteredIC, {}, "Mean values within image collection")

# Add a median composite image.
medianFilteredIC = filteredIC.reduce(ee.Reducer.median())
Map.addLayer(medianFilteredIC, {}, "Median values within image collection")

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# compute a single 30% percentile
p30 = filteredIC.reduce(ee.Reducer.percentile([30]))

Map.addLayer(p30, {"min": 0.05, "max": 0.35}, "30%")

percentiles = [0, 10, 20, 30, 40, 50, 60, 70, 80]

# let's compute percentile images and add them as separate layers


def func_sax(p):
    image = filteredIC.reduce(ee.Reducer.percentile([p]))
    Map.addLayer(image, {"min": 0.05, "max": 0.35}, p + "%")


percentiles.map(func_sax)


#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------


Map
