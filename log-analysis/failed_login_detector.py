import re
from collections import defaultdict

failed_attempts = defaultdict(int)

log_file = "auth.log"
pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")

THRESHOLD = 5

with open(log_file, "r") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            ip = match.group(1)
            failed_attempts[ip] += 1

print("SOC Alert Report\n")

for ip, count in failed_attempts.items():
    if count > THRESHOLD:
        severity = "HIGH"
    elif count > 2:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    print(f"IP: {ip} | Attempts: {count} | Severity: {severity}")
