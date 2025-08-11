import json
import os
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
