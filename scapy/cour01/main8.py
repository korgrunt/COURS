from scapy.all import *
from pdb import set_trace # debuger python for breakpint
from pprint import pprint as pp

### DNS EXPLICATION

# AXFR demaner a un serveur dns de donener toute sa config
# AAAA ipV6
# A ipv4
# CNAME is for alias


#  dig -t NS arpa    => send list of server for arpa

# dig -t AXFR @a.ns.arpa arpa    => ne renvoi pas la list des enregistrement
# dig -t AXFR @c.ns.arpa arpa    => list des enregistrements biern recu

def callback(pkt):
    print(""" Cette fonction est appelé pour chasque paquet sniffé""")
    pkt.show()

sniff(prn=callback, filter="udp port 53")

