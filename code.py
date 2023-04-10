#!/usr/bin/env python3

from pwn import *
import sys
from base64 import b64decode
import re
import decimal
io = remote('43.204.138.14','32369',level="DEBUG"
data =  io.recvall()
a,b = data.split(':',1)

def rot13(str):
	return ''.join([chr((ord(letter) - 97 + 13) % 26 + 97) for letter in str.lower()])
 
if "base64" in b :
       v = b64decode(b)
       print(v)
	io.sendline(v)

elif "rot13" in b :
      
      v=rot13(b)
      print(v)
    io.sendline(v)

elif  "decimal" in b :

       dec = decimal.Decimal("b")
       str(dec)
     io.sendline(v)
else 
	print(error)

io.interactive()
