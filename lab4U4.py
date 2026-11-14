
import json

try:
    # Read the JSON file
    with open("logs.json", "r") as file:
        logs = json.load(file)

    info_count = 0
    warning_count = 0
    error_count = 0

    # Display all log records
    print("Application Log Records:\n")

    for log in logs:
        print("Timestamp:", log["Timestamp"])
        print("Log Level:", log["Log Level"])
        print("Message:", log["Message"])
        print()

        # Count log categories
        if log["Log Level"] == "INFO":
            info_count += 1
        elif log["Log Level"] == "WARNING":
            warning_count += 1
        elif log["Log Level"] == "ERROR":
            error_count += 1

    # Display summary
    print("Log Summary:")
    print("Total INFO messages:", info_count)
    print("Total WARNING messages:", warning_count)
    print("Total ERROR messages:", error_count)

except FileNotFoundError:
    print("Error: logs.json file does not exist!")

except json.JSONDecodeError:
    print("Error: Invalid JSON data!")
