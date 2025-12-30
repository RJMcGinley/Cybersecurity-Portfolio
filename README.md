# Cybersecurity-Portfolio
Python-based security analytics and detection logic focused on identifying anomalous authentication behavior and reducing false positives.

# Security Analytics (Python)

This repository contains Python-based security analysis scripts designed to
detect anomalous behavior while minimizing false positives.

## Current Modules

### Login Anomaly Detection
Analyzes daily login activity against a user-specific historical average.
Alerts are triggered only when activity exceeds both:
- a minimum absolute threshold
- a minimum multiplier threshold

This approach mirrors real-world SOC alert tuning to reduce noise.

## Future Additions
- IP allow/deny analysis
- Threshold-based alerting examples
- Authentication behavior baselining
- Log parsing utilities
- Detection logic demonstrations

## Why This Repo Exists
Many beginner security scripts focus on binary rules. This repository focuses
on **behavioral analysis**, **signal vs noise**, and **realistic alerting logic**.
