# Benchmarking Apache Spark and Hadoop MapReduce on Big Data Classification

This repository incorporates the material used in experiments for the paper **Benchmarking Apache Spark and Hadoop MapReduce on Big Data Classification**; which was submitted to *5th International Conference on Cloud and Big Data Computing* [ICCDBC'21](http://www.iccbdc.org/), in Liverpool, UK. You can reach the paper via [DOI link](https://doi.org/10.1145/3481646.3481649).

## :file_folder: spark
  ### └ naive-bayes.py
        Script that implements Naive-Bayes Classifier using MLlib library of Spark.
        
## :file_folder: mapreduce
  ### └ mahout-nb.sh
        Shell script to use Mahout's NB implementations.
        
  ### └ convert-to-seq.py
        Script to convert datasets in libsvm format to sequential file format.
