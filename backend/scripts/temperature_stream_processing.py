from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
import datetime

spark = SparkSession \
    .builder \
    .getOrCreate()

def temperature_stream_processing(data):
    stations = data["stations"]
    readings = data["readings"][0]

    timestamp = readings["timestamp"]
    flatten_stations = [
        {
            "id": station["id"],
            "deviceId": station["deviceId"],
            "name": station["name"],
            "latitude": station["location"]["latitude"],
            "longitude": station["location"]["longitude"]
        }
        for station in stations
    ]

    flatten_readings = [
        {
            "id": reading["stationId"],
            "temperature": float(reading["value"]),
        }
        for reading in readings["data"]
    ]
    stations_schema = StructType([
        StructField("id", StringType(), True),
        StructField("deviceId", StringType(), True),
        StructField("name", StringType(), True),
        StructField("latitude", DoubleType(), True),
        StructField("longitude", DoubleType(), True),
    ])
    readings_schema = StructType([
        StructField("id", StringType(), True),
        StructField("temperature", DoubleType(), True),
    ])

    station_df = spark.createDataFrame(flatten_stations, schema = stations_schema)
    reading_df = spark.createDataFrame(flatten_readings, schema = readings_schema)

    station_df.show()
    reading_df.show()
    return 
