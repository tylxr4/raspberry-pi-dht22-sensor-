import sqlite3

conn = sqlite3.connect('sensor_data.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    alert_type TEXT,
    message TEXT,
    value REAL
)""")

conn.commit()
conn.close()

print("Alerts table created!")
