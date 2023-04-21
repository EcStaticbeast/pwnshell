from pwn import *
#import binascii
from base64 import b64decode
from decimal import Decimal
io = remote('localhost',1337)#,level="DEBUG")
data =  io.recvlines(2)[1].decode()
a,b = data.split(': ')
print(a)
def rot13(str):
    return ''.join([chr((ord(letter) - 97 + 13) % 26 + 97) for letter in str.lower()])
if "base64" in a :
    v = b64decode(b)
    print("b64")
    print(v)
    io.sendline(v)
elif "rot_13" in a :
    print("rot13")
    v=rot13(b)
    io.sendline(v)
    
elif "decimal" in a :
    result = 0
    b = b.split()
    c = []
    v = ''
    print (b)
    for d in b:
       integer = int(b[result])
       c.append(integer)
       v = chr(c[result])
#       v.append.append(v)
#       print(v)
       print((v),end="")
#       s.strip()
#       print (s)
       result += 1
#    s.append(v)
#    print(s)
    io.sendline(v)#,end="")
else :
    print(error)
print(io.recvline())
