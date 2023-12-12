from scapy.all import *
from pdb import set_trace # debuger python for breakpint

# MY TRACEROUTE on ping (like a real ping or traceroute !!

MAX_TTL = 30
DST = "8.8.8.8"
for i in range(1, MAX_TTL):
    pkt = IP(dst=DST, ttl=i)/ICMP(type="echo-request")
    result = sr1(pkt, timeout=1, verbose=False)
    #result.show()
    print(f"distance is {i}") 
    if result is None:
        ip = "*"
    else :
        ip = result[IP].src

    print(f"IP = {ip}, ttl = {i}")
    if ip == DST:
        break
   



### On peut faire du spoofing wifi en envoyant des paquet Beacon pour se fair epasser pour un point d'acces wifi