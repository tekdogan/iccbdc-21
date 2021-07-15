from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('nb').getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# for time measurements
import time

# for memory profiling
#import objgraph

# Load training data
data = spark.read.format("libsvm") \
.load("s3n://bigdatabucket-blg564e/url_combined.txt")

# Split the data into train and test
splits = data.randomSplit([0.8, 0.2], 97)
train = splits[0]
test = splits[1]

# create the trainer and set its parameters
nb = NaiveBayes(smoothing=1.0, modelType="multinomial")

# start timer
start = time.time()

# train the model
model = nb.fit(train)

# end timer
end = time.time()

# print the time taken to train the model
print(end - start)

# memory profiling after training
#objgraph.show_most_common_types()

# select example rows to display.
predictions = model.transform(test)
predictions.show()

# compute accuracy on the test set
evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction")
accuracy = evaluator.evaluate(predictions)
print("Test set accuracy = " + str(accuracy))
