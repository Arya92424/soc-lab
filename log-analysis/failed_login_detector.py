import re
from collections import defaultdict

# Dictionary to store failed login count per IP
failed_attempts = defaultdict(int)

# Sample auth log file
log_file = "auth.log"

# Regular expression to match failed SSH login attempts
pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")

try:
    with open(log_file, "r") as file:
        for line in file:
            match = pattern.search(line)
            if match:
                ip = match.group(1)
                failed_attempts[ip] += 1

    print("Suspicious IPs (more than 5 failed attempts):\n")

    for ip, count in failed_attempts.items():
        if count > 5:
            print(f"{ip} -> {count} failed attempts")

except FileNotFoundError:
    print("Log file not found. Please make sure auth.log exists.")
