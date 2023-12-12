WARNING: IPython not available. Using standard Python shell instead.
AutoCompletion, History are disabled.
                                      
                     aSPY//YASa       
             apyyyyCY//////////YCa       |
            sY//////YSpcs  scpCY//Pp     | Welcome to Scapy
 ayp ayyyyyyySCP//Pp           syY//C    | Version 2.5.0
 AYAsAYYYYYYYY///Ps              cY//S   |
         pCCCCY//p          cSSps y//Y   | https://github.com/secdev/scapy
         SPPPP///a          pP///AC//Y   |
              A//A            cyP////C   | Have fun!
              p///Ac            sC///a   |
              P////YCpc           A//A   | To craft a packet, you have to be a
       scccccp///pSP///p          p//Y   | packet, and learn how to swim in
      sY/////////y  caa           S//P   | the wires and in the waves.
       cayCyayP//Ya              pY/Ya   |        -- Jean-Claude Van Damme
        sY/PsY////YCc          aC//Yp    |
         sc  sccaCY//PCypaapyCP//YSs  
                  spCPY//////YPSps    
                       ccaacs         
                                      
>>> IP()
<IP  |>
>>> Ether()
<Ether  |>
>>> a = IP()
>>> a.show()
###[ IP ]### 
  version   = 4
  ihl       = None
  tos       = 0x0
  len       = None
  id        = 1
  flags     = 
  frag      = 0
  ttl       = 64
  proto     = hopopt
  chksum    = None
  src       = 127.0.0.1
  dst       = 127.0.0.1
  \options   \

>>> a = IP(dest="9.9.9.9", src="1.2.3.4")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/base_classes.py", line 399, in __call__
    i.__init__(*args, **kargs)
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/packet.py", line 188, in __init__
    raise AttributeError(fname)
AttributeError: dest
>>> a = IP(dst="9.9.9.9", src="1.2.3.4")
>>> a.show()
###[ IP ]### 
  version   = 4
  ihl       = None
  tos       = 0x0
  len       = None
  id        = 1
  flags     = 
  frag      = 0
  ttl       = 64
  proto     = hopopt
  chksum    = None
  src       = 1.2.3.4
  dst       = 9.9.9.9
  \options   \

>>> print(a)
1.2.3.4 > 9.9.9.9 hopopt
>>>  byte(a)
  File "<console>", line 1
    byte(a)
IndentationError: unexpected indent
>>>  bytes(a)
  File "<console>", line 1
    bytes(a)
IndentationError: unexpected indent
>>> bytes(a)
b'E\x00\x00\x14\x00\x01\x00\x00@\x00d\xd2\x01\x02\x03\x04\t\t\t\t'
>>> a
<IP  src=1.2.3.4 dst=9.9.9.9 |>
>>> a.ttl = 12
>>> print(a)
1.2.3.4 > 9.9.9.9 hopopt
>>> a
<IP  ttl=12 src=1.2.3.4 dst=9.9.9.9 |>
>>> a/TCP()
<IP  frag=0 ttl=12 proto=tcp src=1.2.3.4 dst=9.9.9.9 |<TCP  |>>
>>> a
<IP  ttl=12 src=1.2.3.4 dst=9.9.9.9 |>
>>> pkt = a/TCP()
>>> pkt
<IP  frag=0 ttl=12 proto=tcp src=1.2.3.4 dst=9.9.9.9 |<TCP  |>>
>>> pkt.show()
###[ IP ]### 
  version   = 4
  ihl       = None
  tos       = 0x0
  len       = None
  id        = 1
  flags     = 
  frag      = 0
  ttl       = 12
  proto     = tcp
  chksum    = None
  src       = 1.2.3.4
  dst       = 9.9.9.9
  \options   \
###[ TCP ]### 
     sport     = ftp_data
     dport     = http
     seq       = 0
     ack       = 0
     dataofs   = None
     reserved  = 0
     flags     = S
     window    = 8192
     chksum    = None
     urgptr    = 0
     options   = ''

>>> pkthttp = a/TCP()/Raw("GET / HTTP/1.0\r\n\r\n")
>>> pkthttp.show
<bound method Packet.show of <IP  frag=0 ttl=12 proto=tcp src=1.2.3.4 dst=9.9.9.9 |<TCP  |<Raw  load='GET / HTTP/1.0\r\n\r\n' |>>>>
>>> pkthttp.show()
###[ IP ]### 
  version   = 4
  ihl       = None
  tos       = 0x0
  len       = None
  id        = 1
  flags     = 
  frag      = 0
  ttl       = 12
  proto     = tcp
  chksum    = None
  src       = 1.2.3.4
  dst       = 9.9.9.9
  \options   \
###[ TCP ]### 
     sport     = ftp_data
     dport     = http
     seq       = 0
     ack       = 0
     dataofs   = None
     reserved  = 0
     flags     = S
     window    = 8192
     chksum    = None
     urgptr    = 0
     options   = ''
###[ Raw ]### 
        load      = 'GET / HTTP/1.0\r\n\r\n'

>>> bytes(pkthttp)
b'E\x00\x00:\x00\x01\x00\x00\x0c\x06\x98\xa6\x01\x02\x03\x04\t\t\t\t\x00\x14\x00P\x00\x00\x00\x00\x00\x00\x00\x00P\x02 \x00\x9a\xb5\x00\x00GET / HTTP/1.0\r\n\r\n'
>>> load_contrib("socks")
>>> # willl load a a plugin
>>> pkt[TCP]
<TCP  |>
>>> pkt[UDP]
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/packet.py", line 1327, in __getitem__
    raise IndexError("Layer [%s] not found" % name)
