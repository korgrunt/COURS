import hashlib
import lief

binary = lief.parse("original_binary")
binary.remove_signature()
binary.write("binary.nosigned")

filename = input("/home/naouaichia/Workspace/COURS/ios/original_binary")
with open(filename,"rb") as f:
    bytes = f.read() # read entire file as bytes
    readable_hash = hashlib.sha256(bytes).hexdigest();
    print(readable_hash)