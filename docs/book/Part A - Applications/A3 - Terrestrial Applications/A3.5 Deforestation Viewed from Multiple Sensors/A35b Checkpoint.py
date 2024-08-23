import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A3.5 Deforestation Viewed from Multiple Sensors
#  Checkpoint:   A35b
#  Author:       Xiaojing Tang
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

testArea = ee.Geometry.Polygon(
    [
        [
            [-66.73156878460787, -8.662236005089952],
            [-66.73156878460787, -8.916025640576244],
            [-66.44867083538912, -8.916025640576244],
            [-66.44867083538912, -8.662236005089952],
        ]
    ]
)

Map.centerObject(testArea)

# Start and end of the training and monitoring period.
trainPeriod = ee.Dictionary({"start": "2017-01-01", "end": "2020-01-01"})
monitorPeriod = ee.Dictionary({"start": "2020-01-01", "end": "2021-01-01"})

# Near-real-time monitoring parameters.
nrtParam = {"z": 2, "m": 5, "n": 4}

# Sensor specific parameters.
lstParam = {"band": "NDFI", "minRMSE": 0.05, "strikeOnly": False}
s2Param = {"band": "NDFI", "minRMSE": 0.05, "strikeOnly": False}
s1Param = {"band": "VV", "minRMSE": 0.01, "strikeOnly": True}

# ------------------------------------------------------------------------
# CHECKPOINT
# ------------------------------------------------------------------------
Map
