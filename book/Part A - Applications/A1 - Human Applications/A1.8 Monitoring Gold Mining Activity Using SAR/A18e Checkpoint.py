import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.6 Monitoring Gold Mining Activity using SAR
#  Checkpoint:   A16e
#  Authors:      Lucio Villa, Sidney Novoa, Milagros Becerra,
#                Andréa Puzzi Nicolau, Karen Dyson, Karis Tenneson, John Dilger
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###########################
#/ Section Four
###########################

# Define the area of study.
aoi = ee.FeatureCollection('projects/gee-book/assets/A1-8/mdd')

# Center the map.
Map.centerObject(aoi, 10)

# Create an empty image.
empty = ee.Image().byte()

# Convert the area of study to an EE image object so we can visualize
# only the boundary.
aoiOutline = empty.paint({
    'featureCollection': aoi,
    'color': 1,
    'width': 2
})

# Select the satellite basemap view.
Map.setOptions('SATELLITE')

# Add the area of study boundary to the map.
Map.addLayer(aoiOutline, {
    'palette': 'red'
}, 'Area of Study')

# Import the smap result from section 3.
changeDetect = ee.Image('projects/gee-book/assets/A1-8/smap')

# Visualization parameters.
countDates = 30
jet = ['black', 'blue', 'cyan', 'yellow', 'red']
vis = {
    'min': 0,
    'max': countDates,
    'palette': jet
}

# Add results to the map.
Map.addLayer(changeDetect, vis, 'Change Map Unfiltered')

# Digital Elevation Model SRTM.
# https:#developers.google.com/earth-engine/datasets/catalog/USGS_SRTMGL1_003
srtm = ee.Image('USGS/SRTMGL1_003').clip(aoi)
slope = ee.Terrain.slope(srtm)
srtmVis = {
    'min': 0,
    'max': 1000,
    'palette': ['black', 'blue', 'cyan', 'yellow', 'red']
}
Map.addLayer(srtm, srtmVis, 'SRTM Elevation')
slopeVis = {
    'min': 0,
    'max': 15,
    'palette': ['black', 'blue', 'cyan', 'yellow', 'red']
}
Map.addLayer(slope, slopeVis, 'SRTM Slope')

# Hansen Global Forest Change v1.8 (2000-2020)
# https:#developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2020_v1_8
gfc = ee.Image('UMD/hansen/global_forest_change_2020_v1_8').clip(
    aoi)
forest2020 = gfc.select('treecover2000') \
    .gt(0) \
    .updateMask(gfc.select('loss') \
        .neq(1)) \
    .selfMask()
Map.addLayer(forest2020,
    {
        'min': 0,
        'max': 1,
        'palette': ['black', 'green']
    },
    'Forest cover 2020')

# JRC Yearly Water Classification History, v1.3 (Updated until Dec 2020).
# https:#developers.google.com/earth-engine/datasets/catalog/JRC_GSW1_3_GlobalSurfaceWater
waterJRC = ee.Image('JRC/GSW1_3/GlobalSurfaceWater').select(
    'max_extent')
waterVis = {
    'min': 0,
    'max': 1,
    'palette': ['blue', 'black']
}
Map.addLayer(waterJRC.eq(0), waterVis, 'Water Bodies until 2020')

# Apply filters through masks.
alertsFiltered = changeDetect \
    .updateMask(srtm.lt(1000)) \
    .updateMask(slope.lt(15)) \
    .updateMask(forest2020.eq(1)) \
    .updateMask(waterJRC.eq(0)) \
    .selfMask()

# Add filtered results to the map.
Map.addLayer(alertsFiltered,
    {
        'min': 0,
        'max': countDates,
        'palette': jet
    },
    'Change Map Filtered',
    1)

# Function to filter small patches and isolated pixels.
def filterMinPatchs(alerts0, minArea0, maxSize0):
    pixelCount = alerts0.gt(0).connectedPixelCount(maxSize0)
    minPixelCount = ee.Image(minArea0).divide(ee.Image \
    .pixelArea())
    return alerts0.updateMask(pixelCount.gte(minPixelCount))


# Apply the function and visualize the filtered results.
alertsFiltMinPatchs = filterMinPatchs(alertsFiltered, 10000, 200)

Map.addLayer(alertsFiltMinPatchs, vis,
    'Alerts Filtered - Minimum Patches')

# Export filtered results to the Drive.
Export.image.toDrive({
    'image': alertsFiltMinPatchs,
    'description': 'alertsFiltered',
    'folder': 'alertsFiltered',
    'region': aoi,
    'scale': 10,
})

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map