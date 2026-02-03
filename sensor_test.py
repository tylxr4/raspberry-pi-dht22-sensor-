import adafruit_dht
import board
import time
import sqlite3
from datetime import datetime 

sensor = adafruit_dht.DHT22(board.D4)

while True:


    temperature = sensor.temperature
    humidity = sensor.humidity
    temperature_f = (sensor.temperature * 1.8) + 32

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Temperature: {temperature_f:.2f}, Humidity: {humidity:.2f}%")
    time.sleep(2)


    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO readings (timestamp, temperature, humidity) VALUES (?, ?, ?)", 
              (timestamp, temperature_f, humidity))
    conn.commit()
    conn.close()