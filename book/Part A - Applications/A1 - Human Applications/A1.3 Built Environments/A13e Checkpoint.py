import ee
import math
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.3 Built Environments
#  Checkpoint:   A13e
#  Author:       Erin Trochim
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import roads data.
grip4_africa = ee.FeatureCollection(
        'projects/sat-io/open-datasets/GRIP4/Africa'),
    grip4_europe = ee.FeatureCollection(
        'projects/sat-io/open-datasets/GRIP4/Europe'),
    grip4_north_america = ee.FeatureCollection(
        'projects/sat-io/open-datasets/GRIP4/North-America')

# Add a function to add line length in km.
def addLength(feature):
    return feature.set({
        'lengthKm': feature.length().divide(1000)
    }); # km


# Calculate line lengths for all roads in Africa.
grip4_africaLength = grip4_africa.map(addLength)

# Convert the roads to raster.
empty = ee.Image().float()

grip4_africaRaster = empty.paint({
    'featureCollection': grip4_africaLength,
    'color': 'lengthKm'
})

# Import simplified countries.
countries = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017')

# Filter to Africa.
Africa = countries.filter(ee.Filter.eq('wld_rgn', 'Africa'))

# Import global power transmission lines.
transmission = ee.FeatureCollection(
    'projects/sat-io/open-datasets/predictive-global-power-system/distribution-transmission-lines'
)

# Filter transmission lines to Africa.
transmissionAfrica = transmission.filterBounds(Africa)

# Calculate line lengths for all transmission lines in Africa.
transmissionAfricaLength = transmissionAfrica.map(addLength)

# Convert the transmission lines to raster.
transmissionAfricaRaster = empty.paint({
    'featureCollection': transmissionAfricaLength,
    'color': 'lengthKm'
})

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Add roads and transmission lines together into one image.
# Clip to Africa feature collection.
stack = grip4_africaRaster \
    .addBands(transmissionAfricaRaster) \
    .rename(['roads', 'transmission']) \
    .clipToCollection(Africa)

# Calculate spatial statistics: local Geary's C.
# Create a list of weights for a 9x9 kernel.
list = [1, 1, 1, 1, 1, 1, 1, 1, 1]

# The center of the kernel is zero.
centerList = [1, 1, 1, 1, 0, 1, 1, 1, 1]

# Assemble a list of lists: the 9x9 kernel weights as a 2-D matrix.
lists = [list, list, list, list, centerList, list, list, list,
    list
]

# Create the kernel from the weights.
# Non-zero weights represent the spatial neighborhood.
kernel = ee.Kernel.fixed(9, 9, lists, -4, -4, False)

# Use the max among bands as the input.
maxBands = stack.reduce(ee.Reducer.max())

# Convert the neighborhood into multiple bands.
neighs = maxBands.neighborhoodToBands(kernel)

# Compute local Geary's C, a measure of spatial association
# - 0 indicates perfect positive autocorrelation/clustered
# - 1 indicates no autocorrelation/random
# - 2 indicates perfect negative autocorrelation/dispersed
gearys = maxBands.subtract(neighs).pow(2).reduce(ee.Reducer.sum()) \
    .divide(math.pow(9, 2))

# Convert to a -/+1 scale by: calculating C* = 1 - C
# - 1 indicates perfect positive autocorrelation/clustered
# - 0 indicates no autocorrelation/random
# - -1 indicates perfect negative autocorrelation/dispersed
gearysStar = ee.Image(1).subtract(gearys)

# Import palettes.
palettes = require('users/gena/packages:palettes')

# Create custom palette, blue is negative while red is positive autocorrelation/clustered.
palette = palettes.colorbrewer.Spectral[7].reverse()

# Normalize the image and add it to the map.
visParams = {
    'min': -1,
    'max': 1,
    'palette': palette
}

# Display the image.
Map.setCenter(19.8638, -34.5705, 10)
Map.addLayer(gearysStar.focalMax(1), visParams, 'local Gearys C*')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
