import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F5.1 Raster/Vector Conversions
#  Checkpoint:   F51a
#  Authors:      Keiko Nomura, Samuel Bowers
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# -------------#
# Section 1.1 #
# -------------#

# Load raster (elevation) and vector (colombia) datasets.
elevation = ee.Image("USGS/GMTED2010").rename("elevation")
colombia = ee.FeatureCollection("FAO/GAUL_SIMPLIFIED_500m/2015/level0").filter(
    ee.Filter.equals("ADM0_NAME", "Colombia")
)

# Display elevation image.
Map.centerObject(colombia, 7)
Map.addLayer(elevation, {"min": 0, "max": 4000}, "Elevation")

# Initialize image with zeros and define elevation zones.
zones = (
    ee.Image(0)
    .where(elevation.gt(100), 1)
    .where(elevation.gt(200), 2)
    .where(elevation.gt(500), 3)
)

# Mask pixels below sea level (<= 0 m) to retain only land areas.
# Name the band with values 0-3 as 'zone'.
zones = zones.updateMask(elevation.gt(0)).rename("zone")

Map.addLayer(
    zones,
    {
        "min": 0,
        "max": 3,
        "palette": ["white", "yellow", "lime", "green"],
        "opacity": 0.7,
    },
    "Elevation zones",
)

projection = elevation.projection()
scale = elevation.projection().nominalScale()

elevationVector = zones.reduceToVectors(
    {
        "geometry": colombia.geometry(),
        "crs": projection,
        "scale": 1000,  # scale
        "geometryType": "polygon",
        "eightConnected": False,
        "labelProperty": "zone",
        "bestEffort": False,
        "maxPixels": 1e13,
        "tileScale": 3,  # In case of error.
    }
)

print(elevationVector.limit(10))

elevationDrawn = elevationVector.draw({"color": "black", "strokeWidth": 1})
Map.addLayer(elevationDrawn, {}, "Elevation zone polygon")

zonesSmooth = zones.focalMode(4, "square")

zonesSmooth = zonesSmooth.reproject(projection.atScale(scale))

Map.addLayer(
    zonesSmooth,
    {
        "min": 0,
        "max": 3,
        "palette": ["white", "yellow", "lime", "green"],
        "opacity": 0.7,
    },
    "Elevation zones (smooth)",
)

elevationVectorSmooth = zonesSmooth.reduceToVectors(
    {
        "geometry": colombia.geometry(),
        "crs": projection,
        "scale": scale,
        "geometryType": "polygon",
        "eightConnected": False,
        "labelProperty": "zone",
        "bestEffort": False,
        "maxPixels": 1e13,
        "tileScale": 3,
    }
)

smoothDrawn = elevationVectorSmooth.draw({"color": "black", "strokeWidth": 1})
Map.addLayer(smoothDrawn, {}, "Elevation zone polygon (smooth)")

# -------------#
# Section 1.2 #
# -------------#

geometry = ee.Geometry.Polygon(
    [
        [-89.553, -0.929],
        [-89.436, -0.929],
        [-89.436, -0.866],
        [-89.553, -0.866],
        [-89.553, -0.929],
    ]
)

# To zoom into the area, un-comment and run below
# Map.centerObject(geometry,12)
Map.addLayer(geometry, {}, "Areas to extract points")

elevationSamples = elevation.sample(
    {
        "region": geometry,
        "projection": projection,
        "scale": scale,
        "geometries": True,
    }
)

Map.addLayer(elevationSamples, {}, "Points extracted")

# Add three properties to the output table:
# 'Elevation', 'Longitude', and 'Latitude'.


def func_psx(feature):
    geom = feature.geometry().coordinates()
    return ee.Feature(
        None,
        {
            "Elevation": ee.Number(feature.get("elevation")),
            "Long": ee.Number(geom.get(0)),
            "Lat": ee.Number(geom.get(1)),
        },
    )


elevationSamples = elevationSamples.map(func_psx)


# Export as CSV.
Export.table.toDrive(
    {
        "collection": elevationSamples,
        "description": "extracted_points",
        "fileFormat": "CSV",
    }
)

elevationSamplesStratified = zones.stratifiedSample(
    {
        "numPoints": 10,
        "classBand": "zone",
        "region": geometry,
        "scale": scale,
        "projection": projection,
        "geometries": True,
    }
)

Map.addLayer(elevationSamplesStratified, {}, "Stratified samples")

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
