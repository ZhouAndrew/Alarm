# Alarm Server and Client

This project provides a REST API-based alarm server and a command-line client for managing alarms. The server allows users to add, update, delete, and list alarms, while the client provides an easy way to interact with the server.

## Features
- Add alarms with a time and label.
- Update existing alarms.
- Delete alarms.
- List all alarms.

## Requirements
- Python 3.7 or higher
- Flask
- Requests

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd clock-server
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Start the Server
Run the following command to start the server:
```bash
python3 server.py
```
The server will start at `http://127.0.0.1:5000`.

### Use the Client
The client provides the following commands:

- **List all alarms**:
  ```bash
  python3 client.py list
  ```

- **Add a new alarm**:
  ```bash
  python3 client.py add "07:00" "Morning Alarm"
  ```

- **Update an existing alarm**:
  ```bash
  python3 client.py update 0 "08:00" "Updated Alarm"
  ```

- **Delete an alarm**:
  ```bash
  python3 client.py delete 0
  ```

## API Documentation

The Alarm Server provides the following REST API endpoints:

### 1. Get All Alarms
- **Endpoint**: `/alarms`
- **Method**: `GET`
- **Description**: Retrieve a list of all alarms.
- **Response**:
  - `200 OK`: Returns a JSON array of alarms.

### 2. Add a New Alarm
- **Endpoint**: `/alarms`
- **Method**: `POST`
- **Description**: Add a new alarm.
- **Request Body**:
  ```json
  {
    "time": "07:00",
    "label": "Morning Alarm"
  }
  ```
- **Response**:
  - `201 Created`: Returns the added alarm.

### 3. Update an Alarm
- **Endpoint**: `/alarms/<alarm_id>`
- **Method**: `PUT`
- **Description**: Update an existing alarm by its ID.
- **Request Body**:
  ```json
  {
    "time": "08:00",
    "label": "Updated Alarm"
  }
  ```
- **Response**:
  - `200 OK`: Returns the updated alarm.
  - `404 Not Found`: If the alarm ID does not exist.

### 4. Delete an Alarm
- **Endpoint**: `/alarms/<alarm_id>`
- **Method**: `DELETE`
- **Description**: Delete an alarm by its ID.
- **Response**:
  - `200 OK`: Returns the deleted alarm.
  - `404 Not Found`: If the alarm ID does not exist.

## Packaging and Distribution

To package the project, run:
```bash
python3 setup.py sdist
```

To install the package locally:
```bash
pip install dist/clock-server-0.1.tar.gz
```

## License
This project is licensed under the MIT License.

