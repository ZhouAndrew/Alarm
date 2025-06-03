import requests
import argparse

BASE_URL = 'http://127.0.0.1:5000/alarms'

def list_alarms():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        alarms = response.json()
        for i, alarm in enumerate(alarms):
            print(f"{i}: {alarm}")
    else:
        print("Failed to fetch alarms.")

def add_alarm(time, label):
    alarm = {"time": time, "label": label}
    response = requests.post(BASE_URL, json=alarm)
    if response.status_code == 201:
        print("Alarm added:", response.json())
    else:
        print("Failed to add alarm.")

def update_alarm(alarm_id, time, label):
    alarm = {"time": time, "label": label}
    response = requests.put(f"{BASE_URL}/{alarm_id}", json=alarm)
    if response.status_code == 200:
        print("Alarm updated:", response.json())
    else:
        print("Failed to update alarm.")

def delete_alarm(alarm_id):
    response = requests.delete(f"{BASE_URL}/{alarm_id}")
    if response.status_code == 200:
        print("Alarm deleted:", response.json())
    else:
        print("Failed to delete alarm.")

def main():
    parser = argparse.ArgumentParser(description="Command-line client for Alarm Server")
    subparsers = parser.add_subparsers(dest="command")

    # List alarms
    subparsers.add_parser("list", help="List all alarms")

    # Add alarm
    add_parser = subparsers.add_parser("add", help="Add a new alarm")
    add_parser.add_argument("time", help="Time of the alarm (e.g., 07:00)")
    add_parser.add_argument("label", help="Label for the alarm")

    # Update alarm
    update_parser = subparsers.add_parser("update", help="Update an existing alarm")
    update_parser.add_argument("id", type=int, help="ID of the alarm to update")
    update_parser.add_argument("time", help="New time of the alarm (e.g., 07:00)")
    update_parser.add_argument("label", help="New label for the alarm")

    # Delete alarm
    delete_parser = subparsers.add_parser("delete", help="Delete an alarm")
    delete_parser.add_argument("id", type=int, help="ID of the alarm to delete")

    args = parser.parse_args()

    if args.command == "list":
        list_alarms()
    elif args.command == "add":
        add_alarm(args.time, args.label)
    elif args.command == "update":
        update_alarm(args.id, args.time, args.label)
    elif args.command == "delete":
        delete_alarm(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
