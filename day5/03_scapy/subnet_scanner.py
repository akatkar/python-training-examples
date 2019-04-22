from scapy.all import *

# for lsb in range(1,50):
#     ip = f'192.168.1.{lsb}'
#     arp_request = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
#     arp_response = srp1(arp_request, timeout=1, verbose=0)
#     if arp_response:
#         print("IP:", arp_response.psrc, "MAC:" + arp_response.hwsrc)

pkts = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="172.20.44.*", hwdst="ff:ff:ff:ff:ff:ff")
ans,un = srp(pkts, timeout=1, verbose=0)
ans.summary(lambda p: p[1].sprintf("IP %psrc% MAC: %hwsrc%"))
