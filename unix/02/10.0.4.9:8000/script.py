"""
Uncipher Cisco type 7 ciphered passwords
Usage: python uncipher.py <pass> where <pass> is the text of the type 7 password
Example:
$ python uncipher.py 094F4F1D1A0403
catcat
"""
import sys

# this is the key against which the ciphered password values are XOR'd
key = [0x64, 0x73, 0x66, 0x64, 0x3b, 0x6b, 0x66, 0x6f, 0x41,
 0x2c, 0x2e, 0x69, 0x79, 0x65, 0x77, 0x72, 0x6b, 0x6c,
 0x64, 0x4a, 0x4b, 0x44, 0x48, 0x53, 0x55, 0x42]

pw = sys.argv[1] 
# the first 2 characters of the password are the starting index in the key array
# for example: 094F4F1D1A0403 - the index is "09" or 0x2c
index = int(pw[:2],16)

# the remaining values are the characters in the password, as hex bytes
# for example: 094F4F1D1A0403 - characters are represented by 0x4F, 0x4F, 0x1D, 0x1A, etc.
pw_text = pw[2:]

pw_hex_values = [pw_text[start:start+2] for start in range(0,len(pw_text),2)]

# we then XOR those values against the key values, starting at the index, and convert to ASCII
pw_chars = [chr(key[index+i] ^ int(pw_hex_values[i],16)) for i in range(0,len(pw_hex_values))]

pw_plaintext = ''.join(pw_chars)
print(pw_plaintext)