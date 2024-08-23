import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F4.2 Aggregating Images for Time Series
#  Checkpoint:   F42a
#  Author:       Ujaval Gandhi
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

chirps = ee.ImageCollection("UCSB-CHG/CHIRPS/PENTAD")
startDate = "2019-01-01"
endDate = "2020-01-01"
yearFiltered = chirps.filter(ee.Filter.date(startDate, endDate))

print(yearFiltered, "Date-filtered CHIRPS images")


#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------


Map
