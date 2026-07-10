
# Cowrie Honeypot Threat Intelligence & Research Platform

A lightweight cybersecurity research project that deploys a **Cowrie SSH/Telnet Honeypot on AWS EC2**, automatically collects real-world attack telemetry, enriches attacker information, and generates threat intelligence reports using Python.

---

# Overview

Internet-facing servers are continuously targeted by automated bots performing credential stuffing, brute-force attacks, malware deployment, and reconnaissance.

This project was built to study those attacks in a controlled environment by deploying a Cowrie honeypot on AWS and developing a Python-based analysis pipeline that automatically downloads logs, extracts attack statistics, enriches attacker IPs, and generates readable threat reports.

Unlike a basic Cowrie installation, this project focuses on both **honeypot deployment** and **security research**, providing insights into attacker behavior observed on the public Internet.

---

# Objectives

- Deploy a publicly accessible SSH/Telnet honeypot
- Capture real attack traffic from the Internet
- Analyze attacker behavior
- Identify common usernames and passwords
- Analyze commands executed after login
- Enrich attacker IPs with geolocation and ASN information
- Automate log collection from AWS EC2
- Generate readable threat intelligence reports

---

# Architecture

```
                     Internet
                         │
         Automated Bots / Attackers
                         │
             ┌──────────────────────┐
             │ AWS EC2 Ubuntu Server│
             │                      │
             │   Cowrie Honeypot    │
             │ SSH (2222)           │
             │ Telnet (23)          │
             └──────────┬───────────┘
                        │
                 cowrie.json Logs
                        │
             Automatic SCP Download
                        │
               Windows Python Project
                        │
        ┌───────────────┴───────────────┐
        │                               │
    JSON Parser                 IP Enrichment
        │                               │
        └───────────────┬───────────────┘
                        │
            Threat Intelligence Report
```

---

# Features

- AWS EC2 Deployment
- Cowrie SSH Honeypot
- Cowrie Telnet Honeypot
- Automatic Log Download using SCP
- JSON Log Parsing
- Connection Statistics
- Login Analysis
- Username Analysis
- Password Analysis
- Command Analysis
- Unique Attacker Detection
- Country Lookup
- City Lookup
- ISP Identification
- ASN Lookup
- Automated Threat Report Generation

---

# Technologies Used

## Cloud

- AWS EC2
- Ubuntu 24.04

## Honeypot

- Cowrie

## Programming

- Python 3

## Networking

- SSH
- Telnet
- SCP

## Python Libraries

- requests
- json
- collections
- subprocess

---

# Project Structure

```
cowrie/
│
├── main.py
├── download.py
├── parser.py
├── report.py
├── geo_lookup.py
├── config.py
├── requirements.txt
├── cowrie.json
└── README.md
```

---

# Workflow

## Step 1

Deploy Cowrie Honeypot on AWS EC2.

Cowrie listens on SSH and Telnet and records all attacker activity.

↓

## Step 2

Run

```bash
python main.py
```

↓

## Step 3

The script automatically downloads the latest Cowrie logs using SCP.

```
Downloading latest Cowrie logs...

cowrie.json

Download completed successfully.
```

↓

## Step 4

The parser extracts:

- Total Events
- Connections
- Successful Logins
- Usernames
- Passwords
- Commands
- Source IP Addresses

↓

## Step 5

Each attacker IP is enriched using an IP Geolocation API.

Information collected:

- Country
- City
- ISP
- ASN

↓

## Step 6

A complete threat intelligence report is generated.

---

# Sample Report

```
====================================================
Cowrie Honeypot Threat Report
====================================================

Total Events          : 150
Connections           : 7
Successful Logins     : 3
Unique Attacker IPs   : 5

Attacker IP Details

IP      : 112.126.25.48
Country : China
City    : Beijing
ISP     : Hangzhou Alibaba Advertising Co.
ASN     : AS37963

IP      : 122.36.187.5
Country : South Korea
City    : Seongdong-gu
ISP     : LG POWERCOMM
ASN     : AS17858
```

---

# Research Findings

After exposing the honeypot to the Internet, several observations were made.

## Attack Sources

Observed attacks originated from multiple countries including:

- China
- South Korea
- Germany
- United States

---

## Common Login Attempts

Examples observed:

```
root
admin
password
Fireitup
```

Some automated scanners also attempted binary or malformed credentials.

---

## Malware Activity

Several attackers attempted to execute shell scripts immediately after authentication.

Examples included:

```
sh kmount

sh swan

/bin/busybox

enable

system

shell
```

These commands are commonly associated with automated malware deployment targeting Linux systems and IoT devices.

---

# Example Output

The Python application automatically produces reports similar to:

```
Total Events          : 150
Connections           : 7
Successful Logins     : 3
Unique Attacker IPs   : 5

Top Usernames

root

Top Passwords

Fireitup
password

Top Commands

sh kmount
sh swan
/bin/busybox
```

---

# Future Improvements

- MITRE ATT&CK Technique Mapping
- Malware Hash Extraction
- VirusTotal Integration
- URLHaus Integration
- ThreatFox Integration
- IOC Export
- STIX 2.1 Report Generation
- PDF Report Generation
- Web Dashboard using Flask
- Scheduled Automatic Collection
- Docker Deployment

---

# Skills Demonstrated

- Cloud Security
- Honeypot Deployment
- Threat Intelligence
- Log Analysis
- Python Automation
- SSH
- Telnet
- Linux
- AWS
- Network Security
- Security Monitoring
- IOC Analysis
- IP Intelligence
- Threat Research

---

# Screenshots

<img width="1918" height="402" alt="Screenshot 2026-07-10 152011" src="https://github.com/user-attachments/assets/d709af5d-7449-4909-80eb-101863a64f91" />

<img width="1907" height="985" alt="Screenshot 2026-07-10 151501" src="https://github.com/user-attachments/assets/b21fda8f-9459-4de3-98ca-0832cf2d0c8a" />

<img width="1886" height="732" alt="Screenshot 2026-07-10 152131" src="https://github.com/user-attachments/assets/f050ace1-5307-4a84-ae5a-4ccc482567f8" />

---

# Disclaimer

This project was developed for educational purposes, cybersecurity research, and defensive security analysis only.

The honeypot is intentionally deployed in an isolated environment to observe attacker behavior without exposing production systems.
