import ee 
import geemap

Map = geemap.Map()

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
msi = ee.ImageCollection("COPERNICUS/S2"),
    naip = ee.ImageCollection("USDA/NAIP/DOQQ"),
    eo1 = ee.ImageCollection("EO1/HYPERION"),
    tm = ee.ImageCollection("LANDSAT/LT05/C02/T1"),
    mod09 = ee.ImageCollection("MODIS/061/MOD09A1")
#**** End of imports. If edited, may not auto-convert in the playground. ****#
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F1.3 The Remote Sensing Vocabulary
#  Checkpoint:   F13b
#  Authors:      K. Dyson, A. P. Nicolau, D. Saah, and N. Clinton
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###
# Explore spatial resolution
###

# Define a region of interest as a point at San Francisco airport.
sfoPoint = ee.Geometry.Point(-122.3774, 37.6194)

# Center the map at that point.
Map.centerObject(sfoPoint, 16)

# MODIS
# Get an image from your imported MODIS MYD09GA collection.
modisImage = mod09.filterDate('2020-02-01', '2020-03-01').first()

# Use these MODIS bands for near infrared, red, and green, respectively.
modisBands = ['sur_refl_b02', 'sur_refl_b01', 'sur_refl_b04']

# Define visualization parameters for MODIS.
modisVis = {
    'bands': modisBands,
    'min': 0,
    'max': 3000
}

# Add the MODIS image to the map.
Map.addLayer(modisImage, modisVis, 'MODIS')

# Get the scale of the data from the NIR band's projection:
modisScale = modisImage.select('sur_refl_b02') \
    .projection().nominalScale()

print('MODIS NIR scale:', modisScale)

# TM
# Filter TM imagery by location and date.

tmImage = tm \
    .filterBounds(Map.getCenter()) \
    .filterDate('1987-03-01', '1987-08-01') \
    .first()

# Display the TM image as a False color composite.
Map.addLayer(tmImage, {
    'bands': ['B4', 'B3', 'B2'],
    'min': 0,
    'max': 100
}, 'TM')

# Get the scale of the TM data from its projection:
tmScale = tmImage.select('B4') \
    .projection().nominalScale()

print('TM NIR scale:', tmScale)

# MSI
# Filter MSI imagery by location and date.
msiImage = msi \
    .filterBounds(Map.getCenter()) \
    .filterDate('2020-02-01', '2020-04-01') \
    .first()

# Display the MSI image as a False color composite.
Map.addLayer(msiImage, {
    'bands': ['B8', 'B4', 'B3'],
    'min': 0,
    'max': 2000
}, 'MSI')

# Get the scale of the MSI data from its projection:
msiScale = msiImage.select('B8') \
    .projection().nominalScale()
print('MSI scale:', msiScale)

# NAIP
# Get NAIP images for the study period and region of interest.
naipImage = naip \
    .filterBounds(Map.getCenter()) \
    .filterDate('2018-01-01', '2018-12-31') \
    .first()

# Display the NAIP mosaic as a color-IR composite.
Map.addLayer(naipImage, {
    'bands': ['N', 'R', 'G']
}, 'NAIP')

# Get the NAIP resolution from the first image in the mosaic.
naipScale = naipImage.select('N') \
    .projection().nominalScale()

print('NAIP NIR scale:', naipScale)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

##/
# Explore Temporal Resolution
##/

# Use Print to see Landsat revisit time
print('Landsat-5 series:', tm \
    .filterBounds(Map.getCenter()) \
    .filterDate('1987-06-01', '1987-09-01'))

# Create a chart to see Landsat 5's 16 day revisit time.
tmChart = ui.Chart.image.series({
    'imageCollection': tm.select('B4').filterDate('1987-06-01',
        '1987-09-01'),
    'region': sfoPoint
}).setSeriesNames(['NIR'])

# Define a chart style that will let us see the individual dates.
chartStyle = {
    'hAxis': {
        'title': 'Date'
    },
    'vAxis': {
        'title': 'NIR Mean'
    },
    'series': {
        '0': {
            'lineWidth': 3,
            'pointSize': 6
        }
    },
}

# Apply custom style properties to the chart.
tmChart.setOptions(chartStyle)

# Print the chart.
print('TM Chart', tmChart)

# Sentinel-2 has a 5 day revisit time.
msiChart = ui.Chart.image.series({
    'imageCollection': msi.select('B8').filterDate('2020-06-01',
        '2020-09-01'),
    'region': sfoPoint
}).setSeriesNames(['NIR'])

# Apply the previously defined custom style properties to the chart.
msiChart.setOptions(chartStyle)

# Print the chart.
print('MSI Chart', msiChart)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

Map