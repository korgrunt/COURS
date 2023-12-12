from scapy.all import *
from pdb import set_trace # debuger python for breakpint
from pprint import pprint as pp

# get ips for url www.perdu.com
dns_req = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(qd=DNSQR(qname='www.perdu.com', qtype="A"))
ans = sr1(dns_req)

print("__________________")
while DNSRR in ans:
    print(ans[DNSRR].rdata)
    ans = ans[DNSRR].payload
print("__________________")
