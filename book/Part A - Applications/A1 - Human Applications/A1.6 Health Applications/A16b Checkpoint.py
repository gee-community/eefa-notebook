import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.6 Health Applications
#  Checkpoint:   A16b
#  Author:       Dawn Nekorchuk
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Section 1: Data Import
woredas = ee.FeatureCollection("projects/gee-book/assets/A1-6/amhara_woreda_20170207")
# Create region outer boundary to filter products on.
amhara = woredas.geometry().bounds()
gpm = ee.ImageCollection("NASA/GPM_L3/IMERG_V06")
LSTTerra8 = ee.ImageCollection("MODIS/061/MOD11A2").filterDate("2001-06-26", Date.now())
brdfReflect = ee.ImageCollection("MODIS/006/MCD43A4")
brdfQa = ee.ImageCollection("MODIS/006/MCD43A2")

# Visualize woredas with black borders and no fill.
# Create an empty image into which to paint the features, cast to byte.
empty = ee.Image().byte()
# Paint all the polygon edges with the same number and width.
outline = empty.paint({"featureCollection": woredas, "color": 1, "width": 1})
# Add woreda boundaries to the map.
Map.setCenter(38, 11.5, 7)
Map.addLayer(outline, {"palette": "000000"}, "Woredas")

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------

# Section 2: Handling of dates

# 2.1 Requested start and end dates.
reqStartDate = ee.Date("2021-10-01")
reqEndDate = ee.Date("2021-11-30")

# 2.2 LST Dates
# LST MODIS is every 8 days, and a user-requested date will likely not match.
# We want to get the latest previous image date,
#  i.e. the date the closest, but prior to, the requested date.
# We will filter later.
# Get date of first image.
LSTEarliestDate = LSTTerra8.first().date()
# Filter collection to dates from beginning to requested start date.
priorLstImgCol = LSTTerra8.filterDate(LSTEarliestDate, reqStartDate)
# Get the latest (max) date of this collection of earlier images.
LSTPrevMax = priorLstImgCol.reduceColumns(
    {"reducer": ee.Reducer.max(), "selectors": ["system:time_start"]}
)
LSTStartDate = ee.Date(LSTPrevMax.get("max"))
print("LSTStartDate", LSTStartDate)

# 2.3 Last available data dates
# Different variables have different data lags.
# Data may not be available in user range.
# To prevent errors from stopping script,
#  grab last available (if relevant) & filter at end.

# 2.3.1 Precipitation
# Calculate date of most recent measurement for gpm (of all time).
gpmAllMax = gpm.reduceColumns(ee.Reducer.max(), ["system:time_start"])
gpmAllEndDateTime = ee.Date(gpmAllMax.get("max"))
# GPM every 30 minutes, so get just date part.
gpmAllEndDate = ee.Date.fromYMD(
    {
        "year": gpmAllEndDateTime.get("year"),
        "month": gpmAllEndDateTime.get("month"),
        "day": gpmAllEndDateTime.get("day"),
    }
)

# If data ends before requested start, take last data date,
# otherwise use requested date.
precipStartDate = ee.Date(gpmAllEndDate.millis().min(reqStartDate.millis()))
print("precipStartDate", precipStartDate)

# 2.3.2 BRDF
# Calculate date of most recent measurement for brdf (of all time).
brdfAllMax = brdfReflect.reduceColumns(
    {"reducer": ee.Reducer.max(), "selectors": ["system:time_start"]}
)
brdfAllEndDate = ee.Date(brdfAllMax.get("max"))
# If data ends before requested start, take last data date,
# otherwise use the requested date.
brdfStartDate = ee.Date(brdfAllEndDate.millis().min(reqStartDate.millis()))
print("brdfStartDate", brdfStartDate)
print("brdfEndDate", brdfAllEndDate)

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map
