import subprocess
import random
import string

import codecs
import random
import string
import os
from random import randbytes
import pyradamsa
import threading

code_found = []

def execute(inp: bytearray, seed):

    tmpfn = f"tmp.txt"

    with open(tmpfn, "wb") as fd:
        fd.write(inp)

    sp = subprocess.Popen(
        ["./lci", tmpfn],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL)
    
    ret= sp.wait()
 

    #print(inp)
    if((ret) not in code_found):
        code_found.append(ret)
        print(f"seed: {str(seed)} --- ret: {str(ret)}")

    


def read_random_file(directory_path):
    # Get a list of all files in the specified directory
    file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # Check if there are any files in the directory
    if not file_list:
        print("No files found in the directory.")
        return None

    # Choose a random file from the list
    random_file = random.choice(file_list)

    # Construct the full path to the randomly selected file
    file_path = os.path.join(directory_path, random_file)

    # Read the content of the file as bytes
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
        return file_content
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return None
    

rad = pyradamsa.Radamsa()

def execute_avec_timeout(fuzzed, random_integer):
    # Mettez ici la durée maximale d'exécution en secondes
    timeout_duree = 3

    # Créer le thread Timer
    timer_thread = threading.Timer(timeout_duree, timeout_callback)

    try:
        # Démarrer le thread Timer
        timer_thread.start()

        # Appeler votre fonction à exécuter
        execute(fuzzed, random_integer)
    finally:
        # Annuler le thread Timer après l'exécution de la fonction
        timer_thread.cancel()

def timeout_callback():
    # Cette fonction sera appelée si le délai d'attente est dépassé
    print("Temps d'exécution dépassé. La fonction est annulée.")
    for x in range(1000000000):
        #print(random_string)
        random_file = read_random_file("./corpus")

        random_integer = random.randint(1, 9999999999999999999)
        fuzzed = rad.fuzz(random_file)
        #print(fuzzed)
        #print(random_file)
        execute_avec_timeout(fuzzed, random_integer)


for x in range(1000000000):
    #print(random_string)
    random_file = read_random_file("./corpus")

    random_integer = random.randint(1, 9999999999999999999)
    fuzzed = rad.fuzz(random_file)
    #print(fuzzed)
    #print(random_file)
    execute_avec_timeout(fuzzed, random_integer)


 

