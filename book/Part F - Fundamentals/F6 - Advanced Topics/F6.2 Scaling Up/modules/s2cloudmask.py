import ee 
import geemap

Map = geemap.Map()

# Functions for implementing a Sentinel II cloud mask.

# Join two collections on their 'system:index' property.
# The propertyName parameter is the name of the property
# that references the joined image.
def indexJoin(collectionA, collectionB, propertyName):
  joined = ee.ImageCollection(ee.Join.saveFirst(propertyName).apply({
    'primary': collectionA,
    'secondary': collectionB,
    'condition': ee.Filter.equals({
      'leftField': 'system:index',
      'rightField': 'system:index'})
  }))
  # Merge the bands of the joined image.

def func_oxa(image):
    return image.addBands(ee.Image(image.get(propertyName)))

  return joined.map(func_oxa)





# Aggressively mask clouds and shadows.
def maskImage(image):
  # Compute the cloud displacement index from the L1C bands.
  cdi = ee.Algorithms.Sentinel2.CDI(image)
  s2c = image.select('probability')
  cirrus = image.select('B10').multiply(0.0001)

  # Assume low-to-mid atmospheric clouds to be pixels where probability
  # is greater than 65%, and CDI is less than -0.5. For higher atmosphere
  # cirrus clouds, assume the cirrus band is greater than 0.01.
  # The final cloud mask is one or both of these conditions.
  isCloud = s2c.gt(65).And(cdi.lt(-0.5)).Or(cirrus.gt(0.01))

  # Reproject is required to perform spatial operations at 20m scale.
  # 20m scale is for speed, and assumes clouds don't require 10m precision.
  isCloud = isCloud.focal_min(3).focal_max(16)
  isCloud = isCloud.reproject({'crs': cdi.projection(), 'scale': 20})

  # Project shadows from clouds we found in the last step. This assumes we're working in
  # a UTM projection.
  shadowAzimuth = ee.Number(90) \
      .subtract(ee.Number(image.get('MEAN_SOLAR_AZIMUTH_ANGLE')))

  # With the following reproject, the shadows are projected 5km.
  isCloud = isCloud.directionalDistanceTransform(shadowAzimuth, 50)
  isCloud = isCloud.reproject({'crs': cdi.projection(), 'scale': 100})

  isCloud = isCloud.select('distance').mask()
  return image.select('B2', 'B3', 'B4').updateMask(isCloud.Not())


exports.maskImage = maskImage
exports.indexJoin = indexJoin

# LGTM (nclinton)
Map