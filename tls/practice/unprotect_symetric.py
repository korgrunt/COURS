### protect symetrique

# python3 protect_symetric.py <password> <input_file> <output_file> 
import sys
import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
from Crypto.Hash import HMAC, SHA256
import binascii


def derivpassword(password: bytes, salt: bytes, counter: int):

    #Init
    integer_val = 0
    password_h0 = SHA256.new(password + salt + integer_val.to_bytes(4, 'little')).digest()
 
    #Iterate
    for i in range(1, counter):
    
        #Counter bytes to little-endian
        counter_bytes = i.to_bytes(4, byteorder='little')
        #Calculate Hi 
        password_hi = SHA256.new(password_h0 + password + salt + counter_bytes).digest()
        #Update hi_minus_1 for the next iteration
        password_h0 = password_hi

    #Return the first 32 bytes
    return password_hi[:32]




def unprotect_file(password, input_filename, output_filename):
    f = open(input_filename, "rb").read()
    salt = f[:8]
    iv = f[8:24]
    c = f[24:-32]
    hmac = f[-32:]




    print("____salt________________")
    print(salt)
    print("____________________")

    print("___hmac_________________")
    print(hmac)
    print("____________________")

    print("__iv__________________")
    print(iv)
    print("____________________")

    print("__c__________________")
    print(c)
    print("____________________")

    counter = 1000
    key_master = derivpassword(str.encode(password), salt, counter)
    # derive KM
    key_integrity = SHA256.new(key_master + b'01').digest()
    key_cipher = SHA256.new(key_master + b'00').digest()

    cipher = AES.new(key_cipher, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(c), AES.block_size)
    print("The message was: ", pt)
    return 1


def main():
    if len(sys.argv) != 4:
        print("Need three arg please, commmand reminder $> python3 unprotect_symetric.py <password> <input_file> <output_file> ")
        sys.exit(1)

    password = sys.argv[1]
    input_filename = sys.argv[2]
    output_filename = sys.argv[3]

    unprotect_file(password, input_filename, output_filename)

    print("Ok it's valid")
    sys.exit(0)


main()

# (venv) ➜  practice git:(main) ✗ $> python3 protect_symetric.py password ./plain_text.txt ./file_out.txt 



# python3 unprotect_symetric.py password ./sym_file_out.txt ./unprotected_file_out.txt