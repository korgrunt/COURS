### protect symetrique

# python3 protect_symetric.py <password> <input_file> <output_file> 
import sys
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
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




def protect_file(password, input_filename, output_filename):
    print(password)
    print(input_filename)
    # derive password
    salt = get_random_bytes(8)
    counter = 1000
    key_master = derivpassword(str.encode(password), salt, counter)
    # derive KM
    key_integrity = SHA256.new(key_master + b'01').digest()
    key_cipher = SHA256.new(key_master + b'00').digest()
    
    # Read file
    file_to_protect = open(input_filename, "r").read()

    print("ok")

    # Cipĥer data (protect privacy)
    cipher = AES.new(key_cipher, AES.MODE_CBC)
    encrypted_data_bytes = cipher.encrypt(pad(str.encode(file_to_protect), AES.block_size))
    iv = cipher.iv

    #result = json.dumps({'iv':iv, 'ciphertext':encrypted_data_bytes})
    
    # Calculate HMAC (protect privacy)
    h_mac = HMAC.new(key_integrity, digestmod=SHA256)
    h_mac.update(salt)
    h_mac.update(iv)
    h_mac.update(encrypted_data_bytes)
    
    # Calculate HMAC (protect privacy)
    print("salt")
    print(salt)
    print("h_mac")
    print(h_mac.digest())
    print("iv")
    print(iv)
    print("encrypted_data_bytes")
    print(encrypted_data_bytes)
    
    with open(output_filename, 'wb') as f: 
        f.write(salt)
        f.write(iv)
        f.write(encrypted_data_bytes)
        f.write(h_mac.digest())
    return 1


def main():
    if len(sys.argv) != 4:
        print("Need three arg please, commmand reminder $> python3 protect_symetric.py <password> <input_file> <output_file> ")
        sys.exit(1)

    password = sys.argv[1]
    input_filename = sys.argv[2]
    output_filename = sys.argv[3]

    protect_file(password, input_filename, output_filename)

    print("Ok it's valid")
    sys.exit(0)


main()

# (venv) ➜  practice git:(main) ✗ $> python3 protect_symetric.py password ./plain_text.txt ./file_out.txt 


# python3 protect_symetric.py password ./sym_plain_text.txt ./file_out.txt