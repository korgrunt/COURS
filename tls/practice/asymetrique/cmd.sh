# clear file asym_plain_text.txt to encrypted file asym_file_out.txt with signature in file
python3 protect_asymetric.py password ./asym_plain_text.txt ./asym_file_out.txt

# encrypted file asym_file_out.txt with signature in file to clear file asym_file_out.txt with signature check 
python3 unprotect_asymetric.py public_sign.pem private_cypher.pem ./asym_file_out.txt ./unprotected.txt
