"""Encryption with asymmetric key
rsa library
Two keys, a public key and a private key
No one has your private key (no man in the middle attack)
"""

import rsa

publicKey, privateKey = rsa.newkeys(512)

msg = "password_123"
encrypted = rsa.encrypt(msg.encode(), publicKey)
decrypted = rsa.decrypt(encrypted, privateKey).decode()

print(encrypted)
print(decrypted)