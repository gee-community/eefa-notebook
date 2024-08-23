import ee
import math
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.1 Agricultural Environments
#  Checkpoint:   A11b
#  Authors:      Sherrie Wang, George Azzari
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##############################
# 1. Pull all Landsat 7 and 8 images over study area
##############################

# Define study area.
TIGER = ee.FeatureCollection('TIGER/2018/Counties')
region = ee.Feature(TIGER \
    .filter(ee.Filter.eq('STATEFP', '17')) \
    .filter(ee.Filter.eq('NAME', 'McLean')) \
    .first())
geometry = region.geometry()
Map.centerObject(region)
Map.addLayer(region, {
    'color': 'red'
}, 'McLean County')

# Import Landsat imagery.
landsat7 = ee.ImageCollection('LANDSAT/LE07/C02/T1_L2')
landsat8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')

# Functions to rename Landsat 7 and 8 images.
def renameL7(img):
    return img.rename(['BLUE', 'GREEN', 'RED', 'NIR', 'SWIR1',
        'SWIR2', 'TEMP1', 'ATMOS_OPACITY', 'QA_CLOUD',
        'ATRAN', 'CDIST',
        'DRAD', 'EMIS', 'EMSD', 'QA', 'TRAD', 'URAD',
        'QA_PIXEL',
        'QA_RADSAT'
    ])


def renameL8(img):
    return img.rename(['AEROS', 'BLUE', 'GREEN', 'RED', 'NIR',
        'SWIR1',
        'SWIR2', 'TEMP1', 'QA_AEROSOL', 'ATRAN', 'CDIST',
        'DRAD', 'EMIS',
        'EMSD', 'QA', 'TRAD', 'URAD', 'QA_PIXEL', 'QA_RADSAT'
    ])


# Functions to mask out clouds, shadows, and other unwanted features.
def addMask(img):
    # Bit 0: Fill
    # Bit 1: Dilated Cloud
    # Bit 2: Cirrus (high confidence) (L8) or unused (L7)
    # Bit 3: Cloud
    # Bit 4: Cloud Shadow
    # Bit 5: Snow
    # Bit 6: Clear
    #        0: Cloud or Dilated Cloud bits are set
    #        1: Cloud and Dilated Cloud bits are not set
    # Bit 7: Water
    clear = img.select('QA_PIXEL').bitwiseAnd(64).neq(0)
    clear = clear.updateMask(clear).rename(['pxqa_clear'])

    water = img.select('QA_PIXEL').bitwiseAnd(128).neq(0)
    water = water.updateMask(water).rename(['pxqa_water'])

    cloud_shadow = img.select('QA_PIXEL').bitwiseAnd(16).neq(0)
    cloud_shadow = cloud_shadow.updateMask(cloud_shadow).rename([
        'pxqa_cloudshadow'
    ])

    snow = img.select('QA_PIXEL').bitwiseAnd(32).neq(0)
    snow = snow.updateMask(snow).rename(['pxqa_snow'])

    masks = ee.Image.cat([
        clear, water, cloud_shadow, snow
    ])

    return img.addBands(masks)


def maskQAClear(img):
    return img.updateMask(img.select('pxqa_clear'))


# Function to add GCVI as a band.
def addVIs(img):
  gcvi = img.expression('(nir / green) - 1', {
      'nir': img.select('NIR'),
      'green': img.select('GREEN')
  }).select([0], ['GCVI'])

  return ee.Image.cat([img, gcvi])


# Define study time period.
start_date = '2020-01-01'
end_date = '2020-12-31'

# Pull Landsat 7 and 8 imagery over the study area between start and end dates.
landsat7coll = landsat7 \
    .filterBounds(geometry) \
    .filterDate(start_date, end_date) \
    .map(renameL7)

landsat8coll = landsat8 \
    .filterDate(start_date, end_date) \
    .filterBounds(geometry) \
    .map(renameL8)

# Merge Landsat 7 and 8 collections.
landsat = landsat7coll.merge(landsat8coll) \
    .sort('system:time_start')

# Mask out non-clear pixels, add VIs and time variables.
landsat = landsat.map(addMask) \
    .map(maskQAClear) \
    .map(addVIs)

# Visualize GCVI time series at one location.
point = ee.Geometry.Point([-88.81417685576481,
    40.579804398254005
])
landsatChart = ui.Chart.image.series(landsat.select('GCVI'),
        point) \
    .setChartType('ScatterChart') \
    .setOptions({
        'title': 'Landsat GCVI time series',
        'lineWidth': 1,
        'pointSize': 3,
    })
print(landsatChart)

# Get crop type dataset.
cdl = ee.Image('USDA/NASS/CDL/2020').select(['cropland'])
Map.addLayer(cdl.clip(geometry), {}, 'CDL 2020')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

##############################
# 2. Add bands for harmonics
##############################

# Function that adds time band to an image.
def addTimeUnit(image, refdate):
    date = image.date()

    dyear = date.difference(refdate, 'year')
    t = image.select(0).multiply(0).add(dyear).select([0], ['t']) \
        .float()

    imageplus = image.addBands(t)

    return imageplus


# Function that adds harmonic basis to an image.
def addHarmonics(image, omega, refdate):
    image = addTimeUnit(image, refdate)
    timeRadians = image.select('t').multiply(2 * math.pi * omega)
    timeRadians2 = image.select('t').multiply(4 * math.pi *
    omega)

    return image \
        .addBands(timeRadians.cos().rename('cos')) \
        .addBands(timeRadians.sin().rename('sin')) \
        .addBands(timeRadians2.cos().rename('cos2')) \
        .addBands(timeRadians2.sin().rename('sin2')) \
        .addBands(timeRadians.divide(timeRadians) \
            .rename('constant'))


# Apply addHarmonics to Landsat image collection.
omega = 1
landsatPlus = landsat.map(
    def function(image):
        return addHarmonics(image, omega, start_date)
    )
print('Landsat collection with harmonic basis: ', landsatPlus)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

Map
