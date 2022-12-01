"""Symmetric key Ecryption

Fernet library
    pip install cryptography

Data is encoded and decoded with the same key
The receiver needs the key for decryption
Less secure, man in the middle attack
"""

from cryptography.fernet import Fernet

key = Fernet.generate_key()
obj = Fernet(key) # intance

msg = "password_123"
encrypted = obj.encrypt(msg.encode())
decrypted = obj.decrypt(encrypted).decode()

print(encrypted)
print(decrypted)