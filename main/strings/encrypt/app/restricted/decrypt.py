"""Decrypt text
Public encrypted.bin containing encrypted password
Use private.pem restricted private key
"""

import rsa, os

DIR = os.path.dirname(os.path.realpath(__file__))

with open(DIR + '/../encrypted.bin', "rb") as f:
    encrypted = f.read()
        
    with open(DIR + '/private.pem', "rb") as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
        decrypted = rsa.decrypt(encrypted, privateKey).decode()
        
print(encrypted)
print(privateKey)
print(decrypted)