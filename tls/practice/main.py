from typing import Optional
from Crypto.Random import get_random_bytes
import binascii
import string
import sys


def generate_rrandom_pass(len_of_str):
    print(len_of_str)
    print(len_of_str - 1)


    random_str = ""
    for i in range(0, len_of_str + 1):
        print("tet")
        random_int = int.from_bytes(get_random_bytes(1))
        random_str += string.ascii_letters[random_int % len(string.ascii_letters)] if random_int % 2 == 0 else string.digits[random_int % len(string.digits)]

    return random_str


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("at least one arg please")
        sys.exit(1)
    
    random_str = generate_rrandom_pass(int(sys.argv[1]))
    if random_str is not None:
        print('ho my random_str')
        print(random_str)
    else:
        print("error bro")
    sys.exit(1)


# FirstSecondThird

#
# Should not use random int with modulo, instead, should use fonction of crypto.Random.random.choice, and provide it an alphabet with string.ascii_letters + string.digits + string.puncuation 
# 
#