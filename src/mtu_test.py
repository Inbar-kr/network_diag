import subprocess

def run_cmd(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()
    
def get_mtu(iface='enp0s3'):
    cmd = f"cat /sys/class/net/{iface}/mtu"
    return run_cmd(cmd).strip()

def ping_mtu_test(target_ip='8.8.8.8', size=8972):
    cmd = f"ping -c 3 -M do -s {size} {target_ip}"
    output = run_cmd(cmd)
    success = "0% packet loss" in output
    return {'ping_output': output, 'jumbo_frames_supported': success}

def run_mtu_test(iface='enp0s3', target_ip='8.8.8.8'):
    mtu = get_mtu(iface)
    ping_test = ping_mtu_test(target_ip)
    return {'mtu': mtu, **ping_test}

