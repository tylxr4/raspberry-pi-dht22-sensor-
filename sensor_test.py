import adafruit_dht
import board
import time 

sensor = adafruit_dht.DHT22(board.D4)

while True:

    temperature = sensor.temperature
    humidity = sensor.humidity
    temperature_f = (sensor.temperature * 1.8) + 32
    print(f"Temperature: {temperature_f:.2f}, Humidity: {humidity:.2f}%")
    time.sleep(2)
