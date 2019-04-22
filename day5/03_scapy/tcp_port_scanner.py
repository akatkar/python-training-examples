from scapy.all import *

def tcpPortScan():
    res, unans = sr( IP(dst="www.milliyet.com.tr")/TCP(flags="S", dport=(1,1024)) )
    res.nsummary( lfilter=lambda p: (p[1].haslayer(TCP) and (p[1].getlayer(TCP).flags & 2)))

