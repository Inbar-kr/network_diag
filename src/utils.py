import json
import os
import shutil
import signal
import subprocess
from datetime import datetime

def save_report(data, path='reports/report.json'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def log(msg, level='INFO'):
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    level = level.upper()
    log_msg = f"[{timestamp}] [{level}] {msg}"

    print(log_msg)

    log_dir = 'captures'
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, now.strftime('%Y-%m-%d') + '.log')

    with open(log_file, 'a') as f:
        f.write(log_msg + '\n')

def save_pcap(src_path, folder='captures'):
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    dest_path = os.path.join(folder, f'capture_{timestamp}.pcap')
    shutil.copy2(src_path, dest_path)
    return dest_path

# === Packet capture management ===

_capture_process = None
_capture_tmp_file = None

def start_packet_capture(interface='eth0'):
    global _capture_process, _capture_tmp_file

    if _capture_process:
        log("Packet capture already running!", level="WARNING")
        return

    os.makedirs('captures', exist_ok=True)

    # Temporary file for capture
    tmp_filename = f"capture_tmp_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pcap"
    _capture_tmp_file = os.path.join('/tmp', tmp_filename)

    log(f"Starting packet capture on interface '{interface}' -> {_capture_tmp_file}")

    # Start tcpdump as a background process
    _capture_process = subprocess.Popen(
        ["tcpdump", "-i", interface, "-w", _capture_tmp_file],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def stop_packet_capture():
    global _capture_process, _capture_tmp_file

    if not _capture_process:
        log("No packet capture is running.", level="WARNING")
        return None

    log("Stopping packet capture")

    # Send SIGINT to allow clean tcpdump exit and flush
    _capture_process.send_signal(signal.SIGINT)

    try:
        _capture_process.wait(timeout=10)  # wait longer for clean shutdown
    except subprocess.TimeoutExpired:
        log("tcpdump did not exit in time, killing it...", level="WARNING")
        _capture_process.kill()
        _capture_process.wait()

    saved_path = None
    if _capture_tmp_file and os.path.exists(_capture_tmp_file):
        saved_path = save_pcap(_capture_tmp_file)
        os.remove(_capture_tmp_file)
        log(f"Packet capture saved to {saved_path}")
        log(f"File exists? {os.path.exists(saved_path)}")
    else:
        log("Temporary capture file NOT found or already removed!", level="ERROR")

    _capture_process = None
    _capture_tmp_file = None

    return saved_path