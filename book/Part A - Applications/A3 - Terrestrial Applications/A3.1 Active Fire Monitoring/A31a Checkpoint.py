import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A3.1 Active fire monitoring
#  Checkpoint:   A31a
#  Authors:      Morgan A. Crowley* and Tianjia Liu* (*shared first-authorship)
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
  We will use the Bobcat Fire as an example in this practicum.

  Bobcat Fire, Los Angeles County, CA
  'Ignition': Sep 6, 2020
  'Total burned area': 115796 acres
  'Lon': -117.868 W, 'Lat': 34.241 N
  'https':#inciweb.nwcg.gov/incident/7152/
#

# --------
# Inputs
# --------

# Define the location of the fire.
lon = -117.868
lat = 34.241
zoom = 9

# Filter datasets to a specific date range:
# start date of fire.
inYear = 2020
inMonth = 9
inDay = 6

durationAF = 15; # in days
durationBA = 1; # in months

# Date range for active fires.
startDateAF = ee.Date.fromYMD(inYear, inMonth, inDay)
endDateAF = startDateAF.advance(durationAF, 'day')

# Date range for burned area.
startDateBA = ee.Date.fromYMD(inYear, inMonth, 1)
endDateBA = startDateBA.advance(durationBA, 'month')

# -------------------------------
# 1. Reference Perimeter (WFIGS)
# -------------------------------
# Note: each fire has multiple versions, so here we are
# filtering WFIGS by the name of the fire, sorting the
# area of the filtered polygons in descending order,
# and retrieving the polygon with the highest area.
WFIGS = ee.FeatureCollection(
    'projects/gee-book/assets/A3-1/WFIGS')
reference = ee.Feature(WFIGS.filter(ee.Filter.eq('irwin_In_1',
        'BOBCAT')) \
    .sort('poly_Acres', False).first())

# -------------------------------
# 2. MODIS active fire datasets
# -------------------------------
# MOD14A1, MYD14A1 = MODIS/Terra and Aqua active fires and thermal anomalies
# resolution: daily, gridded at 1km in sinusoidal projection (SR-ORG:6974)
# variables: fire mask (FireMask), fire radiative power in MW (MaxFRP)
# satellite overpasses: Terra (10:30am/pm local time), Aqua (1:30am/pm local time)

# Define the Earth Engine paths for MOD14A1 and MYD14A1, collection 6.
mod14a1 = ee.ImageCollection('MODIS/006/MOD14A1')
myd14a1 = ee.ImageCollection('MODIS/006/MYD14A1')

# Filter the datasets according to the date range.
mod14a1Img = mod14a1.filterDate(startDateAF, endDateAF)
myd14a1Img = myd14a1.filterDate(startDateAF, endDateAF)

def getFireMask(image):
    # Fire Mask (FireMask): values ≥ 7 are active fire pixels
    return image.select('FireMask').gte(7)


def getMaxFRP(image):
    # FRP (MaxFRP): MaxFRP needs to be scaled by 0.1 to be in units of MW.
    return image.select('MaxFRP').multiply(0.1)


# Define the active fire mask (count of active fire pixels).
mod14a1ImgMask = mod14a1Img.map(getFireMask).sum()
myd14a1ImgMask = myd14a1Img.map(getFireMask).sum()

# Define the total FRP (MW).
mod14a1ImgFrp = mod14a1Img.map(getMaxFRP).sum()
myd14a1ImgFrp = myd14a1Img.map(getMaxFRP).sum()

# ------------------------------
# 3. MODIS burned area dataset
# ------------------------------
# MCD64A1 = MODIS/Terra and Aqua combined burned area
# resolution: monthly, gridded at 500m in sinusoidal projection (SR-ORG:6974),
# can be disaggregated to daily resolution
# variables: burn date as day of year (BurnDate)

# Define the Earth Engine paths for MCD64A1, collection 6.
mcd64a1 = ee.ImageCollection('MODIS/006/MCD64A1')

def getBurnDate(image):
    # burn day of year (BurnDate)
    return image.select('BurnDate')


# Define the burned area mask.
mcd64a1Img = mcd64a1.filterDate(startDateBA, endDateBA)
mcd64a1ImgMask = mcd64a1Img.map(getBurnDate).min()

# ------------------------------
# 4. GOES 16/17 active fires
# ------------------------------
# GOES-16/17 - geostationary satellites over North/South America
# resolution: every 10-30 minutes, 2 km
# variables: fire mask (Mask), FRP (Power)

# Define the Earth Engine paths for GOES-16/17.
goes16 = ee.ImageCollection('NOAA/GOES/16/FDCF')
goes17 = ee.ImageCollection('NOAA/GOES/17/FDCF')

