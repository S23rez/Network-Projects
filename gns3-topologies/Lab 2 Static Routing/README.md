# 🧪 Lab 2: Multi-Router Static Routing & Traffic Analysis

[![GNS3](https://img.shields.io/badge/GNS3-Lab%202-orange.svg)](https://www.gns3.com)
[![Cisco IOS](https://img.shields.io/badge/Cisco%20IOS-vIOS-blue.svg)](https://www.cisco.com)
[![Wireshark](https://img.shields.io/badge/Traffic-Wireshark%20PCAP-1679A7.svg)](https://www.wireshark.org)

Welcome to **Lab 2** of the GNS3 Topology Series. This lab demonstrates static route configuration, multi-router routing table lookup, ICMP ping diagnostics, and live packet capture analysis using Wireshark across a multi-hop router topology.

---

## 📐 Network Architecture Overview

The network topology consists of 4 Cisco IOS Routers (**R1**, **R2**, **R3**, **R4**) and 2 Virtual PCs (**VPC1**, **VPC2**). Static routes are explicitly defined on each router to enable end-to-end communication across remote subnets.

---

## 📄 Device Logs & Configuration Traces

* 📄 **[R1.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/R1.txt)**: Terminal console capture for Router 1. Shows interface IP configuration (`192.168.10.1`, `192.168.20.1`, `192.168.30.1`), static route configuration (`ip route 192.168.50.0 255.255.255.0 192.168.30.3`), and routing table verification (`show ip route`).
* 📄 **[R2.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/R2.txt)**: Terminal console capture for Router 2.
* 📄 **[R3.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/R3.txt)**: Terminal console capture for Router 3.
* 📄 **[R4.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/R4.txt)**: Terminal console capture for Router 4.
* 📄 **[VPC1.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/VPC1.txt)**: Terminal logs for Virtual PC 1.
* 📄 **[VPC2.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/VPC2.txt)**: Terminal logs for Virtual PC 2.

---

## 🦈 Packet Capture & Visual Topology

* 🦈 **[Packet Capture.pcapng](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/Packet%20Capture.pcapng)**: Live Wireshark packet capture recording network traffic along static route links. Can be opened directly in Wireshark.
* 🖼️ **[Topology.jpg](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/Topology.jpg)**: Network topology diagram.
* 🖼️ **[Topology Capture session.jpg](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/Topology%20Capture%20session.jpg)**: Screen capture illustrating active Wireshark session setup on link interfaces.

---

## 🛠️ Static Routing Commands Used

```cisco
! Configure static route to 192.168.50.0/24 subnet via R3 (192.168.30.3)
R1(config)# ip route 192.168.50.0 255.255.255.0 192.168.30.3

! Configure static route to 192.168.60.0/24 subnet via R3 (192.168.30.3)
R1(config)# ip route 192.168.60.0 255.255.255.0 192.168.30.3

! Inspect Routing Table
R1# show ip route
```

---

## 👤 Author

**Odunuga Fatai Olayinka** — Cybersecurity Student & Network Engineer  
GitHub: [@S23rez](https://github.com/S23rez)
