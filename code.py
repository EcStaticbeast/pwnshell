from pwn import *
from base64 import b64decode
from decimal import Decimal


io = remote('localhost',1337)#,(level="DEBUG")
data =  io.recvlines(2)[1].decode()
a,b = data.split(': ')
print(a)


def rot13(str):
    return ''.join([chr((ord(letter) - 97 + 13) % 26 + 97) for letter in str.lower()])
s = ''

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
    print(b)
    for d in b:
       integer = int(b[result])
       c.append(integer)
       v = chr(c[result])
       s = ''.join((s,v))
       result += 1
    print(s)
    io.sendline(s)
else :
    print(error)

stage2 =  io.recv()
# print(stage2)
e,f,g = stage2.split(b':',(2))
# print(e)
print(f) #cipher
print(g) #key


def decryption(a,b): 
        orig_text = [] 
        for i in range(len(a)): 
            if i<len(b):
               x = (ord(a[i]) -ord(b[i]) + 26) % 26
               x += ord('A')  
               print (i)
            else :
                x = (ord(a[i]) -ord(b[i%len(b)]) + 26) % 26
                x += ord('A')  
                print (i)           
            orig_text.append(chr(x)) 
        return("" . join(orig_text))    
        
f="KOGPC BFVGS"
g="DORAEMON"
t = f.replace(" ","")

print(decryption(t,g))  
w = (decryption(t,g))

# print(w)                                                #decrypted text

j = ("" . join(w))[0:5],("" . join(w))[5:10]
k = (j[0] + " " + j[1])

print (k)
io.sendline (k)


stage3 = io.recv()
print(stage3)


# print(io.recv())
# print(io.interactive())
