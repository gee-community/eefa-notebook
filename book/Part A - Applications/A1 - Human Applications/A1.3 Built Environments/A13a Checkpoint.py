import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A1.3 Built Environments
#  Checkpoint:   A13a
#  Author:       Erin Trochim
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import roads data.
grip4_africa = ee.FeatureCollection(
        'projects/sat-io/open-datasets/GRIP4/Africa'),
    grip4_north_america = ee.FeatureCollection(
        'projects/sat-io/open-datasets/GRIP4/North-America'),
    grip4_europe = ee.FeatureCollection(
        'projects/sat-io/open-datasets/GRIP4/Europe')

# Check the roads data sizes.
print('Grip4 Africa size', grip4_africa.size())
print('Grip4 North America size', grip4_north_america.size())
print('Grip4 Europe size', grip4_europe.size())

# Display the roads data.
Map.addLayer(ee.FeatureCollection(grip4_africa).style(**{
    'color': '413B3A',
    'width': 1
}), {}, 'Grip4 Africa')
Map.addLayer(ee.FeatureCollection(grip4_north_america).style(**{
    'color': '413B3A',
    'width': 1
}), {}, 'Grip4 North America')
Map.addLayer(ee.FeatureCollection(grip4_europe).style(**{
    'color': '413B3A',
    'width': 1
}), {}, 'Grip4 Europe')

# Import simplified countries.
countries = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017')

# Add a function to calculate the feature's geometry area.
# Add the function as a property.
def addArea(feature):
    return feature.set({
        'areaKm': feature.geometry().area().divide(1000 *
            1000)
    }); # km2 squared


# Map the area getting function over the FeatureCollection.
countriesArea = countries.map(addArea)

# Filter to the largest country in Africa.
Algeria = countriesArea.filter(ee.Filter.inList('country_na', [
    'Algeria'
]))

# Display the selected countries.
Map.addLayer(Algeria.style(**{
    'fillColor': 'b5ffb4',
    'color': '00909F',
    'width': 1.0
}), {}, 'Algeria')

# This function calculates the road length per country for the associated GRIP dataset.
def roadLength4Country(country, grip4):

    # Join roads to countries.
    intersectsFilter = ee.Filter.intersects({
        'leftField': '.geo',
        'rightField': '.geo',
        'maxError': 10
    })

    grip4Selected = grip4.filterBounds(country)

    countriesWithRds = ee.Join.saveAll('roads').apply({
        'primary': country,
        'secondary': grip4Selected,
        'condition': intersectsFilter
    }).filter(ee.Filter.neq('roads', None))

    # Return country with calculation of roadLength and roadsPerArea.

def func_uni(country):
        roadsList = ee.List(country.get('roads'))
        roadLengths = roadsList.map(function(road) {
            return ee.Feature(road).intersection(
                country, 10).length(10)
        })
        roadLength = ee.Number(roadLengths.reduce(ee \
            .Reducer.sum()))
        return country.set({
            'roadLength': roadLength.divide(
                1000), # Convert to km.
            'roadsPerArea': roadLength.divide(ee \
                .Number(country.get('areaKm'))
            )
        })

    return countriesWithRds.map(func_uni
).select(['country_na', 'areaKm', 'roadLength',














).select(['country_na', 'areaKm', 'roadLength',
        'roadsPerArea'
    ])


# Apply the road length function to Algeria.
roadLengthAlgeria = roadLength4Country(Algeria, grip4_africa)

# Print the road statistics for Algeria.
print('Roads statistics in Algeria', roadLengthAlgeria)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
