from scapy.all import *
import socket
import requests

load_contrib("socks")

_socks5_methods = { 0x00: 'NO AUTHENTICATION REQUIRED', 
                                  0x01: 'GSSAPI', 
                                  0x02: 'USERNAME/PASSWORD', 
                                  0xFF: 'NO ACCEPTABLE METHODS'
                                  }
class SOCKS5MethodReply(Packet):
    name = "Socks 5 reply"
    overload_fields = {SOCKS: {"vn": 0x5 }}
    fields_desc = [
        ByteEnumField("cd", 0x0, { 0x00: 'NO AUTHENTICATION REQUIRED', 
                                  0x01: 'GSSAPI', 
                                  0x02: 'USERNAME/PASSWORD', 
                                  0xFF: 'NO ACCEPTABLE METHODS'
                                  })
    ]

class SOCKS5MethodQuery(Packet):
    name = "Socks 5 query"
    overload_fields = {SOCKS: {"vn": 0x5 }}
    fields_desc = [
        FieldLenField("nmethods", None,
                      count_of="methods", 
                      fmt="B"),#struct.unpack(">BBHHbbhhIIQQ")
        FieldListField("methods", [], ByteEnumField("method", 0, _socks5_methods))
    ]


class SOCKS5MethodRequest(Packet):
    name = "Socks 5 request"
    overload_fields = {SOCKS: {"vn": 0x5 }}
    fields_desc = [
        ByteEnumField("cmd", 0x01, { 0x01: 'CONNECT', 0x02: 'BIND', 0x03: 'UDP ASSOCIATE' }),
        ByteField("rsv", 0x00),
        ByteEnumField("atyp", 0x01, { 
            0x01: 'IP V4 address', 
            0x03: 'DOMAINNAME', 
            0x04: 'IP V6 address' }),
        MultipleTypeField(
            [
                # IPv4
                (IPField("addr", "0.0.0.0"), lambda pkt: pkt.atyp == 0x01),
                # DNS
                (DNSStrField("addr", ""), lambda pkt: pkt.atyp == 0x03),
                # IPv6
                (IP6Field("addr", "::"), lambda pkt: pkt.atyp == 0x04),
            ],
            StrField("addr", "")  
        ),
        ShortField("port", 0x00),
    ]



ADRESSE = '127.1'
PORT = 1080

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serveur.bind((ADRESSE, PORT))
serveur.listen(1)

while(True):
    client, adresseClient = serveur.accept()
    print(f"Connexion de ', {adresseClient}")

    data = client.recv(1024)
    if not data:
        print(f"Erreur de reception.'")
    else:
        print(f"Reception de: {data}")

        # Socks nego request
        socksQuery = SOCKS(data)
        socksQuery.decode_payload_as(SOCKS5MethodQuery)
        socksQuery.show()
        #ls(socksRequest, verbose=True)

        # Socks nego reply
        response = client.send(bytes(SOCKS()/SOCKS5MethodReply(cd=[b"\x00"])))
        
        # Socks Query
        data = client.recv(1024)
        socksQuery = SOCKS()/SOCKS5MethodQuery(methods=[b"\x00"])
        print("_____________")



        print("_____________")
        
        # Reply to client
        rep = SOCKS()/SOCKS5Reply(addr="0.0.0.0", port=0)
        client.send(bytes(rep))

        # Sockes Request to target
        srv_socket = None
        if socksQuery.atyp == 1:
            srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif socksQuery.atyp == 4:
            srv_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        else:
            print("Error for addr type for target ")
            exit(1)


        srv_socket.connect((socksQuery.addr, socksQuery.port))

        data = client.recv(1024)

        srv_socket.send(bytes(data))
        srv_data = srv_socket.recv(1024)

        #print(target_response)
        print("-----")
        print(srv_data)
        client.send(bytes(srv_data))

        # select (for maage traffic from server to client or from client to server)
        while True:
            result = select.select(
                [client, srv_socket],   # readable
                [],                     # writable
                [],                     # exception table
                1
            )

            if(client in result[0]): # cl -> srv
                data = client.recv(1024)
                if(len(data) == 0):
                    break
                print(f"Client -> srv {data}")
                srv_socket.send(data)
            if(srv_socket in result[0]): # srv ->  cl
                data = srv_socket.recv(1024)
                if(len(data) == 0):
                    break
                print(f"srv -> client {data}")
                client.send(data)
        client.close()
        srv_socket.close()
        print("closed")

