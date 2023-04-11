import re
import subprocess

def get_active_interfaces():
    try:
        output = subprocess.check_output(["ifconfig"]).decode("utf-8")
    except subprocess.CalledProcessError:
        return []

    interfaces = re.findall(r'^(\w+):.*<.*,RUNNING,.*>', output, re.MULTILINE)
    active_interfaces = []

    for interface in interfaces:
        inet_match = re.search(rf'{interface}:.*\n\s+inet\s', output, re.MULTILINE)
        if inet_match:
            active_interfaces.append(interface)

    return active_interfaces

active_interfaces = get_active_interfaces()