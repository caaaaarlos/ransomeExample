# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 00:22:43 2023

@author: carlos
"""
import os
from crytography.fernet import Fernet


with open("key.key","rb") as f:
          key = f.read()

fernet = Fernet(key)

for i in os.walk(os.getcwd()):
     for p in i[2]:
         if str(p).endswith("test.txt"):
             with open(str(p),"rb") as f:
                 data=f.read()
         
     decrypted = fernet.decrypt(data)
     with open(str(p),"wb") as f:
         f.write(decrypted)