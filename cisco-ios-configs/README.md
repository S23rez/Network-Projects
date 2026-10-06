# ⚙️ Cisco IOS Configuration & Hardening Repository

[![Cisco IOS](https://img.shields.io/badge/Cisco-IOS%2015.x-049fd9.svg)](https://www.cisco.com)
[![Category](https://img.shields.io/badge/Category-Network%20Hardening%20%26%20Security-blue.svg)](https://github.com/S23rez/Network-Projects)

This directory is dedicated to Cisco Internetwork Operating System (IOS) router and switch configuration files, security policy templates, and device hardening scripts.

---

## 🎯 Purpose & Scope

The configurations stored in this module are engineered to implement enterprise-grade security standards across Cisco routers and switches. Key operational areas include:

1. **Management Plane Hardening**
   * Encrypted credentials (`enable secret`, `service password-encryption`).
   * SSH v2 enforcement with AES-CTR encryption cipher suites.
   * Executive timeout constraints and login banner disclaimers.

2. **Control & Data Plane Filtering**
   * Standard and Extended Access Control Lists (ACLs).
   * First-match packet filtering policies.
   * Disabling unused management services (`no ip http server`, `no ip http secure-server`).

3. **Layer 2 & Layer 3 Interface Configuration**
   * Interface IP assignment, speed/duplex auto-negotiation, and interface descriptions.
   * PortFast edge configurations and PVST Spanning Tree protocol parameters.
   * DHCP server pool declarations with explicit excluded address ranges.

---

## 📂 Related Portfolio Links

* 🛰️ **GNS3 Topology Device Configs:** View live GNS3 lab configs in [Lab 1 Router Config](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/Router.txt) and [Lab 2 Static Routing R1 Config](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%202%20Static%20Routing/R1.txt).
* 🧪 **Cisco Packet Tracer Labs:** Explore hands-on Packet Tracer labs in [packet-tracer-labs/](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/packet-tracer-labs/README.md).
* 🐍 **Python Firewall Simulator:** Run the ACL simulator in [Cisco Firewall.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/Cisco%20Firewall.py).

---

## 👤 Author

**Odunuga Fatai Olayinka** — Cybersecurity Student & Network Engineer  
GitHub: [@S23rez](https://github.com/S23rez)
