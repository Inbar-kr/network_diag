import json
import os
from datetime import datetime

LOG_FILE = os.path.join('captures', 'network_diag.log')

def save_report(data, path='reports/report.json'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def log(msg):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{now}] {msg}"
    print(line)

    # Make sure captures/ folder exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    # Append log line to file
    with open(LOG_FILE, 'a') as f:
        f.write(line + '\n')
