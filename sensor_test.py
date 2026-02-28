import adafruit_dht
import board
import time
import sqlite3
import signal
import sys
from datetime import datetime

sensor = adafruit_dht.DHT22(board.D4)

def cleanup(signum, frame):
    print('Shutting down...')
    sensor.exit()
    sys.exit(0)

signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)

while True:
    try:
        temp_c = sensor.temperature
        humidity = sensor.humidity

        if temp_c is not None and humidity is not None:
            temp_f = (temp_c * 1.8) + 32
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'Temperature: {temp_f:.2f}, Humidity: {humidity:.2f}%')

            conn = sqlite3.connect('sensor_data.db')
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO readings (timestamp, temperature, humidity) VALUES (?, ?, ?)',
                (timestamp, temp_f, humidity))
            conn.commit()
            conn.close()
    except RuntimeError as e:
        print(f'Sensor read failed: {e}. Retrying...')
    except Exception as e:
        print(f'Unexpected error: {e}')

    time.sleep(2)
