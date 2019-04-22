import json

with open("pcap.json") as pcap:
    packets = json.load(pcap)

# for pckt in packets:
#     layer = pckt['_source']['layers']
#     ipPkt = layer.get('ip')
#     if ipPkt:
#         src = ipPkt['ip.src']
#         dst = ipPkt['ip.dst']
#         print(f'{src}\t\t{dst}')

counts = {}
for pckt in packets:
    layer = pckt['_source']['layers']
    ipPkt = layer.get('ip')
    if ipPkt:
        src = ipPkt['ip.src']
        # try:
        #     count = counts[src]
        # except KeyError:
        #     count = 0
        # counts[src] = count + 1
        counts[src] = counts.get(src, 0) + 1

# print headers
print("Source\t\t\t\tCount")
print("------\t\t\t\t-----------")
# print results
for key in counts:
    print(f'{key}\t\t{counts[key]}')
