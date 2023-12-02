def rc4_key_schedule(key):
    key_length = len(key)
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + int(S[i]) + int(key[i % int(key_length)])) % 256
        S[i], S[j] = S[j], S[i]

    return S

def rc4_encrypt(data, key):
    S = rc4_key_schedule(key)
    i = j = 0
    result = []

    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        result.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

    return ''.join(result)

def rc4_decrypt(data, key):
    # RC4 encryption and decryption are the same operation
    return rc4_encrypt(data, key)

# Exemple d'utilisation :
if __name__ == "__main__":
    plaintext = "Hello, World!"
    key = "SecretKey"

    ciphertext = rc4_encrypt(plaintext, key)
    decrypted_text = rc4_decrypt(ciphertext, key)

    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted text: {decrypted_text}")
