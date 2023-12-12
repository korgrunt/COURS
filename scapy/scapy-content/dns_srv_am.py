from scapy.all import *


class FakeDnsSrv(AnsweringMachine):

    filter = "udp port 53"

    def parse_options(self):
        self.cache = {}

    def is_request(self, pkt):
        "Check if it is a IP/DNSQR(type=A) pkt"
        if DNSQR not in pkt:
            return False
        if IP not in pkt:
            return False
        # Check if it is a A request
        if pkt[DNSQR].qtype != 1:
            return
        return True

    def make_reply(self, pkt):
        query = pkt[DNSQR]
       
        # Cache handling
        target_dom = query.qname
        reply_ip = self.cache.setdefault(target_dom, str(RandIP()))

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
        return pkt_reply

FakeDnsSrv()()