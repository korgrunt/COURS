*Usage pour un participant legitime:
  $ openssl genrsa 2048 > my_ciph_priv.pem [my_ciph_pub.pem]
  $ openssl genrsa 2048 > my_sign_priv.pem [my_sign_pub.pem]


# mode correction
  // Proteger input_file
  $ python multi_protect.py -e <input_file> <output_file> <my_sign_priv.pem> <my_ciph_pub.pem> [<other_ciph_pub.pem> <other_ciph_pub_1.pem>... <other_ciph_pub_n.pem>]
  // retourne 0 si OK, 1 sinon

  // Deproteger input_file
  $ python multi_protect.py -d <input_file> <output_file> <my_priv_ciph.pem> <my_pub_ciph.pem> <sender_sign_pub.pem>
  // retourne 0 si OK, 1 sinon



# mode dev
  // Proteger input_file
  $ python3 multi_protect.py -e input_file output_file my_sign_priv.pem my_ciph_pub.pem other_ciph_pub.pem other_ciph_pub_1.pem other_ciph_pub_n.pem
  // retourne 0 si OK, 1 sinon

  // Deproteger input_file
  $ python3 multi_protect.py -d input_file output_file my_priv_ciph.pem my_pub_ciph.pem sender_sign_pub.pem
  // retourne 0 si OK, 1 sinon