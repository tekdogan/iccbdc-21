mkdir dataset-name

aws s3 cp s3://bucket-name/dataset-name/ dataset-name/ --recursive

hadoop fs -mkdir data/dataset-name

hadoop fs -mkdir data/dataset-name/data

hadoop fs -copyFromLocal dataset-name/* data/dataset-name/data/

mahout seqdirectory -i data/dataset-name/data -o data/dataset-name/nbseqfiles

mahout seq2sparse -i data/dataset-name/nbseqfiles -o data/dataset-name/nbsparse


mahout split -i data/dataset-name/nbsparse/tfidf-vectors -tr data/dataset-name/nbTrain -te data/dataset-name/nbTest -rp 25 -ow -xm mapreduce -mro data/dataset-name/mapReduceOutput

mahout trainnb -i data/dataset-name/nbsparse/tfidf-vectors -li data/dataset-name/nbLabels -o data/dataset-name/nbModel -ow

mahout testnb -i data/dataset-name/nbsparse/tfidf-vectors -m data/dataset-name/nbModel -l data/dataset-name/nbLabels -ow -o data/dataset-name/nbpredictions
