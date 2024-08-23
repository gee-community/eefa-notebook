import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A2.3 Surface Water Mapping
#  Checkpoint:   A23c
#  Authors:      K. Markert, G. Donchyts, A. Haag
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# *** Section 1 ***

# Define a point in Cambodia to filter by location.
point = ee.Geometry.Point(104.9632, 11.7686)

Map.centerObject(point, 11)

# Get the Sentinel-1 collection and filter by space/time.
s1Collection = ee.ImageCollection('COPERNICUS/S1_GRD') \
    .filterBounds(point) \
    .filterDate('2019-10-05', '2019-10-06') \
    .filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING')) \
    .filter(ee.Filter.eq('instrumentMode', 'IW'))

# Grab the first image in the collection.
s1Image = s1Collection.first()

# Add the Sentinel-1 image to the map.
Map.addLayer(s1Image, {
    'min': -25,
    'max': 0,
    'bands': 'VV'
}, 'Sentinel-1 image')

# Specify band to use for Otsu thresholding.
band = 'VV'

# Define a reducer to calculate a histogram of values.
histogramReducer = ee.Reducer.histogram(255, 0.1)

# Reduce all of the image values.
globalHistogram = ee.Dictionary(
    s1Image.select(band).reduceRegion({
        'reducer': histogramReducer,
        'geometry': s1Image.geometry(),
        'scale': 90,
        'maxPixels': 1e10
    }).get(band)
)

# Extract out the histogram buckets and counts per bucket.
x = ee.List(globalHistogram.get('bucketMeans'))
y = ee.List(globalHistogram.get('histogram'))

# Define a list of values to plot.
dataCol = ee.Array.cat([x, y], 1).toList()

# Define the header information for data.
columnHeader = ee.List([
    [
    {
        'label': 'Backscatter',
        'role': 'domain',
        'type': 'number'
    },
    {
        'label': 'Values',
        'role': 'data',
        'type': 'number'
    }, ]
])

# Concat the header and data for plotting.
dataTable = columnHeader.cat(dataCol)

# Create plot using the ui.Chart function with the dataTable.
# Use 'evaluate' to transfer the server-side table to the client.
# Define the chart and print it to the console.
dataTable.evaluate(function(dataTableClient) {
    chart = ui.Chart(dataTableClient) \
        .setChartType('AreaChart') \
        .setOptions({
            'title': band + ' Global Histogram',
            'hAxis': {
                'title': 'Backscatter [dB]',
                'viewWindow': {
                    'min': -35,
                    'max': 15
                }
            },
            'vAxis': {
                'title': 'Count'
            }
        })
    print(chart)
})

# See:
# https:#medium.com/google-earth/otsus-method-for-image-segmentation-f5c48f405e
def otsu(histogram):
    # Make sure histogram is an ee.Dictionary object.
    histogram = ee.Dictionary(histogram)
    # Extract relevant values into arrays.
    counts = ee.Array(histogram.get('histogram'))
    means = ee.Array(histogram.get('bucketMeans'))
    # Calculate single statistics over arrays
    size = means.length().get([0])
    total = counts.reduce(ee.Reducer.sum(), [0]).get([0])
    sum = means.multiply(counts).reduce(ee.Reducer.sum(), [0]) \
        .get([0])
    mean = sum.divide(total)
    # Compute between sum of squares, where each mean partitions the data.
    indices = ee.List.sequence(1, size)

def func_gfk(i):
        aCounts = counts.slice(0, 0, i)
        aCount = aCounts.reduce(ee.Reducer.sum(), [0]) \
            .get([0])
        aMeans = means.slice(0, 0, i)
        aMean = aMeans.multiply(aCounts) \
            .reduce(ee.Reducer.sum(), [0]).get([0]) \
            .divide(aCount)
        bCount = total.subtract(aCount)
        bMean = sum.subtract(aCount.multiply(aMean)) \
            .divide(bCount)
        return aCount.multiply(aMean.subtract(mean).pow(2)) \
            .add(
                bCount.multiply(bMean.subtract(mean).pow(2)))

    bss = indices.map(func_gfk)















    # Return the mean value corresponding to the maximum BSS.
    return means.sort(bss).get([-1])


