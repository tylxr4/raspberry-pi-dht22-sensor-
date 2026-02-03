import sqlite3
conn = sqlite3.connect('sensor_data.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM readings")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()