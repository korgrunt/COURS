from scapy.all import *

def callback(pkt):
    print(""" Cette fonction est appelé pour chasque paquet sniffé""")
    pkt.show()

sniff(prn=callback, filter="icmp" ,store=0)