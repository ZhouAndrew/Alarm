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

