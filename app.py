from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/latest')
def get_latest():
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM readings ORDER BY timestamp DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return jsonify({
            'id': row[0],
            'timestamp': row[1],
            'temperature': row[2],
            'humidity': row[3]
        })
    else:
        return jsonify({'error': 'No data found'})


@app.route('/api/readings')
def get_readings():
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM readings ORDER BY timestamp DESC LIMIT 100")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        return jsonify([{
            'id': row[0],
            'timestamp': row[1],
            'temperature': row[2],
            'humidity': row[3]
        } for row in rows])
    else:
        return jsonify({'error': 'No data found'})




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

