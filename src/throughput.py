import subprocess
import json

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()

def run_iperf_test(server_ip='127.0.0.1', protocol='tcp', time=10):
    proto_flag = '' if protocol == 'tcp' else '-u'
    cmd = f"iperf3 -c {server_ip} {proto_flag} -t {time} -J"
    output = run_cmd(cmd)
    # Read the JSON
    try:
        data = json.loads(output)
        if protocol == 'tcp':
            speed = data['end']['sum_received']['bits_per_second']
        else:
            speed = data['end']['sum']['bits_per_second']
        return {'protocol': protocol, 'speed_bps': speed}
    except:
        return {'protocol': protocol, 'error': 'Failed to parse iperf3 output'}

def run_iperf_tests(server_ip='127.0.0.1'):
    tcp = run_iperf_test(server_ip, 'tcp')
    udp = run_iperf_test(server_ip, 'udp')
    return {'tcp': tcp, 'udp': udp}

