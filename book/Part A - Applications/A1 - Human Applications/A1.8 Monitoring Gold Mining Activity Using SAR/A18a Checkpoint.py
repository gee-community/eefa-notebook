import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.8 Monitoring Gold Mining Activity using SAR
#  Checkpoint:   A18a
#  Authors:      Lucio Villa, Sidney Novoa, Milagros Becerra,
#                Andréa Puzzi Nicolau, Karen Dyson, Karis Tenneson, John Dilger
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###########################
#/ Section One
###########################

# Define the area of study.
aoi = ee.FeatureCollection('projects/gee-book/assets/A1-8/mdd')

# Center the map at the aoi.
Map.centerObject(aoi, 9)

# Create an empty image.
empty = ee.Image().byte()

# Convert the area of study to an EE image object
# so we can visualize only the boundary.
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

# Function to mask the SAR images acquired with an incidence angle
# lower or equal to  31 and greater or equal to 45 degrees.
def maskAngle(image):
    angleMask = image.select('angle')
    return image.updateMask(angleMask.gte(31).And(angleMask.lte(45)))


# Function to get the SAR Collection.
def getCollection(dates, roi, orbitPass0):
    sarCollFloat = ee.ImageCollection('COPERNICUS/S1_GRD_FLOAT') \
        .filterBounds(roi) \
        .filterDate(dates[0], dates[1]) \
        .filter(ee.Filter.eq('orbitProperties_pass', orbitPass0))
    return sarCollFloat.map(maskAngle).select(['VV', 'VH'])


# Define variables: the period of time and the orbitpass.
listOfDates = ['2021-08-01', '2021-08-12']
orbitPass = 'DESCENDING'

# Apply the function to get the SAR mosaic.
sarImageColl = getCollection(listOfDates, aoi, orbitPass) \
    .mosaic() \
    .clip(aoi)
print('SAR Image Mosaic', sarImageColl)

# Apply logarithmic scale.
sarImageScaled = sarImageColl.log10().multiply(10.0)

# Visualize results.
sarVis = {
    'bands': ['VV', 'VH', 'VV'],
    'min': [-18, -23, 3],
    'max': [-4, -11, 15]
}
Map.addLayer(sarImageScaled, sarVis, 'Sentinel-1 / SAR Mosaic')

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map