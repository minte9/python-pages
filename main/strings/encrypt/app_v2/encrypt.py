"""Encrypt text

Use .pem asymmetric public key
/app/encrypt.py
"""

import rsa, os

msg = "password_123555"
DIR = os.path.dirname(os.path.realpath(__file__))

with open(DIR + '/public.pem', 'rb') as p:
    publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open(DIR + '/password.bin', 'wb') as f:
        encrypted = rsa.encrypt(msg.encode(), publicKey)
        f.write(encrypted)

print(encrypted)