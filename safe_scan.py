#importing the libaries 
import nmap #python-nmap library for scanning and port detection
import ipaddress #for handling and manipulating IP addresses and networks
from tabulate import tabulate #for formatting the output in a table format

#function for scanning the network/single ip address
def scan_network(cidr):
    nm = nmap.PortScanner()
    try:
        if '/' in cidr:
            #CIDR Network range
            network = ipaddress.ip_network(cidr, strict=False)
            all_hosts = [str(ip) for ip in network.hosts()]
        else:
            # Single IP
            ipaddress.ip_address(cidr) 
            all_hosts = [cidr]
    except ValueError:
        print(f"Invalid input: {cidr}")
        return

    print(f"\n🔍 Scanning {len(all_hosts)} host(s)...")

   #looping through all the hosts
    for host in all_hosts:
       
        print(f"\nScanning host: {host}")
        nm.scan(hosts=host, arguments='-sT') 
     # connection scan using  protocols 

        if host in nm.all_hosts() and nm[host].state() == 'up':
            print("-" * 46)
            print(f"Host: {host} is up")
            print("-" * 46)

            table = []
            #looping through all the protocols and ports
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                print(lport)
                #looping through all the ports
                for port in sorted(lport):
                    print(nm[host].keys())
                    table.append([proto, port, nm[host][proto][port]['state']])
                # Detailed host information
                print("-" * 46)
                print(f"Host status dict: {nm[host]['status']}")
                print("-" * 46)
         
            # Displaying the results in a table format
            if table:
                print(tabulate(table, headers=["Protocol", "Port", "State"], tablefmt="grid"))
            else:
                print("No open ports found.")
        else:
            print(f" Host: {host} is down or not found in scan")


if __name__ == "__main__":
    #scan_network('ur address')       # Single host (check for typo)
    scan_network('urnetwork')      # Network range
