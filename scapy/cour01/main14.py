from scapy.all import *
import socket
import requests

load_contrib("socks")

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
        print(hexdump(data))
        socksRequest = SOCKS(data)
        ls(socksRequest, verbose=True)

        # Socks nego reply
        response = client.send(b"\x05\x00")
        
        # Socks Query
        data = client.recv(1024)
        socksQuery = SOCKS(data)
        print("_____________")
        print(socksQuery[SOCKS5Request].addr)
        print(socksQuery[SOCKS5Request].port)
        print(socksQuery[SOCKS5Request].atyp)

        print("_____________")
        
        # Reply to client
        rep = SOCKS()/SOCKS5Reply(addr="0.0.0.0", port=0)
        client.send(bytes(rep))

        # Sockes Request to target
        srv_socket = None
        if socksQuery[SOCKS5Request].atyp == 1:
            srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif socksQuery[SOCKS5Request].atyp == 4:
            srv_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        else:
            print("Error for addr type for target ")
            exit(1)


        srv_socket.connect((socksQuery[SOCKS5Request].addr, socksQuery[SOCKS5Request].port))

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

