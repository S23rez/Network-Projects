def firewall_check(source_ip, protocol, destination_port):
    """
    Simulates the Cisco ACL First-Match logic for Router3.
    """
    acl_rules = [
        {"action": "PERMIT", "source": "192.168.60.3", "port": 22}, # Rule 1 (Admin PC)
        {"action": "DENY",   "source": "any",          "port": 22}, # Rule 2 (Block others)
        {"action": "PERMIT", "source": "any",          "port": "any"} # Rule 3 (Allow rest)
    ]

    print(f"--- Processing packet from {source_ip} (Port: {destination_port}) ---")

    for rule in acl_rules:
        source_match = (rule["source"] == "any" or rule["source"] == source_ip)
        port_match = (rule["port"] == "any" or rule["port"] == destination_port)

        if source_match and port_match:
            return f"MATCH FOUND: {rule['action']} with {protocol} Protocol (Rule logic stopped here.)"

    return "DENY (Implicit deny)"

print(firewall_check("192.168.60.3", "TCP", 22))

print(firewall_check("172.168.10.5", "TCP", 22))

print(firewall_check("172.168.10.5", "TCP", 80))