from Crypto.Hash import SHA256  
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

#Example usage
password = b"toto"
salt = b"00000000"
counter = 1000
result = derivpassword(password, salt, counter)
print(binascii.hexlify(result).decode())