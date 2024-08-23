import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      Chapter A3.9 Conservation Applications - Assessing the
#                spatial relationship between burned area and precipitation
#  Checkpoint:   A39a
#  Authors:      Harriet Branson, Chelsea Smith
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ** Upload the area of interest ** #
AOI = ee.Geometry.Polygon([
    [
        [37.72, -11.22],
        [38.49, -11.22],
        [38.49, -12.29],
        [37.72, -12.29]
    ]
])
Map.centerObject(AOI, 9)
Map.addLayer(AOI, {
    'color': 'white'
}, 'Area of interest')

# ** MODIS Monthly Burn Area ** #

# Load in the MODIS Monthly Burned Area dataset.
dataset = ee.ImageCollection('MODIS/006/MCD64A1') \
    .filter(ee.Filter.date('2010-01-01', '2021-12-31'))

# Select the BurnDate band from the images in the collection.
MODIS_BurnDate = dataset.select('BurnDate')

# A function that will calculate the area of pixels in each image by date.
def addArea(img):
    area = ee.Image.pixelArea() \
        .updateMask(
            img
        ) # Limit area calculation to areas that have burned data. \
        .divide(1e6) \
        .clip(AOI) \
        .reduceRegion({
            'reducer': ee.Reducer.sum(),
            'geometry': AOI,
            'scale': 500,
            'bestEffort': True
        }).getNumber(
            'area'
        ); # Retrieve area from the reduce region calculation.
    # Add a new band to each image in the collection named area.
    return img.addBands(ee.Image(area).rename('area'))


# Apply function on image collection.
burnDateArea = MODIS_BurnDate.map(addArea)

# Select only the area band as we are using system time for date.
burnedArea = burnDateArea.select('area')

# Create a chart that shows the total burned area over time.
burnedAreaChart =
    ui.Chart.image \
    .series({
        'imageCollection': burnedArea, # Our image collection.
        'region': AOI,
        'reducer': ee.Reducer.mean(),
        'scale': 500,
        'xProperty': 'system:time_start' # time
    }) \
    .setSeriesNames(['Area']) \
    .setOptions({
        'title': 'Total monthly area burned in AOI',
        'hAxis': {
            'title': 'Date', # The x axis label.
            format: 'YYYY', # Years only for date format.
            'gridlines': {
                'count': 12
            },
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'vAxis': {
            'title': 'Total burned area (km²)', # The y-axis label
            'maxValue': 2250, # The bounds for y-axis
            'minValue': 0,
            'titleTextStyle': {
                'italic': False,
                'bold': True
            }
        },
        'lineWidth': 1.5,
        'colors': ['d74b46'], # The line color
    })
print(burnedAreaChart)

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map
