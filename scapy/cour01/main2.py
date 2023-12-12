from scapy.all import *
from pdb import set_trace # debuger python for breakpint


def callback(pkt):
    print(""" Cette fonction est appelé pour chasque paquet sniffé""")
    pkt.show()

sniff(prn=callback, filter="icmp" ,store=0)