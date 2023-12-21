from scapy.all import *
from pdb import set_trace # debuger python for breakpint
from pprint import pprint as pp

# DNS SPPOF on 10.0.0.1

# domain -> ip


def callback(pkt):
    if ICMP in pkt: 
        if pkt[IP].dst != "10.0.0.1":
            return

        tcp_payload = bytes(pkt[ICMP].payload)
        to_send = TCP(tcp_payload)
        to_send.show()
        #force tcp port
        to_send.dport = 1234
        #Recalcule checksum
        to_send.chksum = None
        
        send(IP(dst="127.0.0.1")/to_send)
    elif TCP in pkt and pkt[TCP].sport == 1234:
        payload = IP(dst="10.0.0.2", src="10.0.0.1")/ICMP(type="echo-reply")/Raw(pkt[TCP])
        send(payload)

print("ok")
conf.L3socket = L3RawSocket

sniff(prn=callback, filter="icmp or src port 1234" ,store=0, iface=["jailin", "lo"])
