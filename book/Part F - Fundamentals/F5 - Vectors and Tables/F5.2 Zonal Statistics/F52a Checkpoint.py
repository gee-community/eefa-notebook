import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F5.2 Zonal Statistics
#  Checkpoint:   F52a
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

def func_jaw(img):
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

    results = ic.map(func_jaw
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
Map
