"""Encrypt App (cmd)
Using an asymmetric public key

$ cd encrypt/app2
$ python app2.py encrypt pass_123
$ python decrypt master_pass
"""

import sys, rsa

if len(sys.argv) < 2: # Check cmd arguments
    sys.exit("Too few arguments")

action = sys.argv[1]

if action == 'encrypt':
    msg = sys.argv[2] # pass_12333

    with open('./public.pem', 'rb') as p: # Read public key
        publicKey = rsa.PublicKey.load_pkcs1(p.read())

        with open('./password.bin', 'wb') as f: # Write encrypted
            encrypted = rsa.encrypt(msg.encode(), publicKey)
            f.write(encrypted)
            print(encrypted) # b'[\xd6z\x7fP@\x96\x91\xa5\x01\x82\r'

if action == 'decrypt':
    master_pass = sys.argv[2]

    if master_pass != 'abc_123': # Check master
        sys.exit('Wrong master password')

    with open('./password.bin', "rb") as f: # Read encrypted
        encrypted = f.read()
    
    with open('./restricted/private.pem', "rb") as p: # decryt, with private key
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
        decrypted = rsa.decrypt(encrypted, privateKey).decode()
        print(decrypted) # pass_12333