from scapy.all import Ether, IP, TCP, sendp, get_if_hwaddr

src_iface = "Wi-Fi"          # your Windows interface
src_mac = get_if_hwaddr(src_iface)

print(f"Source MAC: {src_mac}")
dst_mac = "ur mac address"  # Linux MAC (find with arp -a after ping)

pkt = Ether(src=src_mac, dst=dst_mac)/IP(dst="ur")/TCP(dport=50000, sport=40000, flags="PA")/b"Hello from Windows"
sendp(pkt, iface=src_iface,count=4,loop=1, inter=0.5,realtime=1)