filterGOES = ee.Filter.calendarRange(0, 0, 'minute')

# Filter the datasets according to the date range.
goes16Img = goes16.filterDate(startDateAF, endDateAF) \
    .filter(filterGOES)
goes17Img = goes17.filterDate(startDateAF, endDateAF) \
    .filter(filterGOES)

def getFireMask(image):
    # fire mask (Mask): values from 10-35 are active fire pixels,
    # see the description for QA values to filter out low confidence fires
    return image.select('Mask').gte(10).And(image.select('Mask') \
        .lte(35))


def getFRP(image):
    # FRP (Power), in MW
    return image.select('Power')


# Define the active fire mask (count of active fire pixels).
goes16ImgMask = goes16Img.map(getFireMask).sum()
goes17ImgMask = goes17Img.map(getFireMask).sum()

# Define the total FRP (MW).
goes16ImgFrp = goes16Img.map(getFRP).sum()
goes17ImgFrp = goes17Img.map(getFRP).sum()

# -------------------------------
# 5. Map Visualization - Layers
# -------------------------------
# Use the 'Layers' dropdown menu on the map panel to toggle on and off layers.
Map.addLayer(mod14a1ImgMask.selfMask(), {
    'palette': 'orange'
}, 'MOD14A1')
Map.addLayer(myd14a1ImgMask.selfMask(), {
    'palette': 'red'
}, 'MYD14A1')

Map.addLayer(mcd64a1ImgMask.selfMask(), {
    'palette': 'black'
}, 'MCD64A1')

Map.addLayer(goes16ImgMask.selfMask(), {
    'palette': 'skyblue'
}, 'GOES16', False)
Map.addLayer(goes17ImgMask.selfMask(), {
    'palette': 'purple'
}, 'GOES17', False)

Map.setCenter(lon, lat, zoom)

# ------------------------------------
# 6. Map Visualization - Panel Layout
# ------------------------------------

# Define the panel layout.
panelNames = [
    'MODIS active fires', # panel 0 - top left
    'MODIS burned area', # panel 1 - bottom left
    'GOES active fires', # panel 2 - top right
    'Reference' # panel 3 - bottom right
]

# Create a map for each visualization option.
maps = []
panelNames.forEach(function(name, index) {
    map = ui.Map()
    map.setControlVisibility({
        'fullscreenControl': False
    })

    if (index === 0) {
        map.addLayer(mod14a1ImgMask.selfMask(), {
            'palette': 'orange'
        }, 'MOD14A1')
        map.addLayer(myd14a1ImgMask.selfMask(), {
            'palette': 'red'
        }, 'MYD14A1')
        map.add(ui.Label(panelNames[0], {
            'fontWeight': 'bold',
            'position': 'bottom-left'
        }))
    }
    if (index == 1) {
        map.addLayer(mcd64a1ImgMask.selfMask(), {
            'palette': 'black'
        }, 'MCD64A1')
        map.add(ui.Label(panelNames[1], {
            'fontWeight': 'bold',
            'position': 'bottom-left'
        }))
    }
    if (index == 2) {
        map.addLayer(goes16ImgMask.selfMask(), {
            'palette': 'skyblue'
        }, 'GOES16')
        map.addLayer(goes17ImgMask.selfMask(), {
            'palette': 'purple'
        }, 'GOES17')
        map.add(ui.Label(panelNames[2], {
            'fontWeight': 'bold',
            'position': 'bottom-left'
        }))
    }
    if (index == 3) {
        map.addLayer(reference, {}, 'Reference')
        map.add(ui.Label(panelNames[3], {
            'fontWeight': 'bold',
            'position': 'bottom-left'
        }))
    }
    maps.push(map)
})

linker = ui.Map.Linker(maps)

# Make a label for the main title of the app.
title = ui.Label(
    'Visualizing Fire Datasets in Google Earth Engine', {
        'stretch': 'horizontal',
        'textAlign': 'center',
        'fontWeight': 'bold',
        'fontSize': '24px'
    })

# Define a map grid of 2x2 sub panels.
mapGrid = ui.Panel(
    [
        ui.Panel([maps[0], maps[1]], None, {
            'stretch': 'both'
        }),
        ui.Panel([maps[2], maps[3]], None, {
            'stretch': 'both'
        })
    ],
    ui.Panel.Layout.Flow('horizontal'), {
        'stretch': 'both'
    }
)
maps[0].setCenter(lon, lat, zoom)

# Add the maps and title to the ui.root().
ui.root.widgets().reset([title, mapGrid])
ui.root.setLayout(ui.Panel.Layout.Flow('vertical'))

# -----------------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------------
Map
