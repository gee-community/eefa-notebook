import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A2.5 Water Balance and Drought
#  Checkpoint:   A25s4
#  Author:       Ate Poortinga, Quyen Nguyen, Nyein Soe Thwal, Andréa Puzzi Nicolau
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import the Lower Mekong boundary.
mekongBasin = ee.FeatureCollection(
    'projects/gee-book/assets/A2-5/lowerMekongBasin')

Map.centerObject(mekongBasin, 6)

classStruct = {
    'unknown': {
        'number': 0,
        'color': '6f6f6f'
    },
    'surface water': {
        'number': 1,
        'color': 'aec3d4'
    },
    'snow and ice': {
        'number': 2,
        'color': 'b1f9ff'
    },
    'mangroves': {
        'number': 3,
        'color': '111149'
    },
    'flooded forest': {
        'number': 4,
        'color': '287463'
    },
    'Deciduous forest': {
        'number': 5,
        'color': '152106'
    },
    'Orchard or plantation forest': {
        'number': 6,
        'color': 'c3aa69'
    },
    'evergreen Broadleaf': {
        'number': 7,
        'color': '7db087'
    },
    'mixed forest': {
        'number': 8,
        'color': '387242'
    },
    'urban and built up': {
        'number': 9,
        'color': 'cc0013'
    },
    'cropland': {
        'number': 10,
        'color': '8dc33b'
    },
    'rice': {
        'number': 11,
        'color': 'ffff00'
    },
    'mining': {
        'number': 12,
        'color': 'cec2a5'
    },
    'barren': {
        'number': 13,
        'color': '674c06'
    },
    'wetlands': {
        'number': 14,
        'color': '3bc3b2'
    },
    'grassland': {
        'number': 15,
        'color': 'f4a460'
    },
    'shrubland': {
        'number': 16,
        'color': '800080'
    },
    'aquaculture': {
        'number': 17,
        'color': '51768e'
    }
}

# Function to get a list of ids (keys) from a structure.
def getIds(struct):
    return Object.keys(struct)


# Function to replace spaces with underscores in a list of strings.
def cleanList(list):

def func_nzj(name):
        return name.replace(/\s+/g, '_')

    return list.map(func_nzj)





# Function to get a list of column values from a structure.
def getList(struct, column):

def func_dkz(k):
        value = struct[k][column]
        return value

    return Object.keys(struct).map(func_dkz)






classNamesList = getIds(classStruct)
probNames = cleanList(classNamesList)
classNames = ee.List(classNamesList)
classNumbers = getList(classStruct, 'number')
paletteList = getList(classStruct, 'color')
PALETTE = paletteList.join(',')

# JSON dictionary that defines piechart colors based on the
# landcover class palette.
# https:#developers.google.com/chart/interactive/docs/gallery/piechart
colors = []
for i in range(0, paletteList.length, 1):
    colors.push({
        'color': '_'.replace('_', paletteList[i])
    })


# Set start and end years.
startYear = 2010
endYear = 2020

# Create two date objects for start and end years.
startDate = ee.Date.fromYMD(startYear, 1, 1)
endDate = ee.Date.fromYMD(endYear + 1, 1, 1)

# Make a list with years.
years = ee.List.sequence(startYear, endYear)

# Make a list with months.
months = ee.List.sequence(1, 12)

# Import and filter the MOD13 dataset.
mod13 = ee.ImageCollection('MODIS/006/MOD13A1')
mod13 = mod13.filterDate(startDate, endDate)

# Select the EVI.
EVI = mod13.select('EVI')

# Import and filter the MODIS Terra surface reflectance dataset.
mod09 = ee.ImageCollection('MODIS/006/MOD09A1')
mod09 = mod09.filterDate(startDate, endDate)

landcover = ee.Image(
        'projects/gee-book/assets/A2-5/RLCMSv3/Mekonglandcover2018') \
    .select('lc').clip(mekongBasin)

lcVis = {
    'palette': PALETTE,
    'min': 0,
    'max': classNamesList.length - 1
}
Map.addLayer(landcover, lcVis, '2018 Land Cover')

# We use a function to remove clouds and cloud shadows.
# We map over the mod09 image collection and select the StateQA band.
# We mask pixels and return the image with clouds and cloud shadows masked.

def func_hao(image):
    quality = image.select('StateQA')
    mask = image.And(quality.bitwiseAnd(1).eq(
            0)) # No clouds. \
        .And(quality.bitwiseAnd(2).eq(0));

    return image.updateMask(mask)

mod09 = mod09.map(func_hao)









# We use a function to calculate the Moisture Stress Index.
# We map over the mod09 image collection and select the NIR and SWIR bands
# We set the timestamp and return the MSI.

def func_lru(image):
    nirband = image.select('sur_refl_b02')
    swirband = image.select('sur_refl_b06')
    msi = swirband.divide(nirband) \
        .rename('MSI') \
        .set('system:time_start', image.get(
            'system:time_start'))
    return msi

MSI = mod09.map(func_lru)










