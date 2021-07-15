# used for converting files in libsvm format to
# sequential file format to be used in hadoop mapreduce

from pyspark import SparkContext, SparkConf

distFile = sc.textFile("s3://bucket-name/dataset-name.txt")
distFile.map(lambda x: tuple(x.split(" ", 1))).saveAsSequenceFile("s3://bigdatabucket-blg564e/heartbeat-seq")
