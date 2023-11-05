import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F4.7 Interpreting Time Series with CCDC
#  Checkpoint:   F47d
#  Authors:      Paulo Arévalo, Pontus Olofsson
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

palettes = require('users/gena/packages:palettes')

resultsPath =
    'projects/gee-book/assets/F4-7/Rondonia_example_small'
ccdResults = ee.Image(resultsPath)
Map.centerObject(ccdResults, 10)
print(ccdResults)

# Display segment start and end times.
start = ccdResults.select('tStart')
end = ccdResults.select('tEnd')
Map.addLayer(start, {
    'min': 1999,
    'max': 2001
}, 'Segment start')
Map.addLayer(end, {
    'min': 2010,
    'max': 2020
}, 'Segment end')

# Find the segment that intersects a given date.
targetDate = 2005.5
selectSegment = start.lte(targetDate).And(end.gt(targetDate))
Map.addLayer(selectSegment, {}, 'Identified segment')

# Get all coefs in the SWIR1 band.
SWIR1Coefs = ccdResults.select('SWIR1_coefs')
Map.addLayer(SWIR1Coefs, {}, 'SWIR1 coefs')

# Select only those for the segment that we identified previously.
sliceStart = selectSegment.arrayArgmax().arrayFlatten([
    ['index']
])
sliceEnd = sliceStart.add(1)
selectedCoefs = SWIR1Coefs.arraySlice(0, sliceStart, sliceEnd)
Map.addLayer(selectedCoefs, {}, 'Selected SWIR1 coefs')

# Retrieve only the intercept coefficient.
intercept = selectedCoefs.arraySlice(1, 0, 1).arrayProject([1])
intVisParams = {
    'palette': palettes.matplotlib.viridis[7],
    'min': -6,
    'max': 6
}
Map.addLayer(intercept.arrayFlatten([
    ['INTP']
]), intVisParams, 'INTP_SWIR1')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

Map