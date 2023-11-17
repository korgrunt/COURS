# Init permut table


def xor_bit(bit_a, bit_b):
    if int(bit_a) == 0 and int(bit_b) == 0:
        return '0'
    if int(bit_a) == 0 and int(bit_b) == 1:
        return '1'
    if int(bit_a) == 1 and int(bit_b) == 0:
        return '1'
    if int(bit_a) == 1 and int(bit_b) == 1:
        return '0'

def char_to_bits(one_char):
    return format(ord(one_char), '08b')

def binary_to_char(binary_string):
    return chr(int(binary_string, 2))

def char_xor_char(char_a, char_b):
    char_a_as_bits = char_to_bits(char_a)
    char_b_as_bits = char_to_bits(char_b)

    xor_bits = ""
    for i in range(len(char_a_as_bits)):
        xor_bits += xor_bit(char_a_as_bits[i], char_b_as_bits[i])
    return binary_to_char(xor_bits)

def rc4_exec(data):
    i = 0
    j = 0
    cypher_data = ""
    S_copy = S
    for a in range(len(data)):
        i = (i+1) % 256
        j = (j + S_copy[i]) % 256
        tmp = S_copy[i]
        S_copy[i] = S_copy[j]
        S_copy[j] = tmp
        cypher_idx = (S_copy[i] + S_copy[j]) % 256
        cypher_byte = chr(S_copy[cypher_idx])
        print("cypher_byte")
        print(cypher_byte)
        cypher_char_result = char_xor_char(cypher_byte,data[a])
        cypher_data += cypher_char_result

    return cypher_data

def gen_pseudo_alea(S_initialized, i , j):
    S_copy = S_initialized
    for idx in range(len(S_copy)):
        i = 0
        j = 0
        i += 1
        j = j + S_copy[i]
        tmp = S_copy[i]
        S_copy[i] = S_copy[j]
        S_copy[j] = S_copy[i]
    return str(S_copy[0]) + "_" + str(S_copy[1]) 

if __name__ == "__main__":
    plaintext = "Hello Cypher World! Hello Cypher World! Hello Cypher World! Hello Cypher World! Hello Cypher World! Hello Cypher World! Hello Cypher World! "
    key = ["b7", "7f", "39", "a0", "46", " b6", "a9", "17", "29", "27", "d3", "a5", "73", "c6", "58", "8d"]




    # Key schedule
    S = list(range(256))
    j = 0
    i = 0
    for idx in range(len(S)):

        j = (j + S[i] + int(key[i % len(key)], 16)) % 256
        #print(f"i {i}")
        #print(f"j {j}")
        # permut index j with index i of S
        tmp = S[i]
        S[i] = S[j]
        S[j] = tmp

    # cypher and uncypher
    
    for e in list(range(100)):
        print(f"Generated: {gen_pseudo_alea(S, i , j)}")

    
    cyfer_text = rc4_exec(plaintext)
    decyfer_text = rc4_exec(cyfer_text)
    print(f"Plain text: {plaintext}")
    print("____________________________________________")
    print(f"Ciphertext: {cyfer_text}")
    print("____________________________________________")
    print(f"DeCiphertext: {decyfer_text}")
    
    #print(f"Decrypted text: {decrypted_text}")