#Python 2.7
#Used for the initial setup (one time use)
import os, hashlib
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

raw_key = RSA.generate(2048)
private_key = raw_key.exportKey('PEM')
try:
    with open('master_private.pem', 'w+') as keyfile:
        keyfile.write(private_key)
        keyfile.close()
    print "[*] Successfully created your local RSA private key"
except:
    print "[*] Error creating your key"

make_public = raw_key.publickey()
public_key = make_public.exportKey('PEM')
try:
    with open("master_public.pem", "w+") as keyfile:
        keyfile.write(public_key)
        keyfile.close()
    print "[*] Successfully created your local RSA public key"
except:
    print "[*] Error creating your key"
