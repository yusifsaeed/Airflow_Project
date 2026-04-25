# **Automated Transaction Reporting Pipeline**
An automated data orchestration pipeline built with Apache Airflow. This project demonstrates a complete workflow for processing financial transactions, executing external scripts, and distributing reports via email notifications.


# **Project Overview**

The pipeline (Report_Transaction) is designed to run every 10 minutes, ensuring real-time data processing and reporting. It handles everything from data calculation to multi-channel communication.

Key Features:
- Modular Design: Uses specialized Airflow Operators (Python, Bash, Email).
- Data Integrity: Includes a calculation logic that aggregates transaction data and generates a persistent text report.
- External Integration: Demonstrates the ability to trigger external Python applications (app.py) via Bash commands.
- Automated Alerts: Delivers an HTML-formatted report directly to the stakeholder's inbox.


# **Tech Stack**

- Orchestrator: Apache Airflow
- Language: Python 3
- Scripting: Bash
- Environment: Linux/Docker


# **ScreenShot**
<img width="1912" height="876" alt="Screenshot 2026-04-26 013328" src="https://github.com/user-attachments/assets/484837f6-2590-4b81-9e84-0f511f5e0327" />
