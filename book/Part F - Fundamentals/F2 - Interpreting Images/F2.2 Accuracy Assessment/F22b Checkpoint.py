import ee
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F2.2 Accuracy Assessment: Quantifying Classification Quality
#  Checkpoint:   F22b
#  Authors:      Andréa Puzzi Nicolau, Karen Dyson, David Saah, Nicholas Clinton
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import the reference dataset.
data = ee.FeatureCollection("projects/gee-book/assets/F2-2/milan_data")

# Define the prediction bands.
predictionBands = [
    "SR_B1",
    "SR_B2",
    "SR_B3",
    "SR_B4",
    "SR_B5",
    "SR_B6",
    "SR_B7",
    "ST_B10",
    "ndvi",
    "ndwi",
]

# Split the dataset into training and testing sets.
trainingTesting = data.randomColumn()
trainingSet = trainingTesting.filter(ee.Filter.lessThan("random", 0.8))
testingSet = trainingTesting.filter(ee.Filter.greaterThanOrEquals("random", 0.8))

# Train the Random Forest Classifier with the trainingSet.
RFclassifier = ee.Classifier.smileRandomForest(50).train(
    {
        "features": trainingSet,
        "classProperty": "class",
        "inputProperties": predictionBands,
    }
)

# Now, to test the classification (verify model's accuracy),
# we classify the testingSet and get a confusion matrix.
confusionMatrix = testingSet.classify(RFclassifier).errorMatrix(
    {"actual": "class", "predicted": "classification"}
)

# Print the results.
print("Confusion matrix:", confusionMatrix)
print("Overall Accuracy:", confusionMatrix.accuracy())
print("Producers Accuracy:", confusionMatrix.producersAccuracy())
print("Consumers Accuracy:", confusionMatrix.consumersAccuracy())
print("Kappa:", confusionMatrix.kappa())

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------

# Hyperparameter tuning.
numTrees = ee.List.sequence(5, 100, 5)


def func_ehk(t):
    classifier = ee.Classifier.smileRandomForest(t).train(
        {
            "features": trainingSet,
            "classProperty": "class",
            "inputProperties": predictionBands,
        }
    )
    return (
        testingSet.classify(classifier)
        .errorMatrix("class", "classification")
        .accuracy()
    )


accuracies = numTrees.map(func_ehk)


print(
    ui.Chart.array.values(
        {"array": ee.Array(accuracies), "axis": 0, "xLabels": numTrees}
    ).setOptions(
        {
            "hAxis": {"title": "Number of trees"},
            "vAxis": {"title": "Accuracy"},
            "title": "Accuracy per number of trees",
        }
    )
)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map
