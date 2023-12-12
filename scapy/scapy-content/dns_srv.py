from scapy.all import *
from pdb import pm

# domain -> IP
cache = {}

def callback(pkt):
    global cache
    if DNSQR not in pkt:
        return
    if IP not in pkt:
        return
    
    query = pkt[DNSQR]
    # Check if it is a A request
    if query.qtype != 1:
        return

    # Cache handling
    target_dom = query.qname
    reply_ip = cache.setdefault(target_dom, str(RandIP()))

    # Answer
    pkt_reply = IP(
        dst=pkt[IP].src,
        src=pkt[IP].dst
    ) / UDP(
        dport=pkt[UDP].sport,
        sport=pkt[UDP].dport
    ) / DNS(
        qr=1,
        id=pkt[DNS].id,
        qd=pkt[DNSQR],
        an=DNSRR(
            rrname=target_dom,
            type="A",
            rdata=reply_ip
        )
    )
    send(pkt_reply)


sniff(filter="udp port 53", prn=callback, store=0)