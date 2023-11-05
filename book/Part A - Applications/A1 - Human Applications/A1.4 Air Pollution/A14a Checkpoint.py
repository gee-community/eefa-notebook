import ee 
import geemap

Map = geemap.Map()

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
geometry =

    # shown: False #
    ee.Geometry.Point([114.26732477622326, 30.57603159263821])
#**** End of imports. If edited, may not auto-convert in the playground. ****#
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.4 Air Pollution and Population Exposures
#  Checkpoint:   A14a
#  Authors:      Zander Venter and Sourangsu Chowdhury
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#
 # Section 1: data import and cleaning
 #

# Import a global dataset of administrative units level 1.
adminUnits = ee.FeatureCollection(
    'FAO/GAUL_SIMPLIFIED_500m/2015/level1')

# Filter for the administrative unit that intersects
# the geometry located at the top of this script.
adminSelect = adminUnits.filterBounds(geometry)

# Center the map on this area.
Map.centerObject(adminSelect, 8)

# Make the base map HYBRID.
Map.setOptions('HYBRID')

# Add it to the map to make sure you have what you want.
Map.addLayer(adminSelect, {}, 'selected admin unit')

# Import the population count data from Gridded Population of the World Version 4.
population = ee.ImageCollection(
        'CIESIN/GPWv411/GPW_Population_Count') \
    .filter(ee.Filter.calendarRange(2020, 2020, 'year')) \
    .mean()

# Clip it to your area of interest (only necessary for visualization purposes).
populationClipped = population.clipToCollection(adminSelect)

# Add it to the map to see the population distribution.
popVis = {
    'min': 0,
    'max': 4000,
    'palette': ['black', 'yellow', 'white'],
    'opacity': 0.55
}
Map.addLayer(populationClipped, popVis, 'population count')

# Import the Sentinel-5P NO2 offline product.
no2Raw = ee.ImageCollection('COPERNICUS/S5P/OFFL/L3_NO2')

# Define function to exclude cloudy pixels.
def maskClouds(image):
    # Get the cloud fraction band of the image.
    cf = image.select('cloud_fraction')
    # Create a mask using 0.3 threshold.
    mask = cf.lte(0.3); # You can play around with this value.
    # Return a masked image.
    return image.updateMask(mask).copyProperties(image)


# Clean and filter the Sentinel-5P NO2 offline product.
no2 = no2Raw \
    .filterBounds(adminSelect) \
    .map(maskClouds) \
    .select('tropospheric_NO2_column_number_density')

# Create a median composite for March 2021
no2Median = no2.filterDate('2021-03-01', '2021-04-01').median()

# Clip it to your area of interest (only necessary for visualization purposes).
no2MedianClipped = no2Median.clipToCollection(adminSelect)

# Visualize the median NO2.
no2Viz = {
    'min': 0,
    'max': 0.00015,
    'palette': ['black', 'blue', 'purple', 'cyan', 'green',
        'yellow', 'red'
    ]
}
Map.addLayer(no2MedianClipped, no2Viz, 'median no2 Mar 2021')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map