# We apply a nested loop where we first iterate over
# the relevant years and then iterate over the relevant
# months. The function returns an image with the MSI and EVI
# for each month. A flatten is applied to convert an
# collection of collections into a single collection.
monthlyIndices = ee.ImageCollection.fromImages(

def func_wsp(y):
        return months.map(function(m) {

            # Calculate EVI.
            evi = EVI.filter(ee.Filter \
                    .calendarRange(y, y, 'year')) \
                .filter(ee.Filter.calendarRange(m, m,
                    'month')) \
                .mean() \
                .multiply(0.0001)

            # Calculate MSI.
            msi = MSI.filter(ee.Filter \
                    .calendarRange(y, y, 'year')) \
                .filter(ee.Filter.calendarRange(m, m,
                    'month')) \
                .mean()

            # Return an image with all images as bands.
            return evi.addBands(msi) \
                .set('year', y) \
                .set('month', m) \
                .set('system:time_start', ee.Date \
                    .fromYMD(y, m, 1))

        })

    years.map(func_wsp
).flatten()

























).flatten()
)

# We select the landcover types for evergreen, deciduous forest, cropland and rice.
evergreenForest = landcover.eq(7)
deciduousForest = landcover.eq(5)
cropland = landcover.eq(10)
rice = landcover.eq(11)

# Mask pixels that do not belong to the category.

def func_yqe(img):
    return img.updateMask(evergreenForest)

evergreenIndex = monthlyIndices.map(func_yqe)




# Mask pixels that do not belong to the category.

def func_cip(img):
    return img.updateMask(deciduousForest)

deciduousIndex = monthlyIndices.map(func_cip)




# Mask pixels that do not belong to the category.

def func_vrq(img):
    return img.updateMask(cropland)

croplandIndex = monthlyIndices.map(func_vrq)




# Mask pixels that do not belong to the category.

def func_jit(img):
    return img.updateMask(rice)

riceIndex = monthlyIndices.map(func_jit)




# Define the chart and print it to the console.
chartIndices =
    ui.Chart.image.series({
        'imageCollection': deciduousIndex.select(['EVI', 'MSI']),
        'region': mekongBasin,
        'reducer': ee.Reducer.mean(),
        'scale': 1000,
        'xProperty': 'system:time_start'
    }) \
    .setSeriesNames(['EVI', 'MSI']) \
    .setOptions({
        'title': 'Monthly deciduous forest indices',
        'hAxis': {
            'title': 'Date',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'vAxis': {
            'title': 'Index',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'lineWidth': 1,
        'colors': ['darkgreen', 'brown'],
        'curveType': 'function'
    })

# Print the chart.
print(chartIndices)

# Define the chart and print it to the console.
chartIndices =
    ui.Chart.image.series({
        'imageCollection': evergreenIndex.select(['EVI', 'MSI']),
        'region': mekongBasin,
        'reducer': ee.Reducer.mean(),
        'scale': 1000,
        'xProperty': 'system:time_start'
    }) \
    .setSeriesNames(['EVI', 'MSI']) \
    .setOptions({
        'title': 'Monthly deciduous forest indices',
        'hAxis': {
            'title': 'Date',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'vAxis': {
            'title': 'Index',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'lineWidth': 1,
        'colors': ['darkgreen', 'brown'],
        'curveType': 'function'
    })

# Print the chart.
print(chartIndices)

# Define the chart and print it to the console.
chartIndices =
    ui.Chart.image.series({
        'imageCollection': croplandIndex.select(['EVI', 'MSI']),
        'region': mekongBasin,
        'reducer': ee.Reducer.mean(),
        'scale': 1000,
        'xProperty': 'system:time_start'
    }) \
    .setSeriesNames(['EVI', 'MSI']) \
    .setOptions({
        'title': 'Monthly cropland indices',
        'hAxis': {
            'title': 'Date',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'vAxis': {
            'title': 'Index',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'lineWidth': 1,
        'colors': ['darkgreen', 'brown'],
        'curveType': 'function'
    })

# Print the chart.
print(chartIndices)

# Define the chart and print it to the console.
chartIndices =
    ui.Chart.image.series({
        'imageCollection': riceIndex.select(['EVI', 'MSI']),
        'region': mekongBasin,
        'reducer': ee.Reducer.mean(),
        'scale': 1000,
        'xProperty': 'system:time_start'
    }) \
    .setSeriesNames(['EVI', 'MSI']) \
    .setOptions({
        'title': 'Monthly rice indices',
        'hAxis': {
            'title': 'Date',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'vAxis': {
            'title': 'Index',
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'lineWidth': 1,
        'colors': ['darkgreen', 'brown'],
        'curveType': 'function'
    })

# Print the chart.
print(chartIndices)

# Create the panel for the legend items.
legend = ui.Panel({
    'style': {
        'position': 'bottom-left',
        'padding': '8px 15px'
    }
})

# Create and add the legend title.
legendTitle = ui.Label({
    'value': 'Legend',
    'style': {
        'fontWeight': 'bold',
        'fontSize': '18px',
        'margin': '0 0 4px 0',
        'padding': '0'
    }
})

# Creates and styles 1 row of the legend.
def makeRow(color, name):
    # Create the label that is actually the colored box.
    colorBox = ui.Label({
        'style': {
            'backgroundColor': '#' + color,
            # Use padding to give the box height and width.
            'padding': '8px',
            'margin': '0 0 4px 0'
        }
    })

    # Create the label filled with the description text.
    description = ui.Label({
        'value': name,
        'style': {
            'margin': '0 0 4px 6px'
        }
    })

    return ui.Panel({
        'widgets': [colorBox, description],
        'layout': ui.Panel.Layout.Flow('horizontal')
    })


legend.add(legendTitle)
for i in range(0, classNamesList.length, 1):
    legend.add(makeRow(paletteList[i], classNamesList[i]))


# Add the legend to the map.
Map.add(legend)

# -----------------------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------------------
Map
