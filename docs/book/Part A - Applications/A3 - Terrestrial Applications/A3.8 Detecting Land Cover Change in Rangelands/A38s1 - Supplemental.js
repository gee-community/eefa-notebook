//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  Chapter:      A3.8 Detecting Land Cover Change in Rangelands
//  Section:      Section 3 (A38s1 - Supplemental)
//  Authors:      G.R.H. Allington, N. Kreitzer
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

// This code chunk demonstrates how to generate an Image Collection from
// a multi-band Image. In this case each band in the Image represents a year.

// Load the shapefile asset for the AOI as a Feature Collection.
var aoi = ee.FeatureCollection(
    'projects/gee-book/assets/A3-8/GEE_Ch_AOI');
// Load the multi-band Image of fitted residual greenness values.
var fittedStack = ee.Image('projects/gee-book/assets/A3-8/FR_stack');

var startYear_Num = 1985; 
var endYear_Num   = 2019; 
var numYears = endYear_Num - startYear_Num;
var startMonth = '-01-01';  
var endMonth = '-12-31';  

// Convert the multi-band Image to a List

var fittedStackList = ee.List([]);
  for (var year = startYear_Num; year <= endYear_Num ; year++) {  
  var selBand = (fittedStack.select('fittedResidual_' + year.toString()).rename('FR'));
  var selImg = ee.Image(selBand);
  var nextYear = year + 1;
  var system_time_start = ee.Date(year.toString() + startMonth).millis();
  var system_time_end = ee.Date(nextYear.toString() + startMonth).millis();
  var system_index = year - startYear_Num + 1;
  selImg = selImg
      .set('year', year)
      .set('system:time_start', system_time_start)
      .set('system:time_end', system_time_end)
      .set('system:index', system_index.toString());
  fittedStackList = fittedStackList.add(selImg);
}


var fittedresidColl = ee.ImageCollection(fittedStackList);

// You will need to export this to an Asset if you want to call it in a separate script.
