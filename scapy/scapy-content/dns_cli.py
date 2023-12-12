from scapy.all import *
from argparse import ArgumentParser

parser = ArgumentParser("DNS CLI")
parser.add_argument("--srv", default="8.8.8.8")
parser.add_argument("name")
options = parser.parse_args()

pkt = IP(dst=options.srv)/UDP(dport=53)/DNS(qd=DNSQR(
    qname=options.name,
    qtype="A"
))
ans = sr1(pkt, verbose=False)

while DNSRR in ans:
    print(ans[DNSRR].rdata)
    ans = ans[DNSRR].payload