import ee 
import geemap

Map = geemap.Map()

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
geometry = ee.Geometry.MultiPoint()
#**** End of imports. If edited, may not auto-convert in the playground. ****#
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F6.0 Advanced Raster Visualization
#  Checkpoint:   F60g
#  Authors:      Gennadii Donchyts, Fedor Baart
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Include packages.
palettes = require('users/gena/packages:palettes')
text = require('users/gena/packages:text')

point =  ee.Geometry.Point([-
    106.15944300895228, -74.58262940096245
])

rect =
    ee.Geometry.Polygon(
        [
            [
                [-106.19789515738981, -74.56509549360152],
                [-106.19789515738981, -74.78071448733921],
                [-104.98115931754606, -74.78071448733921],
                [-104.98115931754606, -74.56509549360152]
            ]
        ], None, False)

# Lookup the ice palette.
palette = palettes.cmocean.Ice[7]

# Show it in the console.
palettes.showPalette('Ice', palette)

# Center map on geometry.
Map.centerObject(point, 9)

# Select S1 images for the Thwaites glacier.
images = ee.ImageCollection('COPERNICUS/S1_GRD') \
    .filterBounds(rect) \
    .filterDate('2021-01-01', '2021-03-01') \
    .select('HH') \
    .filter(ee.Filter.isContained({
        'leftValue': rect,
        'rightField': '.geo'
    })) \
    .sort('system:time_start')

# Print number of images.
print(images.size())

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map