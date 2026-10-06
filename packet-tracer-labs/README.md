# 🧪 Cisco Packet Tracer Networking Labs

[![Packet Tracer](https://img.shields.io/badge/Cisco-Packet%20Tracer%208.0%2B-049fd9.svg)](https://www.netacad.com/courses/packet-tracer)
[![Curriculum](https://img.shields.io/badge/CCNA-Curriculum%20Labs-green.svg)](https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html)

This directory contains interactive Cisco Packet Tracer (`.pkt`) lab files structured around core networking principles, Cisco CCNA curriculum competencies, and hands-on CLI configuration skills.

---

## 📋 Lab Directory & Module Index

```text
packet-tracer-labs/
├── 📄 README.md                                                    <- Module Documentation
├── 🧪 Day 01 Lab - Packet Tracer Introduction.pkt                  <- Environment & Interface Setup
├── 🧪 Day 02 Lab - Connecting Devices.pkt                          <- Cabling & Interface Interconnections
├── 🧪 Day 03 Lab - OSI Model.pkt                                   <- PDU Encapsulation & Packet Tracing
├── 🧪 Day 04 Lab - Basic Device Security.pkt                       <- Passwords, Enable Secret, SSH & Banners
├── 🧪 Day 06 Lab - Ethernet LAN Switching.pkt                      <- Switching, MAC Tables & Broadcast Domains
├── 🧪 Day 08 Lab - IPv4 Addresses.pkt                              <- Subnetting & IP Host Assignment
└── 🧪 Day 09 Lab - Interface Configuration.pkt                     <- Interface Speed, Duplex & Descriptions
```

---

## 🔬 Detailed Lab Modules & Skill Breakdown

### 1. 🔹 [Day 01 Lab - Packet Tracer Introduction.pkt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/Day%2001%20Lab%20-%20Packet%20Tracer%20Introduction.pkt)
* **Objective:** Familiarization with the Cisco Packet Tracer visual workspace, device palette, and Logical/Physical view modes.
* **Key Skills:** Navigating workspace controls, placing routers/switches/end-hosts, and inspecting device modules.

---

### 2. 🔹 [Day 02 Lab - Connecting Devices.pkt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/Day%2002%20Lab%20-%20Connecting%20Devices.pkt)
* **Objective:** Selecting and cabling physical network interfaces based on device roles.
* **Key Skills:** Copper Straight-Through cabling (PC to Switch), Copper Cross-Over cabling (Switch to Switch / Router to PC), and Serial interface connections.

---

### 3. 🔹 [Day 03 Lab - OSI Model.pkt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/Day%2003%20Lab%20-%20OSI%20Model.pkt)
* **Objective:** Visualizing OSI model layers and PDU encapsulation/decapsulation in Simulation Mode.
* **Key Skills:** Inspecting Layer 2 Data Link frames, Layer 3 Network IP headers, Layer 4 Transport segments, ICMP echo flows, and ARP requests.

---

### 4. 🔹 [Day 04 Lab - Basic Device Security.pkt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/Day%2004%20Lab%20-%20Basic%20Device%20Security.pkt)
* **Objective:** Hardening Cisco IOS switch and router management access against unauthorized intrusion.
* **Key Skills:** 
  * Configuring `enable secret` password hashing.
  * Console line (`line con 0`) and VTY line (`line vty 0 15`) password protection.
  * Encrypting plain-text passwords with `service password-encryption`.
  * Provisioning SSH remote access with RSA keys (`crypto key generate rsa`).
  * Creating MOTD security banners (`banner motd`).

---

### 5. 🔹 [Day 06 Lab - Ethernet LAN Switching.pkt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/Day%2006%20Lab%20-%20Ethernet%20LAN%20Switching.pkt)
* **Objective:** Understanding Layer 2 Ethernet switching operations and frame forwarding logic.
* **Key Skills:** Dynamic MAC address learning (`show mac address-table`), frame flooding on unknown unicast, broadcast domain isolation, and collision domain segmentation.

---

### 6. 🔹 [Day 08 Lab - IPv4 Addresses.pkt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/Day%2008%20Lab%20-%20IPv4%20Addresses.pkt)
* **Objective:** Designing and applying Classful/Classless IPv4 addressing and subnet masks across network hosts.
* **Key Skills:** Subnetting logic, assigning host IP addresses, subnet masks, default gateways, and verifying intra-subnet reachability with `ping`.

---

### 7. 🔹 [Day 09 Lab - Interface Configuration.pkt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/Day%2009%20Lab%20-%20Interface%20Configuration.pkt)
* **Objective:** Configuring and troubleshooting Cisco IOS Ethernet interfaces on routers and switches.
* **Key Skills:** Setting interface IP addresses (`ip address`), interface descriptions (`description`), speed/duplex modes (`speed auto`, `duplex auto`), bringing interfaces up (`no shutdown`), and checking interface status (`show ip interface brief`).

---

## 🚀 How to Run the Labs

1. Download and install **Cisco Packet Tracer 8.0** (or newer) from Cisco Networking Academy.
2. Double-click any `.pkt` file in this directory to open it in Packet Tracer.
3. Switch between **Realtime** and **Simulation** modes to inspect network behavior and complete instructions.

---

## 👤 Author

**Odunuga Fatai Olayinka** — Cybersecurity Student & Network Engineer  
GitHub: [@S23rez](https://github.com/S23rez)
