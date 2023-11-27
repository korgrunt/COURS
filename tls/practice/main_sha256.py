from typing import Optional
from Crypto.Hash import SHA256
import binascii
import sys

hash_object = SHA256.new(data=b'First')
hash_object.update(b'Second')
hash_object.update(b'Third')

#print(hash_object.hexdigest())

def sliceIt(x, bs):
    return [x[i:i+bs] for i in range(0, len(x), bs)]

def sha256_file(str, chunk_sz=512) -> Optional[bytes]:
    
    print("sys.getsizeof(str)")
    print(sys.getsizeof(str))
    val = sliceIt(str, 512)
    
    hash_object = SHA256.new(data=bytes(val[0], 'utf-8'))

    for i in range(1, len(val)):
        print('turn')
        hash_object.update(bytes(val[i], 'utf-8'))
        print(val[i])
    #print([(str[i:i+n]) for i in range(0, len(str), n)])
    print(str[0])
  
    print('ok')
    return hash_object.hexdigest()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("at least one arg please")
        sys.exit(1)
    
    digest = sha256_file(sys.argv[1])
    if digest is not None:
        print('ho my hash')
        print(digest)
        #print(f"{binascii.hexlify(digest).decode()}")
    else:
        print("error bro")
    sys.exit(1)


# FirstSecondThird

