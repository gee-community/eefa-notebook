import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.3 Built Environments
#  Checkpoint:   A13d
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
Map