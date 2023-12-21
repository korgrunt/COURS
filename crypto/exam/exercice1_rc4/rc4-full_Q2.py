#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: @manojpandey

# Python 3 implementation for RC4 algorithm
# Brief: https://en.wikipedia.org/wiki/RC4

# Will use codecs, as 'str' object in Python 3 doesn't have any attribute 'decode'
import codecs
import random

MOD = 256

value_of_s2 = None
value_of_s1 = None

value_of_byte_1 = None
value_of_byte_2 = None
value_of_byte_3 = None

list_of_seconde_bytes = []
global seconde_bytes_count
seconde_bytes_count = 0
global seconde_bytes_at_zero_count
seconde_bytes_at_zero_count = 0

def KSA(key, clear_key):
    ''' Key Scheduling Algorithm (from wikipedia):
        for i from 0 to 255
            S[i] := i
        endfor
        j := 0
        for i from 0 to 255
            j := (j + S[i] + key[i mod keylength]) mod 256
            swap values of S[i] and S[j]
        endfor
    '''
    key_length = len(key)
    # create the array "S"
    S = list(range(MOD))  # [0,1,2, ... , 255]
    j = 0
    for i in range(MOD):
        j = (j + S[i] + key[i % key_length]) % MOD
        S[i], S[j] = S[j], S[i]  # swap values

    
    return S


def PRGA(S):
    ''' Psudo Random Generation Algorithm (from wikipedia):
        i := 0
        j := 0
        while GeneratingOutput:
            i := (i + 1) mod 256
            j := (j + S[i]) mod 256
            swap values of S[i] and S[j]
            K := S[(S[i] + S[j]) mod 256]
            output K
        endwhile
    '''
    i = 0
    j = 0
    while True:
        i = (i + 1) % MOD
        j = (j + S[i]) % MOD

        S[i], S[j] = S[j], S[i]  # swap values
        K = S[(S[i] + S[j]) % MOD]
        yield K


def get_keystream(formated_key, clear_key):
    ''' Takes the encryption key to get the keystream using PRGA
        return object is a generator
    '''
    S = KSA(formated_key, clear_key)
    return PRGA(S)


def encrypt_logic(key, text):
    global seconde_bytes_count
    global seconde_bytes_at_zero_count
    ''' :key -> encryption key used for encrypting, as hex string
        :text -> array of unicode values/ byte string to encrpyt/decrypt
    '''
    # For plaintext key, use this
    formated_key = [ord(c) for c in key]
    # If key is in hex:
    # key = codecs.decode(key, 'hex_codec')
    # key = [c for c in key]
    keystream = get_keystream(formated_key, key)
  
    next(keystream)


 
    second = next(keystream)
    if(second == 0):
        seconde_bytes_at_zero_count+=1
    seconde_bytes_count+=1

    return ""
    res = []
    for c in text:
        val = ("%02X" % (c ^ next(keystream)))  # XOR and taking hex
        res.append(val)
    return ''.join(res)


def encrypt(key, plaintext):
    ''' :key -> encryption key used for encrypting, as hex string
        :plaintext -> plaintext string to encrpyt
    '''
    plaintext = [ord(c) for c in plaintext]
    return encrypt_logic(key, plaintext)


def decrypt(key, ciphertext):
    ''' :key -> encryption key used for encrypting, as hex string
        :ciphertext -> hex encoded ciphered text using RC4
    '''
    ciphertext = codecs.decode(ciphertext, 'hex_codec')
    res = encrypt_logic(key, ciphertext)
    return codecs.decode(res, 'hex_codec').decode('utf-8')

def generate_random_key():
    dictionary = "abcdefghijklmnopqrstuvwxyz123456789AZERTYUIOPMLKJHGFDSQWXVCBN"
    random_key = ""
    for i in range(1, 9):
        random_key += dictionary[random.randrange(1,60)]
    print(random_key)
    return random_key

def main():

    while True:
        key = generate_random_key()  # plaintext
        plaintext = 'Good work! Your implementation is correct'  # plaintext
        # encrypt the plaintext, using key and RC4 algorithm
        ciphertext = encrypt(key, plaintext)
        print("seconde_bytes_at_zero_count")
        print(seconde_bytes_at_zero_count)
        print("seconde_bytes_count")
        print(seconde_bytes_count)

    print("NOTHING FOUND")
    return

    print('plaintext:', plaintext)
    print('ciphertext:', ciphertext)
    # ..
    # Let's check the implementation
    # ..
    ciphertext = '2D7FEE79FFCE80B7DDB7BDA5A7F878CE298615'\
        '476F86F3B890FD4746BE2D8F741395F884B4A35CE979'
    # change ciphertext to string again
    decrypted = decrypt(key, ciphertext)
    print('decrypted:', decrypted)

    if plaintext == decrypted:
        print('\nCongrats ! You made it.')
    else:
        print('Shit! You pooped your pants ! .-.')

    # until next time folks !




main()