"""Generate keys
Two keys, a public key and a private key
"""

import rsa, os

publicKey, privateKey = rsa.newkeys(512)

DIR = os.path.dirname(os.path.realpath(__file__))

with open(DIR + '/../public.pem', 'wb') as p:
    p.write(publicKey.save_pkcs1('PEM'))
    
with open(DIR + '/private.pem', 'wb') as p:
    p.write(privateKey.save_pkcs1('PEM'))
    
print(publicKey)
print(privateKey)