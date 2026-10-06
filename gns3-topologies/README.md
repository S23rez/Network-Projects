# 🛰️ GNS3 Topologies & Network Simulations

[![GNS3](https://img.shields.io/badge/GNS3-Network%20Simulation-orange.svg)](https://www.gns3.com)
[![Cisco IOS](https://img.shields.io/badge/Cisco%20IOS-15.9%20%7C%2015.2-blue.svg)](https://www.cisco.com)
[![Wireshark](https://img.shields.io/badge/Traffic%20Analysis-Wireshark%20PCAP-1679A7.svg)](https://www.wireshark.org)

This directory contains multi-device enterprise network topology simulations built and tested in **GNS3** (Graphical Network Simulator-3). Each lab includes full terminal configuration logs, network architecture topology diagrams, step-by-step verification traces, and live PCAP packet captures.

---

## 📁 Lab Index & Topology Overview

```text
gns3-topologies/
├── 📄 README.md                        <- Parent GNS3 Documentation
├── 📂 Lab 1/                          <- Multi-Subnet Router & Switch DHCP Infrastructure
│   ├── 📄 README.md                    <- Lab 1 Documentation & DHCP Pool Specs
│   ├── 📄 Router.txt                  <- Cisco IOS 15.9 Router Configuration & DHCP Pools
│   ├── 📄 Switch 1.txt                <- Layer 2 Switch 1 Configuration
│   ├── 📄 Switch 2.txt                <- Layer 2 Switch 2 Configuration
│   ├── 📄 Switch 3.txt                <- Layer 2 Switch 3 Configuration
│   ├── 🖼️ Topology.jpg                <- Visual Topology Diagram
│   └── 🖼️ 1.jpg - 12.jpg              <- Verification & Console Screen Captures
└── 📂 Lab 2 Static Routing/           <- Multi-Router Static Routing Topology & PCAP Capture
    ├── 📄 README.md                    <- Lab 2 Documentation & Routing Table Details
    ├── 📄 R1.txt                      <- Router 1 Terminal Capture & Static Routing setup
    ├── 📄 R2.txt                      <- Router 2 Terminal Capture
    ├── 📄 R3.txt                      <- Router 3 Terminal Capture
    ├── 📄 R4.txt                      <- Router 4 Terminal Capture
    ├── 📄 VPC1.txt                    <- Virtual PC 1 Terminal Logs
    ├── 📄 VPC2.txt                    <- Virtual PC 2 Terminal Logs
    ├── 🦈 Packet Capture.pcapng       <- Live Wireshark Packet Capture Trace
    ├── 🖼️ Topology.jpg                <- Network Topology Overview
    └── 🖼️ Topology Capture session.jpg <- Wireshark Capture Session Layout
```

---

## 🔬 Lab Descriptions & Technical Highlights

### 🧪 Lab 1: Multi-Subnet Router & Switch DHCP Infrastructure
* **Objective:** Implement inter-subnet routing and centralized multi-pool DHCP server configuration across Class A, B, and C subnets on Cisco IOS v15.9.
* **Key Components:** Custom IP DHCP pools (`POOL-10`, `POOL-172`, `POOL-192`), gateway configurations (`10.0.0.254`, `172.16.0.254`, `192.168.0.254`), PVST Spanning Tree, and PortFast edge configurations.
* 🔗 **Dedicated Documentation:** [gns3-topologies/Lab 1/README.md](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/README.md)
* 🔗 **Device Logs:** [Router.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/Router.txt) | [Switch 1.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/Switch%201.txt) | [Switch 2.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/Switch%202.txt) | [Switch 3.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/Switch%203.txt)

---

### 🧪 Lab 2: Multi-Router Static Routing & Wireshark PCAP Analysis
* **Objective:** Establish static routing paths across a multi-router topology (R1–R4, VPC1–VPC2) with end-to-end ICMP verification and PCAP traffic analysis.
* **Key Components:** Custom static route entries (`ip route`), interface IP assignments, ping diagnostic traces, and full network packet capture.
* 🔗 **Dedicated Documentation:** [gns3-topologies/Lab 2 Static Routing/README.md](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/README.md)
* 🔗 **Artifacts & Packet Capture:** [R1.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/R1.txt) | [Packet Capture.pcapng](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/Packet%20Capture.pcapng)

---

## 🛠️ How to Open & Inspect

1. **Topology Viewing:** Open `.jpg` image files in any image viewer.
2. **Wireshark Analysis:** Open `Packet Capture.pcapng` in [Wireshark](https://www.wireshark.org/) to inspect packet headers, ICMP requests/replies, ARP broadcasts, and frame details.
3. **GNS3 Deployment:** Import configurations directly into your GNS3 router nodes running Cisco IOS v15.x.

---

## 👤 Author

**Odunuga Fatai Olayinka** — Cybersecurity Student & Network Engineer  
GitHub: [@S23rez](https://github.com/S23rez)
