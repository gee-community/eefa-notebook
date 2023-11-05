import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F6.0 Advanced Raster Visualization
#  Checkpoint:   F60a
#  Authors:      Gennadii Donchyts, Fedor Baart
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load the ERA5 reanalysis monthly means.
era5 = ee.ImageCollection('ECMWF/ERA5_LAND/MONTHLY')

# Load the palettes package.
palettes = require('users/gena/packages:palettes')

# Select temperature near ground.
era5 = era5.select('temperature_2m')

# Choose a diverging colormap for anomalies.
balancePalette = palettes.cmocean.Balance[7]
threeColorPalette = ['blue', 'white', 'red']

# Show the palette in the Inspector window.
palettes.showPalette('temperature anomaly', balancePalette)
palettes.showPalette('temperature anomaly', threeColorPalette)

# Select 2 time windows of 10 years.
era5_1980 = era5.filterDate('1981-01-01', '1991-01-01').mean()
era5_2010 = era5.filterDate('2011-01-01', '2020-01-01').mean()

# Compute the temperature change.
era5_diff = era5_2010.subtract(era5_1980)

# Show it on the map.
Map.addLayer(era5_diff, {
    'palette': threeColorPalette,
    'min': -2,
    'max': 2
}, 'Blue White Red palette')

Map.addLayer(era5_diff, {
    'palette': balancePalette,
    'min': -2,
    'max': 2
}, 'Balance palette')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map