from scapy.all import *
from pdb import pm
import argparse

parser = argparse.ArgumentParser("MY tracerout3r")
parser.add_argument("dst", help="Target IP")
parser.add_argument("--timeout", type=int, default=1)
parser.add_argument("--max-ttl", type=int, default=30)
parser.add_argument("--fast", action="store_true")
options = parser.parse_args()

def icmp_fast():
    pkts = [
        IP(dst=options.dst, ttl=ttl)/ICMP(seq=ttl)
        for ttl in range(1, options.max_ttl)
    ]
    ans, unans = sr(pkts, verbose=False, timeout=options.timeout)
    
    # ttl -> IP
    t2ip = {}

    # Handle unanswered packets
    for pkt in unans:
        t2ip[pkt[IP].ttl] = "*"
    
    # Handle answered packets
    for qa in ans:
        t2ip[qa.query[IP].ttl] = qa.answer[IP].src

    for ttl, ip in sorted(t2ip.items(), key=lambda x:x[0]):
        print(f"{ttl}. {ip}")


def icmp_slow():
    for ttl in range(1, options.max_ttl):
        pkt = IP(dst=options.dst, ttl=ttl)
        pkt = pkt/ICMP(type="echo-request")
        #pkt = pkt/TCP(dport=80)
        ans = sr1(pkt, verbose=False, timeout=options.timeout)
        if ans is None:
            ip = "*"
        else:
            ip = ans[IP].src
        print(f"{ttl}. {ip}")
        # if ip == options.dst:
        #     break

if options.fast:
    icmp_fast()
else:
    icmp_slow()
