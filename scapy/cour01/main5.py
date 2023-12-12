from scapy.all import *
from pdb import set_trace # debuger python for breakpint

seen = set()

def callback(pkt):
    if(Dot11Beacon in pkt):
        info = pkt.addr2, pkt.info
        if info not in seen:
            seen.add(info)
            print(info)
    elif(Dot11ProbeReq in pkt): # un client qui demande a se connecter
        pkt.show()

sniff(iface="mon0", prn=callback) # retourne la list des paquet 

### On peut faire du spoofing wifi en envoyant des paquet Beacon pour se fair epasser pour un point d'acces wifi