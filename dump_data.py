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


df_rating = spark.read.format("csv").option("delimiter", "::").option('inferSchema',True).load("/home/hduser/Dataset/ratings.dat")
df_rating=df_rating.drop('_c3')

df_rating=df_rating.withColumnRenamed("_c0","userId")
df_rating=df_rating.withColumnRenamed("_c1","movieId")
df_rating=df_rating.withColumnRenamed("_c2","rating")



df_rating.write.format("com.mongodb.spark.sql.DefaultSource").option("database","Project").option("collection", "rating").save()

df_movies = spark.read.format("csv").option("delimiter", "::").option('inferSchema',True).load("/home/hduser/Dataset/movies.dat")


df_movies=df_movies.withColumnRenamed("_c0","movieId")
df_movies=df_movies.withColumnRenamed("_c1","title")
df_movies=df_movies.withColumnRenamed("_c2","genres")


df_movies.write.format("com.mongodb.spark.sql.DefaultSource").option("database","Project").option("collection", "movies").save()

