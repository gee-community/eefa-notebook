import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A2.5 Water Balance and Drought
#  Checkpoint:   A25s1
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

classNamesList = getIds(classStruct)
probNames = cleanList(classNamesList)
classNames = ee.List(classNamesList)
classNumbers = getList(classStruct, 'number')
paletteList = getList(classStruct, 'color')
PALETTE = paletteList.join(',')

collection = ee.ImageCollection(
    'projects/gee-book/assets/A2-5/RLCMSv3')

lcVis = {
    'palette': PALETTE,
    'min': 0,
    'max': classNamesList.length - 1
}

for y in range(2000, 2019, 1):
    startDate = ee.Date.fromYMD(y, 1, 1)
    endDate = ee.Date.fromYMD(y, 12, 31)
    lcMap = ee.Image(collection.filterDate(startDate, endDate) \
            .first()) \
        .select('lc') \
        .clip(mekongBasin)
    Map.addLayer(lcMap, lcVis, y.toString(), False)


# Function to get a list of ids (keys) from a structure.
def getIds(struct):
    return Object.keys(struct)


# Function to replace spaces with underscores in a list of strings.
def cleanList(list):

def func_kdt(name):
        return name.replace(/\s+/g, '_')

    return list.map(func_kdt)





# Function to get a list of column values from a structure.
def getList(struct, column):

def func_waf(k):
        value = struct[k][column]
        return value

    return Object.keys(struct).map(func_waf)






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


for i in range(0, classNamesList.length, 1):
    legend.add(makeRow(paletteList[i], classNamesList[i]))


legend.add(legendTitle)

# Add the legend to the map.
Map.add(legend)

# -----------------------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------------------
Map
