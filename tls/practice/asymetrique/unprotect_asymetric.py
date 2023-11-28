### protect symetrique

# python3 protect_symetric.py <password> <input_file> <output_file> 
import sys
import json
from base64 import b64encode
import binascii

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256, HMAC
from Crypto.Util.Padding import pad, unpad
from Crypto.Signature import pss

def hexdump_bytes(tableau_bytes):
    for i in range(0, len(tableau_bytes), 16):
        ligne = tableau_bytes[i:i + 16]
        hex_string = ' '.join(f'{byte:02x}' for byte in ligne)
        ascii_string = ''.join(chr(byte) if 32 <= byte < 127 else '.' for byte in ligne)
        print(f'{i:08x}: {hex_string.ljust(48)}  {ascii_string}')

separator_file = b'\xa1\xb2\xc3\xd4'
def decouper_par_separateur(tableau_bytes, separateur=b'\xa1\xb2\xc3\xd4'):
    longueur_tableau = len(tableau_bytes)

    result = [0] * 4
    last_slice = 0
    result_idx = 0
    for i in range(longueur_tableau - 1):
        print("tableau_bytes[i:i+4]")
        hexdump_bytes(tableau_bytes[i:i+4])
        if(result_idx == 3):
            break
        if(tableau_bytes[i:i+4] == separateur):
            print("result_idx")
            print(result_idx)
            result[result_idx] = tableau_bytes[last_slice:i]
            i = i + 4
            last_slice = i 
            result_idx = result_idx + 1

    print("result")
    print(result)

    for i in range(len(result)):
        print("result[i]")
        print(result[i])

    if(result_idx != 3):
        print("Can't parse correctly input file")
        exit(1)

    
    return result



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




def protect_file_sym(password, input_filename, output_filename):
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

    data_returned = dict();
    data_returned['iv'] = iv
    data_returned['kc'] = key_cipher
    data_returned['c'] = encrypted_data_bytes
    return data_returned


def protect_file_asym(password, input_filename, output_filename):
    print("hrrllo")

def main():
    if len(sys.argv) != 5:
        print("Need three arg please, commmand reminder $> python3 protect_asymetric.py <password> <input_file> <output_file> ")
        sys.exit(1)


    #chifré en sym et récupérer C, Kc, iv,
    public_sign_filename = sys.argv[1]
    private_cypher_filename = sys.argv[2]
    input_filename = sys.argv[3]
    output_filename = sys.argv[4]
    
    # généré deux bi clée du destinataire, même si en pratque, le destinataire nous envoir uniqument sa clée public et garde la clee privee de sont coté
    # cela a été fait précedement dans le script python protect, on e le refait pas a nouveau
    # une bi clée pour signer qui appartient a l'envoyeur, l'envoyeur partage sa clée public

    # recuppératio de la clée rsa public pour veifier signature


    # recuppératio de la clée rsa pour privé pour déchifrer le sequestre
    

    input_file_bytes = open(input_filename, "rb").read()

    print("okok is sliced")

    
    encrypted_kc_as_sequestre = input_file_bytes[:256]
    cypher_content = input_file_bytes[256:-48]
    iv = input_file_bytes[-48:-32]
    signature = input_file_bytes[-32:]
    
    print(len(encrypted_kc_as_sequestre))
    decrypt_sequestre_key_priv = RSA.import_key(open(private_cypher_filename, "rb").read())
    cipher = PKCS1_OAEP.new(decrypt_sequestre_key_priv)
    kc = cipher.decrypt(input_file_bytes[:256])
    print("message.decode()")

    cipher = AES.new(kc, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(cypher_content), AES.block_size)
    print(pt)



    key_sign_verif = RSA.import_key(open(public_sign_filename, "rb").read())
    h = SHA256.new(input_file_bytes[:-32])

    verifier = pss.new(key_sign_verif)
    try:
        verifier.verify(h, signature)
        print("The signature is authentic.")
    except (ValueError, TypeError):
        print ("The signature is not authentic.")



    exit(0)


    data_returned = protect_file_sym(password, input_filename, output_filename)

    # générer le sequestre qui contient Kc, via la clée clée public de chiffrement 
    recipient_key = RSA.import_key(open("public_cypher.pem").read())
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    encrypted_kc_as_sequestre = cipher_rsa.encrypt(data_returned["kc"])

    # concatener Sequestre, iv, C et les signer

    key = RSA.import_key(open('private_sign.pem').read())
    h = SHA256.new(encrypted_kc_as_sequestre + data_returned["c"] + data_returned["iv"])
    signature = pss.new(key).sign(h)

    # concatener Sequestre, iv, C et signature, et print dan sun file
    
    with open(output_filename, 'wb') as f: 
        f.write(encrypted_kc_as_sequestre)
        f.write(data_returned["c"])
        f.write(data_returned["iv"])
        f.write(signature)


    print("Ok it's valid")
    sys.exit(0)


main()

# (venv) ➜  practice git:(main) ✗ $> python3 protect_asymetric.py password ./asym_plain_text.txt ./asym_file_out.txt
