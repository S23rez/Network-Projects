# 🧪 Lab 1: Multi-Subnet Router & Switch DHCP Infrastructure

[![GNS3](https://img.shields.io/badge/GNS3-Lab%201-orange.svg)](https://www.gns3.com)
[![Cisco IOS](https://img.shields.io/badge/Cisco%20IOS-15.9%20%7C%2015.2-blue.svg)](https://www.cisco.com)
[![Topic](https://img.shields.io/badge/Topic-DHCP%20Pools%20%26%20Subnetting-green.svg)](https://github.com/S23rez/Network-Projects)

Welcome to **Lab 1** of the GNS3 Topology Series. This lab demonstrates multi-subnet inter-VLAN routing, dynamic host configuration using Cisco IOS DHCP pools, and Layer 2 switch portfast configurations across Class A, Class B, and Class C networks.

---

## 📐 Network Topology & Addressing Architecture

```text
               +-----------------------+
               |        Router         |
               | (Cisco IOS v15.9)     |
               +-----------+-----------+
                           |
        +------------------+------------------+
        |                  |                  |
   Gi0/0 (Class A)    Gi0/2 (Class B)    Gi0/1 (Class C)
   10.0.0.254/8       172.16.0.254/16    192.168.0.254/24
        |                  |                  |
+-------+-------+  +-------+-------+  +-------+-------+
|   Switch 1    |  |   Switch 3    |  |   Switch 2    |
| (Cisco IOSv)  |  | (Cisco IOSv)  |  | (Cisco IOSv)  |
+-------+-------+  +-------+-------+  +-------+-------+
        |                  |                  |
    End Devices        End Devices        End Devices
   (DHCP Clients)     (DHCP Clients)     (DHCP Clients)
```

---

## ⚙️ Subnet & DHCP Pool Breakdown

| Interface | Network Subnet | Default Gateway | Excluded IP | DHCP Pool Name | DNS Server |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GigabitEthernet0/0** | `10.0.0.0/8` | `10.0.0.254` | `10.0.0.254` | `POOL-10` | `8.8.8.8` |
| **GigabitEthernet0/2** | `172.16.0.0/16` | `172.16.0.254` | `172.16.0.254` | `POOL-172` | `8.8.8.8` |
| **GigabitEthernet0/1** | `192.168.0.0/24` | `192.168.0.254` | `192.168.0.254` | `POOL-192` | `8.8.8.8` |

---

## 📄 Device Configuration Files

* 📄 **[Router.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/Router.txt)**: Full running configuration of the core Cisco IOS router. Contains IP DHCP pool declarations, excluded IP addresses, interface descriptions, and CEF enablement.
* 📄 **[Switch 1.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/Switch%201.txt)**: Configuration for Switch 1 featuring PVST Spanning Tree and `spanning-tree portfast edge` on host interfaces Gi0/0 and Gi0/1.
* 📄 **[Switch 2.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/Switch%202.txt)**: Configuration for Switch 2.
* 📄 **[Switch 3.txt](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/Switch%203.txt)**: Configuration for Switch 3.

---

## 🖼️ Visual Topology & Verification Screenshots

* 🖼️ **[Topology Diagram](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/gns3-topologies/Lab%201/Topology.jpg)**: GNS3 graphical topology view.
* 🖼️ **Lab Screenshots (`1.jpg` – `12.jpg`)**: Step-by-step console verification capture showing:
  * Dynamic IP address acquisition via DHCP on end hosts.
  * ICMP reachability ping tests across subnets.
  * Router `show ip dhcp binding` and interface status verification.

---

## 🛠️ Key Cisco IOS Commands Used

```cisco
! Exclude default gateway IPs from dynamic DHCP distribution
ip dhcp excluded-address 10.0.0.254
ip dhcp excluded-address 172.16.0.254
ip dhcp excluded-address 192.168.0.254

! Define DHCP Pools
ip dhcp pool POOL-10
 network 10.0.0.0 255.0.0.0
 default-router 10.0.0.254
 dns-server 8.8.8.8

! Enable PortFast on Switch interfaces
interface GigabitEthernet0/0
 negotiation auto
 spanning-tree portfast edge
```

---

## 👤 Author

**Odunuga Fatai Olayinka** — Cybersecurity Student & Network Engineer  
GitHub: [@S23rez](https://github.com/S23rez)
