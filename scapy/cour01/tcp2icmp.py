from scapy.all import *
from pdb import set_trace # debuger python for breakpint
from pprint import pprint as pp

# DNS SPPOF on 10.0.0.1

# domain -> ip


def callback(pkt):
    if ICMP in pkt and pkt[ICMP].type == 8:
        # cas return    
        tcp_p = TCP(bytes(pkt[ICMP].payload))
        tcp_p.chksum = None
        tcp_p.sport = 1234
        send(IP(dst="10.0.0.2", src="10.1.2.3") / tcp_p)
    else:
        if not TCP in pkt:
            return
        if not pkt[TCP].dport == 1234:
            return
        to_send = IP(dst="10.0.0.1", src= "10.0.0.2") / ICMP() / Raw(pkt[IP].payload)
    
        send(to_send)

sniff(prn=callback, filter="port 1234 and host 10.1.2.3" ,store=0)