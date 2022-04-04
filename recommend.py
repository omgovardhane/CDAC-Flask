from pyexpat import model
from pyspark.sql import SparkSession
from pyspark.sql import SparkSession, SQLContext
#from pyspark import SparkConf, SparkContext
import pyspark
import findspark
from pyspark import SparkFiles
#import json
import pyspark.sql.functions as f
from pyspark.ml.recommendation import ALS, ALSModel
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

raw_df = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("database", "Project").option("collection", "rating").load()
raw_df = raw_df.drop("_id")
ml_df = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("database", "Project").option("collection", "movies").load()
ml_df = ml_df.drop("_id")

def give_recom():
        
        als=ALS(maxIter=10, regParam=0.5,userCol='userId',itemCol='movieId',ratingCol='rating',coldStartStrategy='drop')

        train_df,test_df=raw_df.randomSplit([0.7,0.3])

        model=als.fit(train_df)

        recomd_df=model.recommendForUserSubset(raw_df.filter('userId==1'),10)

        ex_df=recomd_df.select(f.col('userId'),f.explode('recommendations').alias('recom')).select('userId','recom.movieId','recom.rating')

        df_op = ex_df.join(ml_df,'movieId').select('title')
        
        return [data[0] for data in df_op.select('title').collect()]
