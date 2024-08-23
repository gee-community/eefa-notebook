import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F6.0 Advanced Raster Visualization
#  Checkpoint:   F60j
#  Authors:      Gennadii Donchyts, Fedor Baart
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

dem = ee.Image('AHN/AHN2_05M_RUW')

# Change map style to HYBRID and center map on the Netherlands
Map.setOptions('HYBRID')
Map.setCenter(4.4082, 52.1775, 18)

# Visualize DEM using black-white color palette
palette = ['black', 'white']
demRGB = dem.visualize(**{
    'min': -5,
    'max': 5,
    'palette': palette
})
Map.addLayer(demRGB, {}, 'DEM')

utils = require('users/gena/packages:utils')

weight =
    0.4; # Weight of Hillshade vs RGB (0 - flat, 1 - hillshaded).
exaggeration = 5; # Vertical exaggeration.
azimuth = 315; # Sun azimuth.
zenith = 20; # Sun elevation.
brightness = -0.05; # 0 - default.
contrast = 0.05; # 0 - default.
saturation = 0.8; # 1 - default.
castShadows = False

rgb = utils.hillshadeRGB(
    demRGB, dem, weight, exaggeration, azimuth, zenith,
    contrast, brightness, saturation, castShadows)

Map.addLayer(rgb, {}, 'DEM (no shadows)')

castShadows = True

rgb = utils.hillshadeRGB(
    demRGB, dem, weight, exaggeration, azimuth, zenith,
    contrast, brightness, saturation, castShadows)

Map.addLayer(rgb, {}, 'DEM (with shadows)')

palettes = require('users/gena/packages:palettes')
palette = palettes.crameri.oleron[50]

demRGB = dem.visualize(**{'min': -5, 'max': 5, 'palette': palette})

castShadows = True

rgb = utils.hillshadeRGB(
  demRGB, dem, weight, exaggeration, azimuth, zenith,
  contrast, brightness, saturation, castShadows)

Map.addLayer(rgb, {}, 'DEM colormap')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
