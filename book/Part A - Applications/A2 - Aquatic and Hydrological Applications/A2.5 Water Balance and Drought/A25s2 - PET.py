import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A2.5 Water Balance and Drought
#  Checkpoint:   A25s2
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

def func_ebb(name):
        return name.replace(/\s+/g, '_')

    return list.map(func_ebb)





# Function to get a list of column values from a structure.
def getList(struct, column):

def func_ycx(k):
        value = struct[k][column]
        return value

    return Object.keys(struct).map(func_ycx)






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

# Import the MOD16 dataset.
mod16 = ee.ImageCollection('MODIS/006/MOD16A2').select('ET')

# Filter for relevant time period.
mod16 = mod16.filterDate(startDate, endDate)

# Import the CHIRPS dataset.
CHIRPS = ee.ImageCollection('UCSB-CHG/CHIRPS/PENTAD')

# Filter for relevant time period.
CHIRPS = CHIRPS.filterDate(startDate, endDate)

landcover = ee.Image(
        'projects/gee-book/assets/A2-5/RLCMSv3/Mekonglandcover2018') \
    .select('lc').clip(mekongBasin)

lcVis = {
    'palette': PALETTE,
    'min': 0,
    'max': classNamesList.length - 1
}
Map.addLayer(landcover, lcVis, '2018 Land Cover')

# We apply a nested loop where we first iterate over
# the relevant years and then iterate over the relevant
# months. The function returns an image with P - ET
# for each month. A flatten is applied to convert an
# collection of collections into a single collection.
waterBalance = ee.ImageCollection.fromImages(

def func_cly(y):
        return months.map(function(m) {

            P = CHIRPS.filter(ee.Filter \
                    .calendarRange(y, y, 'year')) \
                .filter(ee.Filter.calendarRange(m, m,
                    'month')) \
                .sum()

            ET = mod16.filter(ee.Filter \
                    .calendarRange(y, y, 'year')) \
                .filter(ee.Filter.calendarRange(m, m,
                    'month')) \
                .sum() \
                .multiply(0.1)

            wb = P.subtract(ET).rename('wb')

            return wb.addBands(P).addBands(ET).set(
                    'year', y) \
                .set('month', m) \
                .set('system:time_start', ee.Date \
                    .fromYMD(y, m, 1))
        })

    years.map(func_cly
).flatten()























).flatten()
)

# Calculate mean monthly values.
monthlyP = waterBalance.select('precipitation').mean()
monthlyET = waterBalance.select('ET').mean()
monthlyWB = waterBalance.select('wb').mean()

# Apply reducer per land cover category.
# We create binary map for each class and multiply by mean ET.
# The results are stored in a feature with other properties of the class.
# The function returns a feature which are stored in a feature collection.

def func_vdu(nr):
    lc = landcover.eq(ee.Number(nr))

    P = monthlyP.multiply(lc)
    et = monthlyET.multiply(lc)

    pSum = P.reduceRegion({
        'reducer': ee.Reducer.sum(),
        'geometry': mekongBasin,
        'scale': 500
    }).get('precipitation')

    etSum = et.reduceRegion({
        'reducer': ee.Reducer.sum(),
        'geometry': mekongBasin,
        'scale': 500
    }).get('ET')

    return ee.Feature(None).set('et', etSum) \
        .set('p', pSum) \
        .set('class_name', classNames.get(nr)) \
        .set('palette', paletteList[nr]) \
        .set('class_number', nr)

lcFc = ee.FeatureCollection(classNumbers.map(func_vdu
))






















))

#  Create the chart.
pChart = ui.Chart.feature.byFeature({
        'features': lcFc,
        'xProperty': 'class_name',
        'yProperties': ['p', 'class_number']
    }) \
    .setChartType('PieChart') \
    .setOptions({
        'title': 'amount of P per landcover class',
        'slices': colors,
        'sliceVisibilityThreshold': 0 # Don't group small slices.
    })

# Display the chart.
print(pChart)

# Create the chart.
etChart = ui.Chart.feature.byFeature({
        'features': lcFc,
        'xProperty': 'class_name',
        'yProperties': ['et', 'class_number']
    }) \
    .setChartType('PieChart') \
    .setOptions({
        'title': 'amount of ET per landcover class',
        'slices': colors,
        'sliceVisibilityThreshold': 0 # Don't group small slices.
    })

# Display the chart
print(etChart)

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
