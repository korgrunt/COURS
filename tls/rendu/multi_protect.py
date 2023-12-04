from typing import Optional
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256, HMAC
from Crypto.Util.Padding import pad
from Crypto.Signature import pss
import binascii
import string
import sys
import json
from base64 import b64encode


ERR_BAD_ARGV = """
        Please, provide valid arguments, exemple of valide programme usage \n
        for decrypt: python multi_protect.py -d <input_file> <output_file> <my_priv_ciph.pem> <my_pub_ciph.pem> <sender_sign_pub.pem>\n
        for encrypt: python multi_protect.py -e <input_file> <output_file> <my_sign_priv.pem> <my_ciph_pub.pem> [<other_ciph_pub.pem> <other_ciph_pub_1.pem>... <other_ciph_pub_n.pem>]\n
        """

DEPROTECT_WITH_SUCCESS_MSG = "Deprotected with success, go to output file you provide in argument."
PROTECT_WITH_SUCCESS_MSG = "Protected with success, go to output file you provide in argument."

def parse_arguments_deprotect_mode(argv):
    arguments_container = {}

    arguments_container['input_file'] = argv[2]
    arguments_container['output_file'] = argv[3]
    arguments_container['my_priv_ciph'] = argv[4]
    arguments_container['my_pub_ciph'] = argv[5]
    arguments_container['sender_sign_pub'] = argv[6]
    return arguments_container

def parse_arguments_protect_mode(argv):
    arguments_container = {}

    arguments_container['input_file'] = argv[2]
    arguments_container['output_file'] = argv[3]
    arguments_container['my_sign_priv'] = argv[4]
    arguments_container['my_ciph_pub'] = argv[5]
    
    other_ciph_pub = []
    for i in range(6, len(argv)):
        other_ciph_pub.append(argv[i])
    arguments_container['other_ciph_pub'] = other_ciph_pub
    return arguments_container

def deprotect_file(arguments_container):
    print("go to deprotect")

def protect_file(arguments_container):
    









    print("go to protect")

def main(argv):
    if len(argv) < 6:
        print(ERR_BAD_ARGV) # bad arguments
        sys.exit(1)


    if(argv[1] == '-d'): 
        # parse  arguments
        arguments_container = parse_arguments_deprotect_mode(argv)
        # deprotect file
        deprotect_file(arguments_container)
        # print success msg
        print(DEPROTECT_WITH_SUCCESS_MSG) 
    elif(argv[1] == '-e'): # mode encrypt
        # parse  arguments
        arguments_container = parse_arguments_protect_mode(argv)
        # protect file
        protect_file(arguments_container)
        # print success msg
        print(PROTECT_WITH_SUCCESS_MSG) 
    else:
        print(ERR_BAD_ARGV) # bad arguments
        sys.exit(1) 

    sys.exit(0)

# Start program
main(sys.argv)



