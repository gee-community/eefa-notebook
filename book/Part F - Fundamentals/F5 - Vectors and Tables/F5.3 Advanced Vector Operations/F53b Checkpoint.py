import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F5.3 Advanced Vector Operations
#  Checkpoint:   F53b
#  Author:       Ujaval Gandhi
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

blocks = ee.FeatureCollection("TIGER/2010/Blocks")
roads = ee.FeatureCollection("TIGER/2016/Roads")
sfNeighborhoods = ee.FeatureCollection("projects/gee-book/assets/F5-0/SFneighborhoods")

geometry = sfNeighborhoods.geometry()
Map.centerObject(geometry)

# Filter blocks and roads to the San Francisco boundary.
sfBlocks = blocks.filter(ee.Filter.bounds(geometry))
sfRoads = roads.filter(ee.Filter.bounds(geometry))

# Select by Location
# Select all census blocks within 1km of an interstate.
interstateRoads = sfRoads.filter(ee.Filter.eq("rttyp", "I"))

# Visualize the layers
sfBlocksDrawn = sfBlocks.draw({"color": "gray", "strokeWidth": 1}).clip(geometry)
Map.addLayer(sfBlocksDrawn, {}, "All Blocks")
interstateRoadsDrawn = interstateRoads.draw({"color": "blue", "strokeWidth": 3}).clip(
    geometry
)
Map.addLayer(interstateRoadsDrawn, {}, "Interstate Roads")

# Define a spatial filter, with distance 1 km.
joinFilter = ee.Filter.withinDistance(
    {"distance": 1000, "leftField": ".geo", "rightField": ".geo", "maxError": 10}
)

closeBlocks = ee.Join.simple().apply(
    {"primary": sfBlocks, "secondary": interstateRoads, "condition": joinFilter}
)

closeBlocksDrawn = closeBlocks.draw({"color": "orange", "strokeWidth": 1}).clip(
    geometry
)
Map.addLayer(closeBlocksDrawn, {}, "Blocks within 1km")

# Spatial Join (Summary)
# Calculate Tree Counts.

sfNeighborhoods = ee.FeatureCollection("projects/gee-book/assets/F5-0/SFneighborhoods")
sfTrees = ee.FeatureCollection("projects/gee-book/assets/F5-3/SFTrees")

# Visualize the layers

# Use paint() to visualize the polygons with only outline
sfNeighborhoodsOutline = (
    ee.Image()
    .byte()
    .paint({"featureCollection": sfNeighborhoods, "color": 1, "width": 3})
)
Map.addLayer(sfNeighborhoodsOutline, {"palette": ["blue"]}, "SF Neighborhoods")

# Use style() to visualize the points
sfTreesStyled = sfTrees.style(
    **{"color": "green", "pointSize": 2, "pointShape": "triangle", "width": 2}
)
Map.addLayer(sfTreesStyled, {}, "SF Trees")

# Define a spatial intersection filter
intersectFilter = ee.Filter.intersects(
    {"leftField": ".geo", "rightField": ".geo", "maxError": 10}
)

# Define a saveAll join.
saveAllJoin = ee.Join.saveAll(
    {
        "matchesKey": "trees",
    }
)

# Apply the join.
joined = saveAllJoin.apply(sfNeighborhoods, sfTrees, intersectFilter)
print(joined.first())

# Calculate total number of trees within each feature.


def func_gjj(f):
    treesWithin = ee.List(f.get("trees"))
    totalTrees = ee.FeatureCollection(treesWithin).size()
    return f.set("total_trees", totalTrees)


sfNeighborhoods = joined.map(func_gjj)


print(sfNeighborhoods.first())

# Export the results as a CSV.
Export.table.toDrive(
    {
        "collection": sfNeighborhoods,
        "description": "SF_Neighborhood_Tree_Count",
        "folder": "earthengine",
        "fileNamePrefix": "tree_count",
        "fileFormat": "CSV",
        "selectors": ["nhood", "total_trees"],
    }
)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
