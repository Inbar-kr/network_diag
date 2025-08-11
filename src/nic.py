import os
import subprocess

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode()
    except Exception as e:
        return str(e)

def list_interfaces():
        # List all interfaces except loopback
    return [iface for iface in os.listdir('/sys/class/net') if iface != 'lo']

# Collects the MAC address, driver name, and firmware version of one network card
def get_nic_info(iface):
    info = {'interface': iface}
    try:
        with open(f'/sys/class/net/{iface}/address') as f:
            info['mac'] = f.read().strip()
    except:
        info['mac'] = None

    # Get driver and firmware info with ethtool
    ethtool_output = run_cmd(f"ethtool -i {iface}")
    for line in ethtool_output.splitlines():
        if 'driver:' in line:
            info['driver'] = line.split(':')[1].strip()
        if 'firmware-version:' in line:
            info['firmware'] = line.split(':')[1].strip()
    return info

# Check info about all network cards
def check_nics():
    nics = list_interfaces()
    results = []
    for nic in nics:
        results.append(get_nic_info(nic))
    return results
