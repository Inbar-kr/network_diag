import subprocess
import time

def test_dns(host='google.com', server=None):
    cmd = f"dig +short {host}" if not server else f"dig +time=2 @{server} {host}"
    start = time.time()
    try:
        output = subprocess.check_output(cmd, shell=True).decode().strip()
        duration = time.time() - start
        return {'host': host, 'server': server, 'response': output, 'time_sec': duration}
    except Exception as e:
        return {'error': str(e)}
