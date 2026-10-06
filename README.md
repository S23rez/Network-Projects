# 🌐 Comprehensive Network Engineering & Cybersecurity Portfolio

[![Author](https://img.shields.io/badge/Developer-Odunuga%20Fatai%20Olayinka-blue.svg)](https://github.com/S23rez)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg)](https://python.org)
[![GNS3](https://img.shields.io/badge/GNS3-Topologies-orange.svg)](https://gns3.com)
[![Cisco](https://img.shields.io/badge/Cisco-Packet%20Tracer%20%7C%20IOS-049fd9.svg)](https://www.netacad.com)

Welcome to the **Network Engineering & Cybersecurity Portfolio** developed by **Odunuga Fatai Olayinka**. This repository hosts a curated collection of enterprise network topology designs, Cisco IOS device configurations, hands-on Cisco Packet Tracer lab modules, and custom Python automation toolkits for network scanning, security playbooks, OSINT, and privacy compliance.

---

## 📁 Repository Overview & Directory Architecture

```text
Network-Projects/
├── 📄 README.md                        <- Master Repository Documentation
├── 📂 cisco-ios-configs/              <- Cisco IOS Router & Switch Security Hardening Templates
│   └── 📄 README.md
├── 📂 gns3-topologies/                <- Complex Multi-Device GNS3 Simulation Topologies & PCAPs
│   ├── 📄 README.md
│   ├── 📂 Lab 1/                      <- Multi-Subnet Router & Switch DHCP Infrastructure
│   └── 📂 Lab 2 Static Routing/       <- Multi-Router Static Routing Topology & Traffic Capture
├── 📂 packet-tracer-labs/             <- Cisco Packet Tracer (.pkt) Foundational Lab Exercises
│   ├── 📄 README.md
│   └── 📄 Day 01 - Day 09 Labs (.pkt)
└── 📂 python-network-tools/
    └── 📂 Automations/                <- Python Security Automation & Network Audit Suite
        ├── 📄 Readme.md
        ├── 📄 Cisco Firewall.py
        ├── 📄 Network Port Scanner project.py
        ├── 📄 security_playbook_automation.py
        ├── 📄 har_remover.py
        ├── 📄 Iteration-Control-and-Randomized-Audit-Tools.py
        ├── 📄 subdomain_finder.py
        ├── 📄 web_scraper.py
        └── 📄 file_organizer.py
```

---

## 🛠️ Portfolio Modules & Key Capabilities

### 1. ⚙️ Cisco IOS Configurations (`cisco-ios-configs/`)
* **Focus:** Enterprise switch and router security hardening, ACL policies, SSH configuration, and VLAN management.
* **Key Features:** Production-ready Cisco IOS device configuration templates engineered to enforce security best practices across network infrastructure.
* 🔗 **Documentation:** [cisco-ios-configs/README.md](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/cisco-ios-configs/README.md)

---

### 2. 🛰️ GNS3 Topologies & Network Simulations (`gns3-topologies/`)
Simulated high-availability network environments with detailed configuration logs, PCAP Wireshark packet captures, and step-by-step validation.

* **Lab 1: Multi-Subnet Router & Switch DHCP Infrastructure**
  * **Objective:** Implement inter-subnet routing and centralized multi-pool DHCP server configuration across Class A, B, and C subnets on Cisco IOS v15.9.
  * **Key Components:** Custom IP DHCP pools (`POOL-10`, `POOL-172`, `POOL-192`), gateway configurations (`10.0.0.254`, `172.16.0.254`, `192.168.0.254`), PVST Spanning Tree, and PortFast edge configurations.
  * 🔗 **Device Logs:** [Router.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/Router.txt) | [Switch 1.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/Switch%201.txt) | [Switch 2.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/Switch%202.txt) | [Switch 3.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/Switch%203.txt)

* **Lab 2: Multi-Router Static Routing & Wireshark Traffic Analysis**
  * **Objective:** Establish static routing paths across a multi-router topology (R1–R4, VPC1–VPC2) with end-to-end ICMP verification and PCAP traffic analysis.
  * **Key Components:** Custom static route entries (`ip route`), interface IP assignments, ping diagnostic traces, and full network packet capture.
  * 🔗 **Artifacts & Packet Capture:** [R1.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/R1.txt) | [Packet Capture.pcapng](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/Packet%20Capture.pcapng)
* 🔗 **Documentation:** [gns3-topologies/README.md](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/README.md)

---

### 3. 🧪 Cisco Packet Tracer Labs (`packet-tracer-labs/`)
Hands-on Cisco Packet Tracer (`.pkt`) lab exercises building practical proficiency in CCNA-level networking fundamentals:

| Lab File | Focus Area & Skills Covered |
| :--- | :--- |
| 🔹 [Day 01 Lab - Packet Tracer Introduction.pkt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/Day%2001%20Lab%20-%20Packet%20Tracer%20Introduction.pkt) | UI orientation, device deployment, workspace configuration |
| 🔹 [Day 02 Lab - Connecting Devices.pkt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/Day%2002%20Lab%20-%20Connecting%20Devices.pkt) | Media types, straight-through vs cross-over cabling, serial link setup |
| 🔹 [Day 03 Lab - OSI Model.pkt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/Day%2003%20Lab%20-%20OSI%20Model.pkt) | Packet inspection, PDU encapsulation/decapsulation analysis |
| 🔹 [Day 04 Lab - Basic Device Security.pkt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/Day%2004%20Lab%20-%20Basic%20Device%20Security.pkt) | Executive mode passwords, enable secret, SSH setup, banner message |
| 🔹 [Day 06 Lab - Ethernet LAN Switching.pkt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/Day%2006%20Lab%20-%20Ethernet%20LAN%20Switching.pkt) | MAC address table learning, collision domains, VLAN fundamentals |
| 🔹 [Day 08 Lab - IPv4 Addresses.pkt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/Day%2008%20Lab%20-%20IPv4%20Addresses.pkt) | IPv4 addressing schemes, subnetting, default gateways |
| 🔹 [Day 09 Lab - Interface Configuration.pkt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/Day%2009%20Lab%20-%20Interface%20Configuration.pkt) | Speed/duplex negotiation, IP configuration on CLI, interface descriptions |

* 🔗 **Documentation:** [packet-tracer-labs/README.md](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/README.md)

---

### 4. 🐍 Python Security Automation Toolkit (`python-network-tools/Automations/`)
Custom Python security tools designed to automate network audits, reconnaissance, incident response playbooks, and log sanitization.

* 🔍 **[Network Port Scanner project.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/Network%20Port%20Scanner%20project.py)**: Multi-threaded port scanner utilizing Python `socket`, `threading`, and `Queue`. Supports single IPs, range scans, CIDR subnets (`/24`), and service shortcuts (`http`, `ssh`, `ftp`), outputting structured logs to `scan_log.txt`.
* 🛡️ **[security_playbook_automation.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/security_playbook_automation.py)**: Automated Incident Response (IR) playbook simulating SIEM detection of brute-force attacks and executing containment workflows (IP quarantine, user lockout) logged to `security_audit.log`.
* 🧹 **[har_remover.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/har_remover.py)**: Privacy compliance script using `json` and `re` regex to sanitize HTTP Archive (`.har`) files by stripping sensitive headers (`Authorization`, `Cookie`) and masking email addresses prior to sharing.
* 🧱 **[Cisco Firewall.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/Cisco%20Firewall.py)**: Cisco Access Control List (ACL) simulator demonstrating first-match rule processing and packet filtering logic.
* 🎲 **[Iteration-Control-and-Randomized-Audit-Tools.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/Iteration-Control-and-Randomized-Audit-Tools.py)**: Multi-region network audit stress-simulator with randomized 20% failure chaos gates across global nodes (London, USA, China).
* 🏹 **[subdomain_finder.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/subdomain_finder.py)**: Automated HTTP/HTTPS subdomain discovery tool to identify exposed attack surface endpoints.
* 🕵️ **[web_scraper.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/web_scraper.py)**: Lightweight OSINT scraper using `requests` and `BeautifulSoup` to extract domain header metadata.
* 📂 **[file_organizer.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/file_organizer.py)**: System utility that automatically categorizes messy download directories into organized file-type folders.
* 🔗 **Documentation:** [python-network-tools/Automations/Readme.md](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/Readme.md)

---

## 💻 Tech Stack & Key Competencies

* **Networking & Protocols:** IPv4/IPv6 Subnetting, TCP/IP Model, OSI Model, ICMP, DHCP, OSPF, VLANs, PVST Spanning Tree, Static Routing.
* **Network Emulation & Security:** Cisco IOS, GNS3, Cisco Packet Tracer, Wireshark (PCAP Analysis), Access Control Lists (ACLs), Firewall Rule Hardening.
* **Programming & Automation:** Python 3 (Socket Programming, Multi-threading, Regex, Requests, BeautifulSoup, JSON Parsing), PowerShell, Bash.
* **Security & Operations:** Offensive Security, Threat Detection, Incident Response Playbook Automation, Log Sanitization (PII/HAR Redaction), OSINT.

---

## 🚀 Getting Started & Execution Guide

### Prerequisites
* **Python 3.8+**
* **Cisco Packet Tracer 8.0+** (for `.pkt` lab files)
* **GNS3 Environment** (for GNS3 topology files)
* **Wireshark** (for PCAP traffic file inspection)

### Python Automation Quickstart
```bash
# Clone the repository
git clone https://github.com/S23rez/Network-Projects.git
cd Network-Projects/python-network-tools/Automations

# Run the Multi-Threaded Port Scanner
python "Network Port Scanner project.py"

# Run the Automated Security Incident Playbook
python security_playbook_automation.py

# Run the HAR Log Privacy Sanitizer
python har_remover.py
```

---

## 👤 Author & Contact

**Odunuga Fatai Olayinka**
* **Role:** Cybersecurity Student | Python Automation Specialist | Network Engineer
* **GitHub:** [@S23rez](https://github.com/S23rez)
* **Portfolio Repository:** [Network-Projects](https://github.com/S23rez/Network-Projects)

---
*Maintained with precision for network engineering & cybersecurity excellence.*
