Raspberry Pi Temperature & Humidity Monitor

Environmental monitoring system with DHT22 sensor and web dashboard.

Hardware Setup
- Raspberry Pi 4 (4GB)
- DHT22 sensor wired to GPIO4
- Power: 3.3V, Ground: GND

Tech Stack
- Python 3
- Flask (REST API)
- SQLite (database)
- Bootstrap and Chart.js (dashboard)

Installation
- Install dependencies: pip3 install adafruit-circuitpython-dht RPi.GPIO flask --break-system-packages
- Create database: python3 database.py
- Create alerts table: python3 create_alerts_table.py

Usage
- Start sensor: python3 sensor_test.py &
- Start web server: python3 app.py
- Open browser: http://<your-pi-ip>:5000

Features
- Reads temperature and humidity every 2 seconds
- Stores data in SQLite database
- Web dashboard shows live readings
- Chart displays last 100 readings
- Alerts when temp/humidity outside safe range
- Logs alert history

API Endpoints
- /api/latest - current reading
- /api/readings - last 100 readings
- /api/alerts - alert history
- /api/alert - save new alert (POST)
