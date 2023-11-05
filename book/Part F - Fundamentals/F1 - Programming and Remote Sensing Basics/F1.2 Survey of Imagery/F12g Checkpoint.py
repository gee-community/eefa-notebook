import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F1.2 Survey of Raster Datasets
#  Checkpoint:   F12g
#  Authors:      Andréa, Karen, Nick Clinton, David Saah
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##/
# Other datasets
##/

# Import and filter a gridded population dataset.
griddedPopulation = ee.ImageCollection(
        'CIESIN/GPWv411/GPW_Population_Count') \
    .first()

# Predefined palette.
populationPalette = [
   'ffffe7',
   '86a192',
   '509791',
   '307296',
   '2c4484',
   '000066'
]

# Center the Map.
Map.centerObject(griddedPopulation, 3)

# Add the population data to the map.
Map.addLayer(griddedPopulation,
    {
        'min': 0,
        'max': 1200,
        'palette': populationPalette
    },
    'Gridded Population')

# Import the NASA DEM Dataset.
nasaDEM = ee.Image('NASA/NASADEM_HGT/001')

# Add the elevation layer to the map.
Map.addLayer(nasaDEM, {
    'bands': ['elevation'],
    'min': 0,
    'max': 3000
}, 'NASA DEM')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map