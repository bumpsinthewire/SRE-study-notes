import subprocess
import sys
from datetime import datetime


# function for checking the status of a service
def get_status(service_name):
    result = subprocess.run(
        f"systemctl is-active {service_name}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return result


# function for logging
def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("sentinel.log", "a") as f:
        f.write(f"[{timestamp}] {message}\n")


# service that we want to check
service = sys.argv[1] if len(sys.argv) > 1 else "ssh"

# call the function
current_status = get_status(service)

# basic error checking. expecting a 0 or 3 return code
if current_status.returncode != 0 and current_status.returncode != 3:
    print(f"Error: Could not check {service}. RC: {current_status.returncode}")
else:
    status = current_status.stdout.strip()
    print(f"Status of {service} is: {status}")

    # restart the service if it is not active
    if status != "active":

        # log the failure
        log_event(f"ALERT: {service} is {status}. Attempting restart.")

        subprocess.run(f"sudo systemctl restart {service}", shell=True)

        # run the check again to see if the restart worked
        new_check = get_status(service)
        new_status = new_check.stdout.strip()

        # log the result
        log_event(f"RECOVERY: {service} restart attempted. New status: {new_status}")
        print(f"New status of {service} is: {new_status}")
