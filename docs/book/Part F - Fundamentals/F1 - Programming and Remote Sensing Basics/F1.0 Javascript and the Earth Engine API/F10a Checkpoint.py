import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F1.0 Javascript and the Earth Engine API
#  Checkpoint:   F10a
#  Author:       Ujaval Gandhi
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print('Hello World')

city = 'San Francisco'
print(city)

population = 873965
print(population)

cities = ['San Francisco', 'Los Angeles', 'New York', 'Atlanta']
print(cities)

cityData = {
    'city': 'San Francisco',
    'coordinates': [-122.4194, 37.7749],
    'population': 873965
}
print(cityData)

def greet(name):
    return 'Hello ' + name

print(greet('World'))
print(greet('Readers'))

# This is a comment!

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------


Map