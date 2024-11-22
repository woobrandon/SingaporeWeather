from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import datetime

spark = SparkSession.builder \
    .appName("SingaporeTemperatureProcessor") \
    .getOrCreate()

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "singapore_temperature") \
    .load()

print(df)