IndexError: Layer [UDP] not found
>>> pkt[Raw]
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/packet.py", line 1327, in __getitem__
    raise IndexError("Layer [%s] not found" % name)
IndexError: Layer [Raw] not found
>>> pkt[RAW]
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'RAW' is not defined
>>> pkt[TCP]
<TCP  |>
>>> pkt[TCP].underlayer
<IP  frag=0 ttl=12 proto=tcp src=1.2.3.4 dst=9.9.9.9 |<TCP  |>>
>>> pkt[TCP].load
Traceback (most recent call last):
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/packet.py", line 455, in __getattr__
    fld, v = self.getfield_and_val(attr)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/packet.py", line 450, in getfield_and_val
    raise ValueError
ValueError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/packet.py", line 457, in __getattr__
    return self.payload.__getattr__(attr)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/packet.py", line 455, in __getattr__
    fld, v = self.getfield_and_val(attr)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/packet.py", line 1764, in getfield_and_val
    raise AttributeError(attr)
AttributeError: load
>>> pkt[TCP].payload

>>> blob = raw(pkt[IP])
>>> IP(blob)
<IP  version=4 ihl=5 tos=0x0 len=40 id=1 flags= frag=0 ttl=12 proto=tcp chksum=0x98b8 src=1.2.3.4 dst=9.9.9.9 |<TCP  sport=ftp_data dport=http seq=0 ack=0 dataofs=5 reserved=0 flags=S window=8192 chksum=0x7967 urgptr=0 |>>
>>> blob = raw(pk bytes(a)
KeyboardInterrupt
>>> Ether()/IP()/ICMP()
<Ether  type=IPv4 |<IP  frag=0 proto=icmp |<ICMP  |>>>
>>> mypacket = Ether()/IP()/ICMP()
>>> mypacket.show()
###[ Ethernet ]### 
  dst       = ff:ff:ff:ff:ff:ff
  src       = 00:00:00:00:00:00
  type      = IPv4
###[ IP ]### 
     version   = 4
     ihl       = None
     tos       = 0x0
     len       = None
     id        = 1
     flags     = 
     frag      = 0
     ttl       = 64
     proto     = icmp
     chksum    = None
     src       = 127.0.0.1
     dst       = 127.0.0.1
     \options   \
###[ ICMP ]### 
        type      = echo-request
        code      = 0
        chksum    = None
        id        = 0x0
        seq       = 0x0
        unused    = ''

>>> mypacket[IP].dst = 8.8.8.8
  File "<console>", line 1
    mypacket[IP].dst = 8.8.8.8
                          ^^
SyntaxError: invalid syntax
>>> mypacket[IP].dst = "8.8.8.8"
>>> mypacket.show()
WARNING: getmacbyip failed on [Errno 1] Operation not permitted
WARNING: Mac address to reach destination not found. Using broadcast.
###[ Ethernet ]### 
  dst       = ff:ff:ff:ff:ff:ff
  src       = ec:b1:d7:35:93:d4
  type      = IPv4
###[ IP ]### 
     version   = 4
     ihl       = None
     tos       = 0x0
     len       = None
     id        = 1
     flags     = 
     frag      = 0
     ttl       = 64
     proto     = icmp
     chksum    = None
     src       = 192.168.1.38
     dst       = 8.8.8.8
     \options   \
###[ ICMP ]### 
        type      = echo-request
        code      = 0
        chksum    = None
        id        = 0x0
        seq       = 0x0
        unused    = ''

>>> mypacket[ICMP].type = "echo-request"
>>> mypacket[ICMPpkt[RAW]
KeyboardInterrupt
>>> mypacket[ICMP.show()
KeyboardInterrupt
>>> mypacket.show()
WARNING: getmacbyip failed on [Errno 1] Operation not permitted
WARNING: Mac address to reach destination not found. Using broadcast.
###[ Ethernet ]### 
  dst       = ff:ff:ff:ff:ff:ff
  src       = ec:b1:d7:35:93:d4
  type      = IPv4
###[ IP ]### 
     version   = 4
     ihl       = None
     tos       = 0x0
     len       = None
     id        = 1
     flags     = 
     frag      = 0
     ttl       = 64
     proto     = icmp
     chksum    = None
     src       = 192.168.1.38
     dst       = 8.8.8.8
     \options   \
###[ ICMP ]### 
        type      = echo-request
        code      = 0
        chksum    = None
        id        = 0x0
        seq       = 0x0
        unused    = ''

>>> send(mypacket)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/sendrecv.py", line 445, in send
    return _send(
           ^^^^^^
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/sendrecv.py", line 414, in _send
    socket = socket or _func(iface)(iface=iface, **kargs)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/arch/linux.py", line 484, in __init__
    self.ins = socket.socket(
               ^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/socket.py", line 232, in __init__
    _socket.socket.__init__(self, family, type, proto, fileno)
PermissionError: [Errno 1] Operation not permitted
>>> send(mypacket)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/sendrecv.py", line 445, in send
    return _send(
           ^^^^^^
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/sendrecv.py", line 414, in _send
    socket = socket or _func(iface)(iface=iface, **kargs)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/naouaichia/Workspace/COURS/scapy/cour01/venv/lib/python3.11/site-packages/scapy/arch/linux.py", line 484, in __init__
    self.ins = socket.socket(
               ^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/socket.py", line 232, in __init__
    _socket.socket.__init__(self, family, type, proto, fileno)
PermissionError: [Errno 1] Operation not permitted
>>> exit()
