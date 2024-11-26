import sqlite3
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
from backend.scripts import consumer 

app = Flask(__name__)
CORS(app)

@app.route('/temperature', methods = ["GET"])
def get_temperature():
    consumer.fetched_temperature()

print(consumer.fetched_temperature())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

