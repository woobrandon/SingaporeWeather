import sqlite3
import os
import datetime

os.chdir('./backend/data/')

def create_table():
    """
    Create a table with the columns id, filename, features and productUrl
    """
    # Connect to the SQLite database
    conn = sqlite3.connect('singapore_weather_database.db')
    cursor = conn.cursor()

    # Create temperature table 
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS temperature (
        timestamp DATETIME NOT NULL,          
        id VARCHAR(10) NOT NULL,
        temperature REAL NOT NULL,
        PRIMARY KEY (id, timestamp)   
    )
    ''')

    # Create station table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stations (
        id VARCHAR(10) PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        latitude REAL NOT NULL,
        longitude REAL NOT NULL
    )
    ''')

    conn.commit()
    conn.close()
    print("Table initialized!")
    return

def insert_temperatures(temperatures, timestamp) -> None:
    conn = sqlite3.connect('singapore_weather_database.db')
    cursor = conn.cursor()

    temperatures = temperatures.collect()

    for temperature in temperatures:

        cursor.execute("""
            INSERT OR IGNORE INTO temperature (timestamp, id, temperature)
            VALUES (?, ?, ?)
        """, (timestamp, temperature["id"], temperature["temperature"]))

    conn.commit()
    conn.close()
    return

def insert_stations(stations) -> None:
    conn = sqlite3.connect('singapore_weather_database.db')
    cursor = conn.cursor()

    stations = stations.collect()
    for station in stations:
        cursor.execute("""
            INSERT OR IGNORE INTO stations (id, name, latitude, longitude)
            VALUES (?, ?, ?, ?)
        """, (station["id"], station["name"], station["latitude"], station["longitude"]))

    conn.commit()
    conn.close()

    return

create_table()