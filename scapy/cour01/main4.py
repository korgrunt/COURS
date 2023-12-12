from scapy.all import *
from pdb import set_trace # debuger python for breakpint

seen = set()

def callback(pkt):
    info = pkt.addr2, pkt.info
    if info not in seen:
        seen.add(info)
        print(info)

sniff(iface="mon0", lfilter=lambda x: Dot11Beacon in x, prn=callback) # retourne la list des paquet 

### On peut faire du spoofing wifi en envoyant des paquet Beacon pour se fair epasser pour un point d'acces wifi