from scapy.all import *
from pdb import set_trace # debuger python for breakpint
from pprint import pprint as pp
# MY TRACEROUTE on ping (like a real ping or traceroute !!
#     if("type" not in pak[ICMP] or pak[ICMP].sprintf("%type%") != "echo-reply"):

def icmp_fast():
    pkts = [
      IP(dst="8.8.8.8", ttl=ttl)/ICMP(seq=ttl)
      for ttl in range(1, 90)   
    ]
    ans, unans = sr(pkts, verbose=False, timeout=1)
    
    # ttl -> IP
    t2ip = {}

    for pkt in unans:
        t2ip[pkt[IP].ttl] = "*" 

    for query, answer in ans:
        t2ip[query[IP].ttl] = answer[IP].src 

    for ttl, ip in sorted(t2ip.items(), key=lambda x:x[0]):
        print(f"{ttl}. {ip}")

    print("__________")



    #pp(t2ip)

icmp_fast()


# va envoyer 5 paquet de 1 a 5 pour 1.2.3.4 et 5 paquet pour 8.8.8.8


### On peut faire du spoofing wifi en envoyant des paquet Beacon pour se fair epasser pour un point d'acces wifi