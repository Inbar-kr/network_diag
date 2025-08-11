import subprocess
import json

def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode()

def check_ip_info():
    # Uses ip command JSON output
    result = {}
    output = run_cmd("ip -j addr show")
    data = json.loads(output)
    for iface in data:
        if iface['ifname'] != 'lo':
            addrs = iface.get('addr_info', [])
            ipv4 = [a['local'] for a in addrs if a['family'] == 'inet']
            if ipv4:
                result[iface['ifname']] = ipv4[0]
    return result
