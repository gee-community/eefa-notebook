import ee
import geemap

Map = geemap.Map()

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
geometry =

    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[77.65634552256087, 13.221993749480964],
          [77.65634552256087, 13.170852478759896],
          [77.75041595713118, 13.170852478759896],
          [77.75041595713118, 13.221993749480964]]], None, False),
    L8 = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
#**** End of imports. If edited, may not auto-convert in the playground. ****#
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.2 Urban Environments
#  Checkpoint:   A12a
#  Authors:      Michelle Stuhlmacher and Ran Goldblatt
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Map.centerObject(geometry)

# Filter collection.
collection = L8 \
    .filterBounds(geometry) \
    .filterDate('2010-01-01', '2020-12-31') \
    .filter(ee.Filter.lte('CLOUD_COVER_LAND', 3))

# Define GIF visualization arguments.
gifParams = {
    'bands': ['SR_B4', 'SR_B3', 'SR_B2'],
    'min': 0.07 * 65536,
    'max': 0.3 * 65536,
    'region': geometry,
    'framesPerSecond': 15,
    format: 'gif'
}

# Render the GIF animation in the console.
print(ui.Thumbnail(collection, gifParams))

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map
