from scapy.all import *
from pdb import set_trace # debuger python for breakpint

sniff(iface="mon0", lfilter=lambda x: Dot11Beacon in x, prn=lambda p: print("[%s] %s" % (p.addr2, p.info))) # retourne la list des paquet 