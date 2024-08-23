import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F4.2 Aggregating Images for Time Series
#  Checkpoint:   F42c
#  Author:       Ujaval Gandhi
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

chirps = ee.ImageCollection("UCSB-CHG/CHIRPS/PENTAD")
year = 2019
startDate = ee.Date.fromYMD(year, 1, 1)

endDate = startDate.advance(1, "year")

yearFiltered = chirps.filter(ee.Filter.date(startDate, endDate))
print(yearFiltered, "Date-filtered CHIRPS images")

print(startDate, "Start date")
print(endDate, "End date")

print("Start date as timestamp", startDate.millis())
print("End date as timestamp", endDate.millis())

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Aggregate this time series to compute monthly images.
# Create a list of months
months = ee.List.sequence(1, 12)


# Write a function that takes a month number
# and returns a monthly image.
def createMonthlyImage(beginningMonth):
    startDate = ee.Date.fromYMD(year, beginningMonth, 1)
    endDate = startDate.advance(1, "month")
    monthFiltered = yearFiltered.filter(ee.Filter.date(startDate, endDate))

    # Calculate total precipitation.
    total = monthFiltered.reduce(ee.Reducer.sum())
    return total.set(
        {
            "system:time_start": startDate.millis(),
            "system:time_end": endDate.millis(),
            "year": year,
            "month": beginningMonth,
        }
    )


# map() the function on the list of months
# This creates a list with images for each month in the list
monthlyImages = months.map(createMonthlyImage)

# Create an ee.ImageCollection.
monthlyCollection = ee.ImageCollection.fromImages(monthlyImages)
print(monthlyCollection)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

Map
