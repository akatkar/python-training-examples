from scapy.all import *

# ACK SCANNER
def ack_scanner():
    ans, unans = sr(IP(dst='www.slashdot.org')/TCP(dport=[80,666],flags='A'))
    for s,r in ans:
        if s[TCP].dport == r[TCP].sport:
            print(f'{s[TCP].dport} is unfiltered')

    for s in unans:
        print(f'{s[TCP].dport} is filtered')


def main():
    # ack_scanner()
    ans, unans = sr(IP(dst="192.168.1.1", proto=(0, 20)) / "SCAPY", retry=2)

if __name__ == '__main__':
    main()