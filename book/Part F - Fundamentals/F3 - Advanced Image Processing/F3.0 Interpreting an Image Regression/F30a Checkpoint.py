import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F3.0 Interpreting an Image: Regression
#  Checkpoint:   F30a
#  Authors:      K. Dyson, A. Nicolau, D. Saah, N. Clinton
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define a Turin polygon.
Turin = ee.Geometry.Polygon(
    [
        [
            [7.455553918110218, 45.258245019259036],
            [7.455553918110218, 44.71237367431335],
            [8.573412804828967, 44.71237367431335],
            [8.573412804828967, 45.258245019259036],
        ]
    ],
    None,
    False,
)

# Center on Turin
Map.centerObject(Turin, 9)

mod44b = ee.ImageCollection("MODIS/006/MOD44B")

##/
# Start Linear Fit
##/

# Put together the dependent variable by filtering the
# ImageCollection to just the 2020 image near Turin and
# selecting the percent tree cover band.
percentTree2020 = (
    mod44b.filterDate("2020-01-01", "2021-01-01")
    .first()
    .clip(Turin)
    .select("Percent_Tree_Cover")
)

# You can print information to the console for inspection.
print("2020 Image", percentTree2020)

Map.addLayer(percentTree2020, {"max": 100}, "Percent Tree Cover")

landsat8_raw = ee.ImageCollection("LANDSAT/LC08/C02/T1_RT")

# Put together the independent variable.
landsat8filtered = (
    landsat8_raw.filterBounds(Turin.centroid({"maxError": 1}))
    .filterDate("2020-04-01", "2020-4-30")
    .first()
)

print("Landsat8 filtered", landsat8filtered)

# Display the L8 image.
visParams = {"bands": ["B4", "B3", "B2"], "max": 16000}
Map.addLayer(landsat8filtered, visParams, "Landsat 8 Image")

# Calculate NDVI which will be the independent variable.
ndvi = landsat8filtered.normalizedDifference(["B5", "B4"])

# Create the training image.
trainingImage = ndvi.addBands(percentTree2020)
print("training image for linear fit", trainingImage)


# Independent variable first, dependent variable second.
# You need to include the scale variable.
linearFit = trainingImage.reduceRegion(
    {
        "reducer": ee.Reducer.linearFit(),
        "geometry": Turin,
        "scale": 30,
        "bestEffort": True,
    }
)

# Inspect the results.
print("OLS estimates:", linearFit)
print("y-intercept:", linearFit.get("offset"))
print("Slope:", linearFit.get("scale"))

# Create a prediction based on the linearFit model.
predictedTree = ndvi.expression(
    "intercept + slope * ndvi",
    {
        "ndvi": ndvi.select("nd"),
        "intercept": ee.Number(linearFit.get("offset")),
        "slope": ee.Number(linearFit.get("scale")),
    },
)

print("predictedTree", predictedTree)

# Display the results.
Map.addLayer(predictedTree, {"max": 100}, "Predicted Percent Tree Cover")

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------


Map
