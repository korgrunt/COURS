

def key_schedule(key):
    sched = [i for i in range(0, 256)]

    i = 0
    for j in range(0, 256):
        i = (i + sched[j] + key[j % len(key)]) % 256
        sched[i], sched[j] = sched[j], sched[i]

    return sched

def stream_generation(key_sched):
    stream = []
    i = 0
    j = 0

    while True:
        i = (1 + i) % 256
        j = (key_sched[i] + j) % 256
        key_sched[i], key_sched[j] = key_sched[j], key_sched[i]
        yield key_sched[(key_sched[i] + key_sched[j]) % 256]

def encrypt(plaintext, key):
    text = [ord(char) for char in plaintext]
    key = [ord(char) for char in key]
    cypher_text = ""

    for_stat = [0 for x in range(1000)]
    key_sched = key_schedule(key) 
    key_stream = stream_generation(key_sched)

    for idx in range(0, 1000):
        for_stat[idx] = next(key_stream)
    print("for_stat")
    print(for_stat)
    print("_____________")

    for char in plaintext:
        encrypted = str(hex(ord(char) ^ next(key_stream))).upper()
        cypher_text += encrypted

    print(f"key {key}")
    print(f"text {text}")
    print(f"key_sched {key_sched}")
    return cypher_text

if __name__ == "__main__":
    plaintext = "Hello Cypher World! Hello Cypher World! Hello Cypher World! Hello Cypher World! Hello Cypher World! Hello Cypher World! Hello Cypher World! "
    key = "key_for_e"
    action = "E" # "E" for encrypt, "D" for decrypt
    
    result = encrypt(plaintext, key)
    print(result)

