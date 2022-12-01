"""Encryption with asymmetric key

Rsa library
    pip install rsa
    
Two keys, a public key and a private key
No one has your private key
"""

import rsa

publicKey, privateKey = rsa.newkeys(512)

msg = "password_123"
encrypted = rsa.encrypt(msg.encode(), publicKey)
decrypted = rsa.decrypt(encrypted, privateKey).decode()

print(encrypted) # b'\x07z\x110\xb4\x05\xcb\xb8\x0b[FN2\xeb'
print(decrypted) # password_123