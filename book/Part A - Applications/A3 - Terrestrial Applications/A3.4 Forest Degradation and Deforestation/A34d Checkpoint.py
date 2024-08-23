import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A3.4 Forest Degradation and Deforestation
#  Checkpoint:   A34d
#  Author:       Carlos Souza Jr., Karis Tenneson, John Dilger,
#                Crystal Wespestad, Eric Bullock
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

api = require("users/bullocke/coded:CODED/api")
utils = require("projects/GLANCE:ccdcUtilities/api")

# ------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------

# We will use the geometry of the image from the previous section as
# the study area.
studyArea = ee.Image("LANDSAT/LT05/C02/T1_L2/LT05_226068_19840411").geometry()

# Get cloud masked (Fmask) Landsat imagery.
landsat = (
    utils.Inputs.getLandsat()
    .filterBounds(studyArea)
    .filterDate("1984-01-01", "2021-01-01")
)

# Make a forest mask
gfwImage = ee.Image("UMD/hansen/global_forest_change_2019_v1_7")

# Get areas of forest cover above the threshold
treeCover = 40
forestMask = gfwImage.select("treecover2000").gte(treeCover).rename("landcover")

samples = ee.FeatureCollection(
    "projects/gee-book/assets/A3-4/sample_with_pred_hansen_2010"
)

minObservations = 4
chiSquareProbability = 0.97
training = samples
forestValue = 1
startYear = 1990
endYear = 2020
classBands = ["NDFI", "GV", "Shade", "NPV", "Soil"]
prepTraining = False

# ---------------- CODED parameters
codedParams = {
    "minObservations": minObservations,
    "chiSquareProbability": chiSquareProbability,
    "training": training,
    "studyArea": studyArea,
    forestValue: forestValue,
    forestMask: forestMask,
    "classBands": classBands,
    "collection": landsat,
    "startYear": startYear,
    "endYear": endYear,
    "prepTraining": prepTraining,
}

# -------------- Run CODED
results = api.ChangeDetection.coded(codedParams)
print(results)

# ------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------
Map
