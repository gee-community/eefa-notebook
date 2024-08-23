import ee
import geemap

Map = geemap.Map()

#
'Author': Sofia Ermida (sofia.ermida@ipma.pt; @ermida_sofia)

This code is free and open.
By using this code and any data derived with it,
you agree to cite the following reference
'in any publications derived from them':
Ermida, S.L., Soares, P., Mantas, V., Göttsche, F.-M., Trigo, I.F., 2020.
    Google Earth Engine open-source code for Land Surface Temperature estimation from the Landsat series.
    'Remote Sensing, 12 (9), 1471; https':#doi.Org/10.3390/rs12091471

This function selects the Landsat data based on user inputs
and performes the LST computation

'to call this function use':

LandsatLST = require('users/sofiaermida/landsat_smw_lst:modules/Landsat_LST.js')
LandsatCollection = LandsatLST.collection(landsat, date_start, date_end, geometry)

'USES':
    - NCEP_TPW.js
    - cloudmask.js
    - compute_NDVI.js
    - compute_FVC.js
    - compute_emissivity.js
    - SMWalgorithm.js

'INPUTS':
        '- landsat': <string>
                  the Landsat satellite id
                  'valid inputs': 'L4', 'L5', 'L7' and 'L8'
        '- date_start': <string>
                      start date of the Landsat collection
                      format: YYYY-MM-DD
        '- date_end': <string>
                    end date of the Landsat collection
                    format: YYYY-MM-DD
        '- geometry': <ee.Geometry>
                    region of interest
        '- use_ndvi': <boolean>
                if True, NDVI values are used to obtain a
                dynamic emissivity; if False, emissivity is
                obtained directly from ASTER
'OUTPUTS':
        - <ee.ImageCollection>
          'image collection with bands':
          '- landsat original bands': all from SR excpet the TIR bands (from TOA)
          - cloud masked
          - 'NDVI': normalized vegetation index
          - 'FVC': fraction of vegetation cover [0-1]
          - 'TPW': total precipitable water [mm]
          - 'EM': surface emissvity for TIR band
          - 'LST': land surface temperature

  '14-08-2020': update to avoid using the getInfo() and if()
    (Thanks Tyler Erickson for the suggestion)

  '11-07-2022': update to use collection 2
#

##############/ ATTENTION ###################
######################################/
#
# As off 11.07.2022 a new version of the code is released:
#      - update to use collection 2 data
#      - emissivities of water and snow surfaces are now prescribed
#
# the previous version of the code will still be available; the replaced code
# is commented
#
#######################################
#######################################

# MODULES DECLARATION -----------------------------------------------------------
# Total Precipitable Water
NCEP_TPW = require('users/sofiaermida/landsat_smw_lst:modules/NCEP_TPW.js')
#cloud mask
cloudmask = require('users/sofiaermida/landsat_smw_lst:modules/cloudmask.js')
#Normalized Difference Vegetation Index
NDVI = require('users/sofiaermida/landsat_smw_lst:modules/compute_NDVI.js')
#Fraction of Vegetation cover
FVC = require('users/sofiaermida/landsat_smw_lst:modules/compute_FVC.js')
#surface emissivity
EM = require('users/sofiaermida/landsat_smw_lst:modules/compute_emissivity.js')
# land surface temperature
LST = require('users/sofiaermida/landsat_smw_lst:modules/SMWalgorithm.js')
# --------------------------------------------------------------------------------

COLLECTION = ee.Dictionary({
  'L4': {
    'TOA': ee.ImageCollection('LANDSAT/LT04/C02/T1_TOA'),
    'SR': ee.ImageCollection('LANDSAT/LT04/C02/T1_L2'),
    'TIR': ['B6',],
    'VISW': ['SR_B1','SR_B2','SR_B3','SR_B4','SR_B5','SR_B7','QA_PIXEL']
  },
  'L5': {
    'TOA': ee.ImageCollection('LANDSAT/LT05/C02/T1_TOA'),
    'SR': ee.ImageCollection('LANDSAT/LT05/C02/T1_L2'),
    'TIR': ['B6',],
    'VISW': ['SR_B1','SR_B2','SR_B3','SR_B4','SR_B5','SR_B7','QA_PIXEL']
  },
  'L7': {
    'TOA': ee.ImageCollection('LANDSAT/LE07/C02/T1_TOA'),
    'SR': ee.ImageCollection('LANDSAT/LE07/C02/T1_L2'),
    'TIR': ['B6_VCID_1','B6_VCID_2'],
    'VISW': ['SR_B1','SR_B2','SR_B3','SR_B4','SR_B5','SR_B7','QA_PIXEL']
  },
  'L8': {
    'TOA': ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA'),
    'SR': ee.ImageCollection('LANDSAT/LC08/C02/T1_L2'),
    'TIR': ['B10','B11'],
    'VISW': ['SR_B1','SR_B2','SR_B3','SR_B4','SR_B5','SR_B6','SR_B7','QA_PIXEL']
  }
})

# COLLECTION 1
COLLECTION = ee.Dictionary({
  'L4': {
    'TOA': ee.ImageCollection('LANDSAT/LT04/C01/T1_TOA'),
    'SR': ee.ImageCollection('LANDSAT/LT04/C01/T1_SR'),
    'TIR': ['B6',]
  },
  'L5': {
    'TOA': ee.ImageCollection('LANDSAT/LT05/C01/T1_TOA'),
    'SR': ee.ImageCollection('LANDSAT/LT05/C01/T1_SR'),
    'TIR': ['B6',]
  },
  'L7': {
    'TOA': ee.ImageCollection('LANDSAT/LE07/C01/T1_TOA'),
    'SR': ee.ImageCollection('LANDSAT/LE07/C01/T1_SR'),
    'TIR': ['B6_VCID_1','B6_VCID_2'],
  },
  'L8': {
    'TOA': ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA'),
    'SR': ee.ImageCollection('LANDSAT/LC08/C01/T1_SR'),
    'TIR': ['B10','B11']
  }
})
#

def exports.collection(landsat, date_start, date_end, geometry, use_ndvi):

  print('!!!!! On 11-07-2022 this code has been updated to run with landsat collection 2 data !!!!!')
  # load TOA Radiance/Reflectance
  collection_dict = ee.Dictionary(COLLECTION.get(landsat))

  landsatTOA = ee.ImageCollection(collection_dict.get('TOA')) \
                .filter(ee.Filter.date(date_start, date_end)) \
                .filterBounds(geometry)
                #.map(cloudmask.toa)

  # load Surface Reflectance collection for NDVI
  landsatSR = ee.ImageCollection(collection_dict.get('SR')) \
                .filter(ee.Filter.date(date_start, date_end)) \
                .filterBounds(geometry) \
                .map(cloudmask.sr) \
                .map(NDVI.addBand(landsat)) \
                .map(FVC.addBand(landsat)) \
                .map(NCEP_TPW.addBand) \
                .map(EM.addBand(landsat,use_ndvi))

  # combine collections
  # all channels from surface reflectance collection
  # except tir channels: from TOA collection
  # select TIR bands
  tir = ee.List(collection_dict.get('TIR'))
  visw = ee.List(collection_dict.get('VISW')) \
    .add('NDVI') \
    .add('FVC') \
    .add('TPW') \
    .add('TPWpos') \
    .add('EM')
  landsatALL = (landsatSR.select(visw).combine(landsatTOA.select(tir), True))

  # compute the LST
  landsatLST = landsatALL.map(LST.addBand(landsat))

  return landsatLST

Map
