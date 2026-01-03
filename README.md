# Cybersecurity Portfolio

Python-based security analytics and detection logic focused on identifying anomalous authentication behavior and reducing false positives.

## Purpose
This repository contains focused Python examples that demonstrate how I approach **security analysis, detection logic, and signal-to-noise reduction** in a SOC-style context.

The emphasis is on:
- Explainable logic
- Practical thresholds
- Reducing false positives
- Clear reasoning over black-box rules

### Login Anomaly Detection
Analyzes daily login activity against a user-specific historical average. Alerts are triggered only when activity exceeds both:

- A minimum absolute threshold (fixed increase)
- A minimum proportional threshold (multiplier-based increase)

This mirrors real-world SOC alert tuning, where detections must balance sensitivity with operational noise.

## Portfolio Context
This repository represents the **analysis and detection** side of my cybersecurity work.

Additional projects in my GitHub profile demonstrate complementary skills such as:
- Security automation
- File parsing and configuration hygiene
- Practical access control maintenance

Together, these projects reflect how detection and response workflows support each other in real security operations.

## Why This Repo Exists
Many beginner security scripts rely on binary rules (e.g., “greater than X = alert”).  
This portfolio focuses instead on **behavioral analysis**, **context-aware thresholds**, and **decision-making logic** that can be reasoned about and adjusted over time.
