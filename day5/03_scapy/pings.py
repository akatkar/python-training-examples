from scapy.all import *

def arp_ping():
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"),timeout=2)
    ans.summary(lambda x: x[1].sprintf("%Ether.src% %ARP.psrc%"))

def icmp_ping():
    ans, unans = sr(IP(dst="192.168.1.1-20") / ICMP(),timeout=2)
    ans.summary(lambda p: p[1].sprintf("%IP.src% is alive"))


def tcp_ping():
    ans, unans = sr(IP(dst="192.168.1.*") / TCP(dport=80, flags="S"),timeout=3)
    ans.summary(lambda p: p[1].sprintf("%IP.src% is alive"))


def udp_ping():
    ans, unans = sr(IP(dst="192.168.*.1-10") / UDP(dport=0))
    ans.summary(lambda p: p[1].sprintf("%IP.src% is alive"))


def main():
    # arp_ping()
    # arping("192.168.1.*")
    # icmp_ping()
    tcp_ping()

if __name__ == '__main__':
    main()