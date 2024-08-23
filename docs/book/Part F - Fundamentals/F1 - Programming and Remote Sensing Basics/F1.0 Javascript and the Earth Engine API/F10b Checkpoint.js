//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  Chapter:      F1.0 Javascript and the Earth Engine API
//  Checkpoint:   F10b
//  Author:       Ujaval Gandhi 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

var a = 1;
var b = 2;

var result = ee.Number(a).add(b);
print(result);

var yearList = ee.List.sequence(1980, 2020, 5);
print(yearList);

//  -----------------------------------------------------------------------
//  CHECKPOINT 
//  -----------------------------------------------------------------------

