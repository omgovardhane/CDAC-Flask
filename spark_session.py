from pyspark.sql import SparkSession
from pyspark.sql import SparkSession, SQLContext
#from pyspark import SparkConf, SparkContext
#import pyspark
import findspark
#from pyspark import SparkFiles
#import json
import pyspark.sql.functions as f
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
findspark.init()
findspark.find()
#import pickle

inp="mongodb://127.0.0.1/Project.movierecom"
outp="mongodb://127.0.0.1/Project.movierecom"

spark=SparkSession\
        .builder\
        .appName("movierecom")\
        .config("spark.mongodb.input.uri",inp)\
        .config("spark.mongodb.output.uri",outp)\
        .config("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.12:2.4.2")\
        .getOrCreate()










