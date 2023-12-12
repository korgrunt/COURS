from scapy.all import *
from pdb import pm

seen = set()

def callback(pkt):
    if Dot11Beacon in pkt:
        # (BSSID, ESSID)
        info = (pkt.addr2, pkt.info)
        if info not in seen:
            seen.add(info)
            print(f"[{info[0]}] {info[1]}")
    elif Dot11ProbeReq in pkt:
        print(f"ProbeReq: {pkt.addr2} - {pkt.info}")



sniff(iface="mon0", prn=callback)
