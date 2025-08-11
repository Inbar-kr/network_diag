def monitor_link_once(iface='enp0s3'):
    try:
        with open(f"/sys/class/net/{iface}/carrier") as f:
            carrier = f.read().strip()
        status = "up" if carrier == '1' else "down"
    except:
        status = "unknown"
    return {iface: status}

