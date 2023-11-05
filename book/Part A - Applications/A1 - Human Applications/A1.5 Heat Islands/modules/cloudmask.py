import ee 
import geemap

Map = geemap.Map()

#
'Author': Sofia Ermida (sofia.ermida@ipma.pt; @ermida_sofia)

this function mask clouds and cloud shadow using the Quality band

'to call this function use':

cloudmask = require('users/sofiaermida/landsat_smw_lst:modules/cloudmask.js')
TOAImageMasked = cloudmask.toa(image)
SRImageMasked = cloudmask.sr(image)
or
TOAcollectionMasked = ImageCollection.map(cloudmask.toa)
SRcollectionMasked = ImageCollection.map(cloudmask.sr)


'INPUTS':
        '- image': <ee.Image>
                image for which clouds are masked
'OUTPUTS':
        - <ee.Image>
          the input image with updated mask

  '11-07-2022': update to use collection 2
#

# cloudmask for TOA data
def exports.toa(image):
  qa = image.select('QA_PIXEL')
  mask = qa.bitwiseAnd(1 << 3)
  return image.updateMask(mask.Not())


# cloudmask for SR data
def exports.sr(image):
  qa = image.select('QA_PIXEL')
  mask = qa.bitwiseAnd(1 << 3) \
    .Or(qa.bitwiseAnd(1 << 4))
  return image.updateMask(mask.Not())


# COLLECTION 1
# cloudmask for TOA data
def exports.toa(image):
  qa = image.select('BQA')
  mask = qa.bitwiseAnd(1 << 4).eq(0)
  return image.updateMask(mask)


# cloudmask for SR data
def exports.sr(image):
  qa = image.select('pixel_qa')
  mask = qa.bitwiseAnd(1 << 3) \
    .Or(qa.bitwiseAnd(1 << 5))
  return image.updateMask(mask.Not())

#
Map