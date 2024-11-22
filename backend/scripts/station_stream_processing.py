from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import datetime
import os

os.environ["HADOOP_USER_NAME"] = "brandonwookj"
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.driver.bindAddress", "localhost") \
    .getOrCreate()


def station_stream_processing(data):
    stations = data["sations"]
    print("testing")
    print(stations)
    df = spark.createDataFrame(stations)
    return df