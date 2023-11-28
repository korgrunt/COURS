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


def deriv_password_to_master_key(password: bytes, salt: bytes, counter: int):

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
    # extract salt, iv, c and hmac_digest
    f = open(input_filename, "rb").read()
    salt = f[:8]
    iv = f[8:24]
    c = f[24:-32]
    hmac_digest = f[-32:]

    # Derive password
    counter = 1000
    key_master = deriv_password_to_master_key(str.encode(password), salt, counter)
    # Derive key_master to key_integrity and key_cipher
    key_integrity = SHA256.new(key_master + b'01').digest()
    key_cipher = SHA256.new(key_master + b'00').digest()

    # decrypt cypher
    cipher = AES.new(key_cipher, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(c), AES.block_size)

    # rebuild hmac
    h_mac = HMAC.new(key_integrity, digestmod=SHA256)
    h_mac.update(salt)
    h_mac.update(iv)
    h_mac.update(c)

    # compare hmac for integrity check
    if hmac_digest == h_mac.digest():
        # program will exit 0 at the end of executiob
        print("Valid HMAC")
    else:
        # program will exit 1 at the end of execution, if can't write file, exit 2, if can't read file, exit 3, if can't parse file, exit 4
        print("Invalid HMAC")
    
    # write decrypted message
    with open(output_filename, 'wb') as fo: 
        fo.write(pt)

    return 1


def main():
    # check args
    if len(sys.argv) != 4:
        print("Need three arg please, commmand reminder $> python3 unprotect_symetric.py <password> <input_file> <output_file> ")
        sys.exit(1)
    # extract args
    password = sys.argv[1]
    input_filename = sys.argv[2]
    output_filename = sys.argv[3]

    # decrypt msg from input file
    unprotect_file(password, input_filename, output_filename)

    # decrypt msg from input file
    print("Ok it's valid")
    sys.exit(0)


main()


# python3 unprotect_symetric.py password ./sym_file_out.txt ./unprotected_file_out.txt