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

This function applies a vegetation cover correction to ASTER emissivity
in order to obtain a bare ground emissivity component at each pixel

'to call this function use':

ASTERGED = require('users/sofiaermida/landsat_smw_lst:modules/ASTER_bare_emiss.js')
bare_ground_emiss = ASTERGED.emiss_bare_bandXX(image)
or
ImageCollectionwithASTER = ImageCollection.map(ASTERGED.emiss_bare_bandXX)

with XX = band number

'INPUTS':
        '- image': <ee.Image>
                  an image is required to clip the ASTER data
                  to the image geometry; using the full ASTER image
                  compromises the performance
'OUTPUTS':
        - <ee.Image>
          bare ground emissivity of band XX
#


# get ASTER emissivity
aster = ee.Image("NASA/ASTER_GED/AG100_003")

#get ASTER FVC from NDVI
aster_ndvi = aster.select('ndvi').multiply(0.01)

aster_fvc = aster_ndvi.expression('((ndvi-ndvi_bg)/(ndvi_vg - ndvi_bg))**2',
  {'ndvi':aster_ndvi,'ndvi_bg':0.2,'ndvi_vg':0.86})
aster_fvc = aster_fvc.where(aster_fvc.lt(0.0),0.0)
aster_fvc = aster_fvc.where(aster_fvc.gt(1.0),1.0)

# bare ground emissivity functions for each band
def exports.emiss_bare_band10(image):
  return image.expression('(EM - 0.99*fvc)/(1.0-fvc)',{
    'EM':aster.select('emissivity_band10').multiply(0.001),
    'fvc':aster_fvc}) \
    .clip(image.geometry())


def exports.emiss_bare_band11(image):
  return image.expression('(EM - 0.99*fvc)/(1.0-fvc)',{
    'EM':aster.select('emissivity_band11').multiply(0.001),
    'fvc':aster_fvc}) \
    .clip(image.geometry())


def exports.emiss_bare_band12(image):
  return image.expression('(EM - 0.99*fvc)/(1.0-fvc)',{
    'EM':aster.select('emissivity_band12').multiply(0.001),
    'fvc':aster_fvc}) \
    .clip(image.geometry())


def exports.emiss_bare_band13(image):
  return image.expression('(EM - 0.99*fvc)/(1.0-fvc)',{
    'EM':aster.select('emissivity_band13').multiply(0.001),
    'fvc':aster_fvc}) \
    .clip(image.geometry())


def exports.emiss_bare_band14(image):
  return image.expression('(EM - 0.99*fvc)/(1.0-fvc)',{
    'EM':aster.select('emissivity_band14').multiply(0.001),
    'fvc':aster_fvc}) \
    .clip(image.geometry())

Map