import ee
import geemap

Map = geemap.Map()

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
geometry =

    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[-112.1088347655006, 38.522463862329126],
          [-112.1088347655006, 38.22315763773188],
          [-111.91520073229748, 38.22315763773188],
          [-111.91520073229748, 38.522463862329126]]], None, False)
#**** End of imports. If edited, may not auto-convert in the playground. ****#
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      A3.6 Working With GPS and Weather Data
#  Checkpoint:   A36a
#  Authors:      Peder Engelstad, Daniel Carver, Nicholas E. Young
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import the data and add it to the map and print.
cougarF53 = ee.FeatureCollection(
    'projects/gee-book/assets/A3-6/cougarF53')

Map.centerObject(cougarF53, 10)

Map.addLayer(cougarF53, {}, 'cougar presence data')

print(cougarF53, 'cougar data')

# Call in image collection and filter.
Daymet = ee.ImageCollection('NASA/ORNL/DAYMET_V4') \
    .filterDate('2014-02-11', '2014-11-02') \
    .filterBounds(geometry)

def func_zwz(image):
        return image.clip(geometry) \
    .map(func_zwz)




print(Daymet, 'Daymet')


# Convert to a multiband image.
DaymetImage = Daymet.toBands()

print(DaymetImage, 'DaymetImage')

# Call the sample regions function.
samples = DaymetImage.sampleRegions({
    'collection': cougarF53,
    'properties': ['id'],
    'scale': 1000
})

print(samples, 'samples')

# -----------------------------------------------------------------------
# CHECKPOINT
# -----------------------------------------------------------------------
Map
