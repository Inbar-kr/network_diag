# Network Diagnostics & Performance Testing Automation

## Project Overview  
network_diag is an automated network diagnostics and performance testing suite built with Python designed to validate key networking components and protocols on Ubuntu systems. It automates checking NIC status, IP configuration, MTU/jumbo frames support, link up/down monitoring, DNS resolution, packet loss, and throughput testing (TCP/UDP) using tools like iperf3.

This project helps verify hardware and network software health, ensuring network interfaces and configurations are working properly. It generates detailed reports for easy analysis and supports troubleshooting network issues in environments similar to production hardware testing labs.

## Key Features  
- **NIC Detection:** Verify network interfaces, MAC addresses, drivers, and firmware status.  
- **IP & Subnet Check:** Confirm IP address and subnet mask configurations.  
- **MTU & Jumbo Frames:** Test maximum packet sizes allowed by the network.  
- **Link Up/Down Monitoring:** Track changes in network link status over time.  
- **DNS Resolution Checks:** Validate domain name system lookups and response times.  
- **Packet Loss Detection:** Use ping and packet capture to detect dropped packets.  
- **Throughput Testing:** Measure network speed over TCP and UDP with iperf3.  
- **VLAN Testing (optional):** Verify VLAN connectivity and firewall rules.  
- **Reporting:** Generate human-readable HTML and JSON reports summarizing all tests.  

## Tech Stack  
- **Language:** Python 3  
- **Tools:** iperf3, ethtool, tcpdump, dig, ping  
- **Libraries:** psutil, scapy, jinja2, pandas, matplotlib  
- **OS:** Ubuntu (recommended for testing and deployment)  

## Prerequisites  
Ensure you have the following installed on your Ubuntu system:  
- Python 3.6+  
- iperf3  
- ethtool  
- tcpdump  
- dnsutils  
- net-tools  
- Python packages from `requirements.txt`  

## Installation  
1. Clone or download this repository.  
2. Create and activate a Python virtual environment:  
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```  
3. Install Python dependencies:  
    ```bash
    pip install -r requirements.txt
    ```  
4. Install system packages:  
    ```bash
    sudo apt update
    sudo apt install -y iperf3 ethtool tcpdump dnsutils net-tools
    ```  

## Running Tests Locally  
Run all network diagnostics and performance tests:  
    ```bash
    python src/main.py
    ``` 

## Reporting
- Results from each run are saved in the reports/ folder as JSON and HTML files.
- Packet captures (pcap files) are saved in the captures/ folder for deeper analysis.

##### Note: This project is a personal and educational portfolio project. It is not intended for redistribution or external use.