# Apply otsu thresholding.
globalThreshold = otsu(globalHistogram)
print('Global threshold value:', globalThreshold)

# Create list of empty strings that will be used for annotation.
thresholdCol = ee.List.repeat('', x.length())
# Find the index where the bucketMean equals the threshold.
threshIndex = x.indexOf(globalThreshold)
# Set the index to the annotation text.
thresholdCol = thresholdCol.set(threshIndex, 'Otsu Threshold')

# Redefine the column header information with annotation column.
columnHeader = ee.List([
    [
    {
        'label': 'Backscatter',
        'role': 'domain',
        'type': 'number'
    },
    {
        'label': 'Values',
        'role': 'data',
        'type': 'number'
    },
    {
        'label': 'Threshold',
        'role': 'annotation',
        'type': 'string'
    }]
])

# Loop through the data rows and add the annotation column.
i) {
    i = ee.Number(i)
    row = ee.List(dataCol.get(i))
    return row.add(ee.String(thresholdCol.get(i)))
})

# Concat the header and data for plotting.
dataTable = columnHeader.cat(dataCol)

# Create plot using the ui.Chart function with the dataTable.
# Use 'evaluate' to transfer the server-side table to the client.
# Define the chart and print it to the console.
dataTable.evaluate(function(dataTableClient) {
    # loop through the client-side table and set empty strings to None
    for i in range(0, dataTableClient.length, 1):
        if (dataTableClient[i][2] === '') {
            dataTableClient[i][2] = None
        }

    chart = ui.Chart(dataTableClient) \
        .setChartType('AreaChart') \
        .setOptions({
            'title': band + \
                ' Global Histogram with Threshold annotation',
            'hAxis': {
                'title': 'Backscatter [dB]',
                'viewWindow': {
                    'min': -35,
                    'max': 15
                }
            },
            'vAxis': {
                'title': 'Count'
            },
            'annotations': {
                'style': 'line'
            }
        })
    print(chart)
})

# Apply the threshold on the image to extract water.
globalWater = s1Image.select(band).lt(globalThreshold)

# Add the water image to the map and mask 0 (no-water) values.
Map.addLayer(globalWater.selfMask(),
    {
        'palette': 'blue'
    },
    'Water (global threshold)')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# *** Section 2 ***

# Define parameters for the adaptive thresholding.
# Initial estimate of water/no-water for estimating the edges
initialThreshold = -16
# Number of connected pixels to use for length calculation.
connectedPixels = 100
# Length of edges to be considered water edges.
edgeLength = 20
# Buffer in meters to apply to edges.
edgeBuffer = 300
# Threshold for canny edge detection.
cannyThreshold = 1
# Sigma value for gaussian filter in canny edge detection.
cannySigma = 1
# Lower threshold for canny detection.
cannyLt = 0.05

# Get preliminary water.
binary = s1Image.select(band).lt(initialThreshold) \
    .rename('binary')

# Get projection information to convert buffer size to pixels.
imageProj = s1Image.select(band).projection()

# Get canny edges.
canny = ee.Algorithms.CannyEdgeDetector({
    'image': binary,
    'threshold': cannyThreshold,
    'sigma': cannySigma
})

# Process canny edges.

# Get the edges and length of edges.
connected = canny.updateMask(canny).lt(cannyLt) \
    .connectedPixelCount(connectedPixels, True)

# Mask short edges that can be noise.
edges = connected.gte(edgeLength)

# Calculate the buffer in pixel size.
edgeBufferPixel = ee.Number(edgeBuffer).divide(imageProj \
    .nominalScale())

# Buffer the edges using a dilation operation.
bufferedEdges = edges.fastDistanceTransform().lt(edgeBufferPixel)

# Mask areas not within the buffer .
edgeImage = s1Image.select(band).updateMask(bufferedEdges)

# Add the detected edges and buffered edges to the map.
Map.addLayer(edges, {
    'palette': 'red'
}, 'Detected water edges')
edgesVis = {
    'palette': 'yellow',
    'opacity': 0.5
}
Map.addLayer(bufferedEdges.selfMask(), edgesVis,
    'Buffered water edges')

