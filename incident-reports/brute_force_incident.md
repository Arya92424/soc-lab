# Incident Report – Brute Force Attempt

## Incident Summary
Multiple failed SSH login attempts were detected from a single IP address,
indicating a potential brute-force attack.

## Detection Method
- Source: Linux authentication logs
- Detection Logic: More than 5 failed login attempts from the same IP
- Tool: Custom Python log analysis script

## Indicators of Compromise (IOCs)
- Suspicious IP address: 192.168.1.10
- Service targeted: SSH

## MITRE ATT&CK Mapping
- Technique: T1110 – Brute Force

## Severity
High

## Recommended Response
- Block IP address at firewall level
- Review other login activity from the same IP
- Enforce strong password policies
- Enable MFA if possible
