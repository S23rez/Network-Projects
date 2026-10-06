# 🛡️ Cybersecurity Automation & Intelligence Toolkit

[![Author](https://img.shields.io/badge/Developer-Odunuga%20Fatai%20Olayinka-blue.svg)](https://github.com/S23rez)
[![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg)](https://python.org)
[![Category](https://img.shields.io/badge/Category-Cybersecurity%20Automation%20%26%20OSINT-red.svg)](https://github.com/S23rez/Network-Projects)

**Developed by Odunuga Fatai Olayinka**  
*Cybersecurity Student | Python Automation Specialist | Network Analyst*

This directory is a curated collection of professional-grade Python scripts designed to automate critical security workflows, perform network reconnaissance, execute SIEM incident response playbooks, strip sensitive PII from HAR traffic captures, and assist in Open-Source Intelligence (OSINT) investigations.

---

## 🚀 Featured Security Tools

### 1. 🔍 Advanced Network Port Scanner
* 📄 **File:** [Network Port Scanner project.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/Network%20Port%20Scanner%20project.py)
* **Purpose:** Rapidly identifies active services and open attack vectors across single hosts, IP ranges, or subnets.
* **Technical Highlights:** Built with Python’s `socket`, `threading`, and `Queue` for high-performance concurrent multithreaded scanning. Supports IP ranges (`192.168.1.1-20`), CIDR notation (`192.168.1.0/24`), and service shortcuts (`http`, `ssh`, `ftp`). Logs findings to `scan_log.txt`.
* **Security Use Case:** Essential for initial reconnaissance during penetration testing or internal network auditing.

### 2. 🛡️ SIEM Detection & Incident Response Playbook Automator
* 📄 **File:** [security_playbook_automation.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/security_playbook_automation.py)
* **Purpose:** Automates the Incident Response (IR) lifecycle—from SIEM brute-force detection to automated containment actions.
* **Technical Highlights:** Simulates detection thresholds (`MAX_FAILED_ATTEMPTS = 5`), triggers automated containment steps (IP quarantine, user account lockouts, SOC notification), and appends audit logs to `security_audit.log`.
* **Security Use Case:** Automates Tier-1 SOC operations to reduce Mean Time to Respond (MTTR) during brute-force attacks.

### 3. 🧹 Network Log (HAR) Sanitizer & Privacy Redactor
* 📄 **File:** [har_remover.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/har_remover.py)
* **Purpose:** Redacts PII and sensitive credentials from HTTP Archive (`.har`) files before sharing for debugging.
* **Technical Highlights:** Leverages `json` and `re` regex to sanitize HAR files. Strips sensitive headers (`Authorization`, `Cookie`, `Set-Cookie`) and masks email addresses, outputting cleaned files to `Sanitized_Uploads/`.
* **Security Use Case:** Critical for Data Privacy Compliance (GDPR/HIPAA) and preventing accidental credential leakage during QA testing.

### 4. 🧱 Cisco Firewall & ACL Rule Simulator
* 📄 **File:** [Cisco Firewall.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/Cisco%20Firewall.py)
* **Purpose:** Automates and simulates Cisco Router Access Control List (ACL) first-match filtering logic.
* **Technical Highlights:** Scripted logic for evaluating inbound packets against IP and port rule tables, terminating execution on first matching `PERMIT` or `DENY` rule.
* **Security Use Case:** Validates ACL policy accuracy prior to deploying firewall rules to live production routers.

### 5. 🏗️ Multi-Region Iteration & Randomized Chaos Audit Simulator
* 📄 **File:** [Iteration-Control-and-Randomized-Audit-Tools.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/Iteration-Control-and-Randomized-Audit-Tools.py)
* **Purpose:** Models global infrastructure health checks across distributed multi-region nodes.
* **Technical Highlights:** Implements nested iteration loops across regional data centers (London, USA, China) with a 20% randomized failure probability gate.
* **Security Use Case:** Stress-tests SOC monitoring tools and automation logic against multi-region node failures.

### 6. 🏹 Subdomain Discovery Tool
* 📄 **File:** [subdomain_finder.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/subdomain_finder.py)
* **Purpose:** Maps an organization’s external attack surface by discovering active subdomains.
* **Technical Highlights:** Uses automated HTTP/HTTPS GET probes to test subdomains against target domains.
* **Security Use Case:** Critical for discovering unmonitored development servers or shadow IT assets.

### 7. 🕵️ OSINT Web Scraper
* 📄 **File:** [web_scraper.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/web_scraper.py)
* **Purpose:** Automates public intelligence harvesting from target web pages.
* **Technical Highlights:** Built with `requests` and `BeautifulSoup` featuring custom User-Agent headers.
* **Security Use Case:** Identifies public data leaks, exposed headlines, and domain metadata.

### 8. 📂 System Workflow Automator
* 📄 **File:** [file_organizer.py](file:///c:/Users/Suarez/My-Portfolios/Network-Projects/python-network-tools/Automations/file_organizer.py)
* **Purpose:** Categorizes cluttered directories into extension-based security storage bunkers.
* **Technical Highlights:** Uses `os` and `shutil` for file system sorting.
* **Security Use Case:** Maintains clean workstation hygiene for security logs and PCAP files.

---

## 🛠️ Execution Instructions

```bash
# Navigate to the automations folder
cd python-network-tools/Automations

# 1. Run Port Scanner
python "Network Port Scanner project.py"

# 2. Run Incident Response Playbook
python security_playbook_automation.py

# 3. Sanitize HAR files in current folder
python har_remover.py

# 4. Simulate Cisco Firewall ACL evaluation
python "Cisco Firewall.py"
```

---

## 👤 Author

**Odunuga Fatai Olayinka** — Cybersecurity Student & Python Automation Specialist  
GitHub: [@S23rez](https://github.com/S23rez)