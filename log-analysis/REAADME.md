# Failed Login Detection – SOC Lab

## Objective
Detect brute-force SSH login attempts by analyzing Linux authentication logs.

## Description
This script parses Linux auth logs and identifies IP addresses with more than 5 failed login attempts, which may indicate a brute-force attack.

## Security Relevance
- Common SOC detection use case
- Maps to MITRE ATT&CK: T1110 (Brute Force)
- Helps analysts identify malicious IP addresses

## Tools Used
- Python
- Linux authentication logs

## Outcome
Suspicious IPs with repeated failed login attempts are flagged for investigation.
