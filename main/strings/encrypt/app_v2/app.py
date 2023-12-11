"""Encrypt App (cmd)
Using an asymmetric public key

$ cd encrypt/app2
$ python app2.py encrypt pass_123
$ python decrypt master_pass
"""

import sys, rsa

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

action = sys.argv[1]

if action == 'encrypt':
    msg = sys.argv[2]
    with open('./public.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
        with open('./password.bin', 'wb') as f:
            encrypted = rsa.encrypt(msg.encode(), publicKey)
            f.write(encrypted)
            print(encrypted)

if action == 'decrypt':
    master_pass = sys.argv[2]
    if master_pass != 'master_pass':
        sys.exit('Wrong master password')
    with open('./password.bin', "rb") as f:
        encrypted = f.read()
    with open('./restricted/private.pem', "rb") as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
        decrypted = rsa.decrypt(encrypted, privateKey).decode()
        print(decrypted)