import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F5.2 Zonal Statistics
#  Checkpoint:   F52b
#  Authors:      Sara Winsemius and Justin Braaten
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Functions that the rest of the chapter is based on.

# Returns a function for adding a buffer to points and optionally transforming
# to rectangular bounds
def bufferPoints(radius, bounds):
    return function(pt) {
        pt = ee.Feature(pt)
        'return bounds ? pt.buffer(radius).bounds()' : pt.buffer(
            radius)
    }


# Reduces images in an ImageCollection by regions defined in a
# FeatureCollection. Similar to mapping reduceRegions over an ImageCollection,
# but breaks the task up a bit more and includes parameters for managing
# property names.
def zonalStats(ic, fc, params):
    # Initialize internal params dictionary.
    _params = {
        'reducer': ee.Reducer.mean(),
        'scale': None,
        'crs': None,
        'bands': None,
        'bandsRename': None,
        'imgProps': None,
        'imgPropsRename': None,
        'datetimeName': 'datetime',
        'datetimeFormat': 'YYYY-MM-dd HH:'mm':ss'
    }

    # Replace initialized params with provided params.
    if (params) {
        for param in params:
            _params[param] = params[param] || _params[param]

    }

    # Set default parameters based on an image representative.
    imgRep = ic.first()
    nonSystemImgProps = ee.Feature(None) \
        .copyProperties(imgRep).propertyNames()
    if (!_params.bands) _params.bands = imgRep.bandNames()
    if (!_params.bandsRename) _params.bandsRename = _params.bands
    if (!_params.imgProps) _params.imgProps = nonSystemImgProps
    if (!_params.imgPropsRename) _params.imgPropsRename = _params \
        .imgProps

    # Map the reduceRegions function over the image collection.

def func_fpj(img):
        # Select bands (optionally rename), set a datetime & timestamp property.
        img = ee.Image(img.select(_params.bands, _params \
                .bandsRename)) \
            .set(_params.datetimeName, img.date().format(
                _params.datetimeFormat)) \
            .set('timestamp', img.get('system:time_start'))

        # Define final image property dictionary to set in output features.
        propsFrom = ee.List(_params.imgProps) \
            .cat(ee.List([_params.datetimeName,
            'timestamp']))
        propsTo = ee.List(_params.imgPropsRename) \
            .cat(ee.List([_params.datetimeName,
            'timestamp']))
        imgProps = img.toDictionary(propsFrom).rename(
            propsFrom, propsTo)

        # Subset points that intersect the given image.
        fcSub = fc.filterBounds(img.geometry())

        # Reduce the image by regions.
        return img.reduceRegions({
                'collection': fcSub,
                'reducer': _params.reducer,
                'scale': _params.scale,
                'crs': _params.crs
            }) \
            .map(function(f) {
                return f.set(imgProps)
            })

        # Converts the feature collection of feature collections to a single
        #feature collection.

    results = ic.map(func_fpj
).flatten()



































).flatten()

    return results


# Creating points that will be used for the rest of the chapter.
# Alternatively, you could load your own points.
pts = ee.FeatureCollection([
    ee.Feature(ee.Geometry.Point([-118.6010, 37.0777]), {
        'plot_id': 1
    }),
    ee.Feature(ee.Geometry.Point([-118.5896, 37.0778]), {
        'plot_id': 2
    }),
    ee.Feature(ee.Geometry.Point([-118.5842, 37.0805]), {
        'plot_id': 3
    }),
    ee.Feature(ee.Geometry.Point([-118.5994, 37.0936]), {
        'plot_id': 4
    }),
    ee.Feature(ee.Geometry.Point([-118.5861, 37.0567]), {
        'plot_id': 5
    })
])

print('Points of interest', pts)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Example 1: Topographic variables

# Buffer the points.
ptsTopo = pts.map(bufferPoints(45, False))

# Import the MERIT global elevation dataset.
elev = ee.Image('MERIT/DEM/v1_0_3')

# Calculate slope from the DEM.
slope = ee.Terrain.slope(elev)

# Concatenate elevation and slope as two bands of an image.
topo = ee.Image.cat(elev, slope)
    # Computed images do not have a 'system:time_start' property; add one based \
    .set('system:time_start', ee.Date('2000-01-01').millis())

# Wrap the single image in an ImageCollection for use in the
# zonalStats function.
topoCol = ee.ImageCollection([topo])

# Define parameters for the zonalStats function.
params = {
    'bands': [0, 1],
    'bandsRename': ['elevation', 'slope']
}

# Extract zonal statistics per point per image.
ptsTopoStats = zonalStats(topoCol, ptsTopo, params)
print('Topo zonal stats table', ptsTopoStats)

