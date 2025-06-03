from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for alarms
alarms = []

@app.route('/alarms', methods=['GET'])
def get_alarms():
    """Get all alarms."""
    return jsonify(alarms)

@app.route('/alarms', methods=['POST'])
def add_alarm():
    """Add a new alarm."""
    alarm = request.json
    alarms.append(alarm)
    return jsonify({"message": "Alarm added successfully!", "alarm": alarm}), 201

@app.route('/alarms/<int:alarm_id>', methods=['PUT'])
def update_alarm(alarm_id):
    """Update an existing alarm."""
    if alarm_id < 0 or alarm_id >= len(alarms):
        return jsonify({"error": "Alarm not found"}), 404

    alarms[alarm_id] = request.json
    return jsonify({"message": "Alarm updated successfully!", "alarm": alarms[alarm_id]})

@app.route('/alarms/<int:alarm_id>', methods=['DELETE'])
def delete_alarm(alarm_id):
    """Delete an alarm."""
    if alarm_id < 0 or alarm_id >= len(alarms):
        return jsonify({"error": "Alarm not found"}), 404

    removed_alarm = alarms.pop(alarm_id)
    return jsonify({"message": "Alarm deleted successfully!", "alarm": removed_alarm})

if __name__ == '__main__':
    app.run(debug=True)
