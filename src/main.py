from nic import check_nics
from ip_check import check_ip_info
from mtu_test import run_mtu_test
from link_monitor import monitor_link_once
from throughput import run_iperf_tests
from dns_check import test_dns
from utils import save_report, log, start_packet_capture, stop_packet_capture


def main():
    log("Starting network diagnostics")

    start_packet_capture(interface="enp0s3")

    report = {}
    try:
        log("Checking NICs...")
        report['nic'] = check_nics()

        log("Checking IP configuration...")
        report['ip'] = check_ip_info()

        log("Testing MTU / Jumbo Frames...")
        report['mtu'] = run_mtu_test()

        log("Checking Link status...")
        report['link'] = monitor_link_once()

        log("Running throughput tests (iperf3)...")
        report['throughput'] = run_iperf_tests()

        log("Testing DNS resolution...")
        report['dns'] = test_dns()

        save_report(report)
        log("Report saved to reports/report.json")

    finally:
        stop_packet_capture()

    log("Network diagnostics completed.")

if __name__ == "__main__":
    main()
