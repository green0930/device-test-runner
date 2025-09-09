# Device Health Monitor

# Device Health Monitor

## Overview

This project demonstrates automated system-level testing across Android and Linux embedded devices using Python.

It combines:
- Android device testing using **ADB** commands
- Linux embedded device testing over **SSH**
- Basic health checks like memory availability and system uptime
- Automated pass/fail reporting and log generation

## Motivation

As QA increasingly spans multiple platforms and embedded hardware, automating validation across devices ensures consistency and reliability. This tool bridges mobile and embedded testing by leveraging Python to remotely interact with devices, collect system metrics, and generate reports.

## Setup

### Prerequisites

- Python 3.6 or higher  
- An Android device with USB debugging enabled and `adb` installed  
- A Linux embedded device accessible over SSH (e.g., Raspberry Pi)  
- Network connectivity between your machine and the Linux device

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/device-health-monitor.git
cd device-health-monitor


## Overview

This project demonstrates automated system-level testing across Android and Linux embedded devices using Python.

- Runs shell commands on Android devices via ADB
- Runs shell commands on Linux devices via SSH
- Performs basic health checks (memory, uptime)
- Generates pass/fail reports

## Setup

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Connect your Android device with USB debugging enabled.

3. Make sure SSH is enabled on your Linux device and you have the hostname/IP, username, and password.

4. Update the credentials in `test_runner.py`.

## Run Tests

```bash
python test_runner.py
