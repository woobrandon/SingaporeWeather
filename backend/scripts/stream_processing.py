from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType
import datetime

spark = SparkSession \
    .builder \
    .getOrCreate()

def process_temperature_stream(data):
    stations = data["stations"]
    readings = data["readings"][0]

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

    station_df = spark.createDataFrame(flatten_stations, schema = stations_schema).drop("deviceId")
    reading_df = spark.createDataFrame(flatten_readings, schema = readings_schema)

    result_df = station_df.join(reading_df, on = "id", how = "inner")
    result_df.show()
    return result_df

def process_weather_forecast_stream(data):
    forecasts = data["records"][0]["forecasts"]
    flatten_forecasts = [
        {
            "day": forecast["day"],
            "forecast_date": forecast["timestamp"],
            "temperature_low": forecast["temperature"]["low"],
            "temperature_high": forecast["temperature"]["high"],
            "humidity_low": forecast["relativeHumidity"]["low"],
            "humidity_high": forecast["relativeHumidity"]["high"],
            "forecast": forecast["forecast"]["text"],
            "wind_speed_low": forecast["wind"]["speed"]["low"],
            "wind_speed_high": forecast["wind"]["speed"]["high"],
            "wind_direction": forecast["wind"]["direction"]
        }
        for forecast in forecasts
    ]

    forecasts_schema = StructType([
        StructField("day", StringType(), True),
        StructField("forecast_date", StringType(), True),
        StructField("temperature_low", IntegerType(), True),
        StructField("temperature_high", IntegerType(), True),
        StructField("humidity_low", IntegerType(), True),
        StructField("humidity_high", IntegerType(), True),
        StructField("forecast", StringType(), True),
        StructField("wind_speed_low", IntegerType(), True),
        StructField("wind_speed_high", IntegerType(), True),
        StructField("wind_direction", StringType(), True)
    ])

    forecasts_df = spark.createDataFrame(flatten_forecasts, schema = forecasts_schema)
    forecasts_df.show()
    return forecasts_df
