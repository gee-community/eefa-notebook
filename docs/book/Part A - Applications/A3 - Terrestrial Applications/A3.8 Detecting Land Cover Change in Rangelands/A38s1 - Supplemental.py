import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A3.8 Detecting Land Cover Change in Rangelands
#  Section:      Section 3 (A38s1 - Supplemental)
#  Authors:      G.R.H. Allington, N. Kreitzer
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# This code chunk demonstrates how to generate an Image Collection from
# a multi-band Image. In this case each band in the Image represents a year.

# Load the shapefile asset for the AOI as a Feature Collection.
aoi = ee.FeatureCollection(
    'projects/gee-book/assets/A3-8/GEE_Ch_AOI')
# Load the multi-band Image of fitted residual greenness values.
fittedStack = ee.Image('projects/gee-book/assets/A3-8/FR_stack')

startYear_Num = 1985
endYear_Num   = 2019
numYears = endYear_Num - startYear_Num
startMonth = '-01-01'
endMonth = '-12-31'

# Convert the multi-band Image to a List

fittedStackList = ee.List([])
  for year in range(startYear_Num, , 1):
  selBand = (fittedStack.select('fittedResidual_' + year.toString()).rename('FR'))
  selImg = ee.Image(selBand)
  nextYear = year + 1
  system_time_start = ee.Date(year.toString() + startMonth).millis()
  system_time_end = ee.Date(nextYear.toString() + startMonth).millis()
  system_index = year - startYear_Num + 1
  selImg = selImg \
      .set('year', year) \
      .set('system:time_start', system_time_start) \
      .set('system:time_end', system_time_end) \
      .set('system:index', system_index.toString())
  fittedStackList = fittedStackList.add(selImg)



fittedresidColl = ee.ImageCollection(fittedStackList)

# You will need to export this to an Asset if you want to call it in a separate script.
Map