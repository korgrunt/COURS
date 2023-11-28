# clear file sym_plain_text.txt to encrypted file sym_file_out.txt with hmac integrity in file
python3 protect_symetric.py password ./sym_plain_text.txt ./sym_file_out.txt

# encrypted file sym_file_out.txt to clear file unprotected_file_out.txt with hmac integrity check from hmac_digest in file
python3 unprotect_symetric.py password ./sym_file_out.txt ./unprotected_file_out.txt
