import ee
import geemap

Map = geemap.Map()


# Function to calculate predicted ndvi and residuals from precipitation.
def calcPredNdviAndResiduals(img1):
    predNDVI = (
        img1.select("scale")
        .multiply(img1.select("precipitation"))
        .add(img1.select("offset"))
        .rename("predictedNDVI")
    )
    img1 = img1.addBands([predNDVI])
    residual = (
        img1.select("predictedNDVI")
        .subtract(img1.select("greenness"))
        .multiply(-1)
        .toFloat()
        .rename("residual")
    )
    return img1.addBands([residual])


# Prepares Collection to be run in LandTrendr subsetting Residual and Greenness.
def compileresidualColl(image):
    return image.select(["residual", "greenness"])


# Combine Precipitation and Greenness Lists into Image Collection
def createResidColl(greenColl, precipColl, aoi):

    # set some params
    startYear_Num = 1985
    endYear_Num = 2019
    numYears = endYear_Num - startYear_Num
    startMonth = "-01-01"
    endMonth = "-12-31"

    # ----  HERE WE USE LISTS TO COMBINE the two Image Collections :
    # Send GreennessColl to List to prepare integration of precip data.
    greenestList = greenColl.toList(numYears + 1, 0)
    precipList = precipColl.toList(numYears + 1, 0)

    # Add precipitation band to greenest pixel composites.
    greenestWprecipList = ee.List([])
    for i in range(0, numYears, 1):
        greenestThisYear = ee.Image(greenestList.get(i))
        greenestThisYear = greenestThisYear.addBands(precipList.get(i))
        greenestWprecipList = greenestWprecipList.add(greenestThisYear)

    # Create New Image Collection of Precip and Greenest NDVI per Pixel per Year.
    greenestWprecip = ee.ImageCollection(greenestWprecipList)

    def aoi_clip(image):
        return image.clip(aoi)

    # Clips Images in Collection
    greenestWprecipColl = greenestWprecip.map(aoi_clip)

    # ----------- Regress Precipitation and Greenness per Year per AOI

    # Precipitation vs ndvi regression.
    linearFit = greenestWprecipColl.select(["precipitation", "greenness"]).reduce(
        ee.Reducer.linearFit()
    )

    # Function to add a list of scale and offset from 'linearFit' to collection.
    def addRegression2Collection(img):
        scale = linearFit.select("scale")
        offset = linearFit.select("offset")
        return img.addBands([scale, offset])

    # Add scale and offset as bands in greenestWprecipList collection.
    greenestWprecipColl = greenestWprecipColl.map(addRegression2Collection)

    # Calculate predicted ndvi and residuals.
    greenestWprecipColl = greenestWprecipColl.map(calcPredNdviAndResiduals)
    print(greenestWprecipColl, "see all bands in here now")
    # FYI, this Image Collection now contains the following bands for each year:
    # greeness
    # precipitation
    # scale
    # offset
    # predicted NDVI
    # residual

    # Maps compileresidualColl.
    residualColl = greenestWprecipColl.map(compileresidualColl)

    return residualColl


exports.createResidColl = createResidColl

# LGTM (nclinton)
Map
