from scapy.all import *

# command list
lsc()

# protocol list
ls()
# show IP protocol
ls(IP)
ls(Ether)

# configuration
conf
conf.route
# (change promisc mode)

# generate a packet
ip_pkt = IP(dst="google.com")/ICMP()/"Ali was here"
ip_pkt.show()

ether_pkt = Ether()/IP(dst="google.com")/ICMP()/"XXX"
ether_pkt.show()

# ---------------------------------------------
# generate multiple packets
# ---------------------------------------------
# generate using list
a = IP(dst=["192.168.1","www.slashdot.org"])
# >>> a
# <IP  dst=['192.168.1', Net('www.slashdot.org')] |>
# [p for p in a]

# generate using IP Addess Mask: 30 means 32-30=2 bits address -> 2^2 = 4 IP packet
a = IP(dst="www.slashdot.org/30")
# >>> a
# <IP dst=Net('www.slashdot.org/30') |>
# [p for p in a]

# generate using wild card. * means all possible values
a = IP(dst="192.168.1.*")
# >>> a
# <IP  dst=Net('192.168.1.*') |>
# [p for p in a]

# generate using range. * means all possible values
a = IP(dst="192.168.1.20-30")
# >>> a
# <IP  dst=Net('192.168.1.20-30') |>
# [p for p in a]

# generate packets with different ports
c=TCP(dport=[80,443])
# >>> c
# <TCP  dport=['http', 'https'] |>
# [p for p in c]
# !
# [p for p in a/c]

# generate packets with different ttl
b = IP(ttl=[1, 2, (5, 9)])
# >>> a
# <IP  ttl=[1, 2, (5, 9)] |>
# [p for p in a]

# ---------------------------------------------
# Sending Packets
# ---------------------------------------------
# send packets at layer 3
send(ip_pkt)

# send packets at layer 2
sendp(ether_pkt)

# send packets continuously
sendp(ether_pkt, loop=1)

# send packets continuously with 1 second interval
sendp(ether_pkt, loop=1, inter=1)

# send 3 packets with 1 second interval
sendp(ether_pkt, loop=1, inter=1, count=3)

# ---------------------------------------------
# Sending & Receiving
# ---------------------------------------------
sr(ip_pkt)
# In Python _ (underscore) is the latest result
response, no_response = _

tcp_pkt = IP(dst="127.0.0.1")/TCP(dport=[23,8080,53])
sr1(tcp_pkt)

# sending as loop
srloop(IP(dst="www.target.com/30")/TCP())

# srploop for layer2
# ---------------------------------------------
# Make Table
# ---------------------------------------------
# ans, unans = sr(IP(dst=["192.168.1.1","yahoo.com","slashdot.org"])/TCP(dport=[22,80,443],flags="S"))
ipPkts = IP(dst=["192.168.1.1", "yahoo.com", "slashdot.org"])
tcpPkts = TCP(dport=[22, 80, 443], flags="S")
ans, unans = sr(ipPkts / tcpPkts)


# Use this one for Python 2.x
# ans.filter(lambda (s,r):TCP in r and r[TCP].flags&2).make_table(lambda (s,r):(s.dst, s.dport, "X"))
ans.filter(lambda p:TCP in p[1] and p[1][TCP].flags&2).make_table(lambda p:(p[0].dst, p[0].dport, "X"))


traceroute (["www.n11.com.tr"], maxttl=20)


# ---------------------------------------------
# Sniffing
# ---------------------------------------------
pkts = sniff(count=3)

pkts.summary()

pkts[0]
pkts[1]
pkts[2]

hexdump(pkts[0])

pkts[1].show()

# sniff only icmp
pkts = sniff(count=3, filter="icmp")
pkts

pkts = sniff(count=3, filter="icmp", prn=lambda x: x.summary())


a=sniff(filter="tcp and ( port 25 or port 110 )",prn=lambda x: x.sprintf("%IP.src%:%TCP.sport% -> %IP.dst%:%TCP.dport%  %2s,TCP.flags% : %TCP.payload%"))

# ---------------------------------------------
# Working with PCAP file
# ---------------------------------------------
# Writing pcap files
pkts = sniff(filter="tcp and port 80", count=3)
wrpcap("./networking/03_scapy/tcp_pkts.pcap", pkts)

# Reading pcap files
rd_pkts = rdpcap("./networking/03_scapy/tcp_pkts.pcap")
rd_pkts.summary()

# Replaying a pcap file



for pkt in rd_pkts:
    send(pkt)

# ---------------------------------------------
# Test and Attacks
# ---------------------------------------------
# Fuzzing:
fuzz_pkt = IP(dst="www.milliyet.com.tr")/fuzz(UDP()/NTP(version=4))
send(fuzz_pkt, loop=1)

# ARP Cache Poisoning
# for this to work, you also have to perform a VLAN hopping attack, this is essentially the classic
# ARP cache poisoning attack that will prevent a client from joining the gateway.
# clientMAC =
# psrc =
# pdst =
# arp_pkt = Ether(dst=clientMAC)/ARP(op="who-has", psrc=gateway, pdst=client)
# send(arp_pkt, loop=1, inter=RandNum(10,40))

# There is also a Scapy function called arpcachepoison() that you can use, the code is below and will
# send a ARP response to the target with your MAC address and the victim’s IP address.
# arpcachepoison(target, victim, interval=60)