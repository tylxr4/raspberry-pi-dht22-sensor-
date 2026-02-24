from flask import Flask, jsonify, render_template, request
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

@app.route('/api/alert', methods=['POST'])
def log_alert():
    from flask import request
    from datetime import datetime
    
    data = request.get_json()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alerts (timestamp, alert_type, message, value) VALUES (?, ?, ?, ?)",
                   (timestamp, data['alert_type'], data['message'], data['value']))
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'success'})

@app.route('/api/alerts')
def get_alerts():
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alerts ORDER BY timestamp DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    
    if rows:
        return jsonify([{
            'id': row[0],
            'timestamp': row[1],
            'alert_type': row[2],
            'message': row[3],
            'value': row[4]
        } for row in rows])
    else:
        return jsonify([])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