# Reduce all of the image values.
localHistogram = ee.Dictionary(
    edgeImage.reduceRegion({
        'reducer': histogramReducer,
        'geometry': s1Image.geometry(),
        'scale': 90,
        'maxPixels': 1e10
    }).get(band)
)

# Apply otsu thresholding.
localThreshold = otsu(localHistogram)
print('Adaptive threshold value:', localThreshold)

# Extract out the histogram buckets and counts per bucket.
x = ee.List(localHistogram.get('bucketMeans'))
y = ee.List(localHistogram.get('histogram'))

# Define a list of values to plot.
dataCol = ee.Array.cat([x, y], 1).toList()

# Concat the header and data for plotting.
dataTable = columnHeader.cat(dataCol)

# Create list of empty strings that will be used for annotation.
thresholdCol = ee.List.repeat('', x.length())
# Find the index that bucketMean equals the threshold.
threshIndex = x.indexOf(localThreshold)
# Set the index to the annotation text.
thresholdCol = thresholdCol.set(threshIndex, 'Otsu Threshold')

# Redefine the column header information now with annotation col.
columnHeader = ee.List([
    [
    {
        'label': 'Backscatter',
        'role': 'domain',
        'type': 'number'
    },
    {
        'label': 'Values',
        'role': 'data',
        'type': 'number'
    },
    {
        'label': 'Threshold',
        'role': 'annotation',
        'type': 'string'
    }]
])

# Loop through the data rows and add the annotation col.
i) {
    i = ee.Number(i)
    row = ee.List(dataCol.get(i))
    return row.add(ee.String(thresholdCol.get(i)))
})

# Concat the header and data for plotting.
dataTable = columnHeader.cat(dataCol)

# Create plot using the ui.Chart function with the dataTable.
# Use 'evaluate' to transfer the server-side table to the client.
# Define the chart and print it to the console.
dataTable.evaluate(function(dataTableClient) {
    # Loop through the client-side table and set empty strings to None.
    for i in range(0, dataTableClient.length, 1):
        if (dataTableClient[i][2] === '') {
            dataTableClient[i][2] = None
        }

    chart = ui.Chart(dataTableClient) \
        .setChartType('AreaChart') \
        .setOptions({
            'title': band + \
                ' Adaptive Histogram with Threshold annotation',
            'hAxis': {
                'title': 'Backscatter [dB]',
                'viewWindow': {
                    'min': -35,
                    'max': 15
                }
            },
            'vAxis': {
                'title': 'Count'
            },
            'annotations': {
                'style': 'line'
            }
        })
    print(chart)
})

# Apply the threshold on the image to extract water.
localWater = s1Image.select(band).lt(localThreshold)

# Add the water image to the map and mask 0 (no-water) values.
Map.addLayer(localWater.selfMask(),
    {
        'palette': 'darkblue'
    },
    'Water (adaptive threshold)')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Get the previous 5 years of permanent water.

# Get the JRC historical yearly dataset.
jrc = ee.ImageCollection('JRC/GSW1_3/YearlyHistory') \
    .filterDate('1985-01-01', s1Image.date()) \
    .limit(5, 'system:time_start', False)


def func_fjc(image):
        # Extract out the permanent water class.
        return image.select('waterClass').eq(3)
        # Reduce the collection to get information on if a pixel has
        # been classified as permanent water in the past 5 years.

permanentWater = jrc.map(func_fjc
).sum()




).sum() \
    .unmask(0) \
    .gt(0) \
    .updateMask(localWater.mask())

# Add the permanent water layer to the map.
Map.addLayer(permanentWater.selfMask(),
    {
        'palette': 'royalblue'
    },
    'JRC permanent water')

# Find areas where there is not permanent water, but water is observed.
floodImage = permanentWater.Not().And(localWater)

# Add flood image to map.
Map.addLayer(floodImage.selfMask(), {
    'palette': 'firebrick'
}, 'Flood areas')

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
