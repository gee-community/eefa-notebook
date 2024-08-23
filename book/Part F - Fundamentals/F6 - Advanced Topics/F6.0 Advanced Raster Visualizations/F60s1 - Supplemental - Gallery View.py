import ee
import geemap

Map = geemap.Map()

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
geometryLabel =

    # shown: False #
    ee.Geometry.Point([-104.81854696562625, 38.291704822204]),
    geometryGallery =

    # shown: False #
    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[-104.82125520585478, 38.294351019931455],
          [-104.82125520585478, 38.23194594511732],
          [-104.71980333207549, 38.23194594511732],
          [-104.71980333207549, 38.294351019931455]]], None, False)
#**** End of imports. If edited, may not auto-convert in the playground. ****#
text = require('users/gena/packages:text')
gallery = require('users/gena/packages:gallery')

Map.centerObject(geometryGallery, 12)

images = ee.ImageCollection('COPERNICUS/S2') \
    .filterDate('2020-01-01', '2022-01-01') \
    .filterBounds(geometryLabel)


def func_wpn(month):
  month = ee.Number(month)
  return images.filter(ee.Filter.calendarRange(month, month.add(1), 'month')) \
      .select(['B12', 'B8', 'B4']) \
      .reduce(ee.Reducer.percentile([15])) \
      .set({
        'label': ee.Date.fromYMD(2000, month.add(1), 1).format('MMM')
      })

imagesMonthly = ee.List.sequence(0, 11).map(func_wpn)










imagesMonthly = ee.ImageCollection(imagesMonthly)

# Render monthly images + label.

def func_dua(i):
  label = text.draw(i.get('label'), geometryLabel, Map.getScale(), {
      'fontSize': 24,
      'textColor': 'ffffff',
      'outlineColor': '000000',
      'outlineWidth': 3,
      'outlineOpacity': 0.6
  })
  return i.visualize(**{'min': 300, 'max': 3500}).blend(label)

imagesRGB = imagesMonthly.map(func_dua)











# Generate a single filmstrip image (rows x columns).
rows = 3
columns = 4
imageFilmstrip = gallery \
    .draw(imagesRGB, geometryGallery.bounds(), rows, columns)

Map.addLayer(imageFilmstrip)

# LGTM (nclinton)
Map
