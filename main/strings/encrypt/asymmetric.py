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

print(encrypted)
print(decrypted)