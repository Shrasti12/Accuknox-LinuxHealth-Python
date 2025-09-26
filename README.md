# Linux System Health Monitor
A lightweight Python script to monitor Linux system health by tracking CPU usage, memory usage, disk space, and running process count. The script logs system metrics at regular intervals and raises alerts if any predefined thresholds are exceeded (e.g., CPU usage above 80%). Designed for simplicity and easy customization, it provides continuous local monitoring with console output and log file recording.

# Features
Monitors CPU, memory, disk usage, and running processes

Configurable threshold alerts with console and log file notifications

Uses psutil for efficient system metric collection

Easy to configure monitoring intervals and thresholds

Suitable for use on Linux systems to track system health in real-time

# Setup and Usage
Install required dependency:

 ```bash
pip install psutil
```
Run the script:

text
 ```bash
python system_monitor.py
```
Monitor terminal output or review system_monitor.log for logged alerts and system status.