# Display the layers on the map.
Map.setCenter(-118.5957, 37.0775, 13)
Map.addLayer(topoCol.select(0), {
    'min': 2400,
    'max': 4200
}, 'Elevation')
Map.addLayer(topoCol.select(1), {
    'min': 0,
    'max': 60
}, 'Slope')
Map.addLayer(pts, {
    'color': 'purple'
}, 'Points')
Map.addLayer(ptsTopo, {
    'color': 'yellow'
}, 'Points w/ buffer')


########################################

# Example 2: MODIS

ptsModis = pts.map(bufferPoints(50, True))

# Load MODIS time series
modisCol = ee.ImageCollection('MODIS/006/MOD09A1') \
    .filterDate('2015-01-01', '2020-01-01') \
    .filter(ee.Filter.calendarRange(183, 245, 'DAY_OF_YEAR'))

# Define parameters for the zonalStats function.
params = {
    'reducer': ee.Reducer.median(),
    'scale': 500,
    'crs': 'EPSG:5070',
    'bands': ['sur_refl_b01', 'sur_refl_b02', 'sur_refl_b06'],
    'bandsRename': ['modis_red', 'modis_nir', 'modis_swir'],
    'datetimeName': 'date',
    'datetimeFormat': 'YYYY-MM-dd'
}

# Extract zonal statistics per point per image.
ptsModisStats = zonalStats(modisCol, ptsModis, params)
print('Limited MODIS zonal stats table', ptsModisStats.limit(50))

########################################

# Example 3: Landsat timeseries

# Mask clouds from images and apply scaling factors.
def maskScale(img):
    qaMask = img.select('QA_PIXEL').bitwiseAnd(parseInt('11111',
        2)).eq(0)
    saturationMask = img.select('QA_RADSAT').eq(0)

    # Apply the scaling factors to the appropriate bands.
    def getFactorImg(factorNames):
        factorList = img.toDictionary().select(factorNames) \
            .values()
        return ee.Image.constant(factorList)

    scaleImg = getFactorImg(['REFLECTANCE_MULT_BAND_.'])
    offsetImg = getFactorImg(['REFLECTANCE_ADD_BAND_.'])
    scaled = img.select('SR_B.').multiply(scaleImg).add(
    offsetImg)

    # Replace the original bands with the scaled ones and apply the masks.
    return img.addBands(scaled, None, True) \
        .updateMask(qaMask) \
        .updateMask(saturationMask)


# Selects and renames bands of interest for Landsat OLI.
def renameOli(img):
    return img.select(
        ['SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
        ['Blue', 'Green', 'Red', 'NIR', 'SWIR1', 'SWIR2'])


# Selects and renames bands of interest for TM/ETM+.
def renameEtm(img):
    return img.select(
        ['SR_B1', 'SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B7'],
        ['Blue', 'Green', 'Red', 'NIR', 'SWIR1', 'SWIR2'])


# Prepares (cloud masks and renames) OLI images.
def prepOli(img):
    img = maskScale(img)
    img = renameOli(img)
    return img


# Prepares (cloud masks and renames) TM/ETM+ images.
def prepEtm(img):
    img = maskScale(img)
    img = renameEtm(img)
    return img


ptsLandsat = pts.map(bufferPoints(15, True))

oliCol = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') \
    .filterBounds(ptsLandsat) \
    .map(prepOli)

etmCol = ee.ImageCollection('LANDSAT/LE07/C02/T1_L2') \
    .filterBounds(ptsLandsat) \
    .map(prepEtm)

tmCol = ee.ImageCollection('LANDSAT/LT05/C02/T1_L2') \
    .filterBounds(ptsLandsat) \
    .map(prepEtm)

# Merge the sensor collections
landsatCol = oliCol.merge(etmCol).merge(tmCol)

# Define parameters for the zonalStats function.
params = {
    'reducer': ee.Reducer.max(),
    'scale': 30,
    'crs': 'EPSG:5070',
    'bands': ['Blue', 'Green', 'Red', 'NIR', 'SWIR1', 'SWIR2'],
    'bandsRename': ['ls_blue', 'ls_green', 'ls_red', 'ls_nir',
        'ls_swir1', 'ls_swir2'
    ],
    'imgProps': ['SENSOR_ID', 'SPACECRAFT_ID'],
    'imgPropsRename': ['img_id', 'satellite'],
    'datetimeName': 'date',
    'datetimeFormat': 'YYYY-MM-dd'
}

# Extract zonal statistics per point per image.
ptsLandsatStats = zonalStats(landsatCol, ptsLandsat, params) \
    .filter(ee.Filter.NotNull(params.bandsRename))
print('Limited Landsat zonal stats table', ptsLandsatStats.limit(50))

Export.table.toAsset({
    'collection': ptsLandsatStats,
    'description': 'EEFA_export_Landsat_to_points',
    'assetId': 'EEFA_export_values_to_points'
})

Export.table.toDrive({
    'collection': ptsLandsatStats,
    'folder': 'EEFA_outputs', # this will create a new folder if it doesn't exist
    'description': 'EEFA_export_values_to_points',
    'fileFormat': 'CSV'
})

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------




Map
