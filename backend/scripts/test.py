import sqlite3
import os

os.chdir('./backend/data/')

def fetch_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('singapore_weather_database.db')
    cursor = conn.cursor()
    # Write the SQL query to fetch all data from the 'temperature' table
    cursor.execute('SELECT * FROM temperature')

    # Fetch all rows of data from the result
    rows = cursor.fetchall()
    # Print the fetched rows
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

fetch_data()