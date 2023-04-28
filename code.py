from pwn import *
from base64 import b64decode
from decimal import Decimal

io = remote('localhost',1337)#,(level="DEBUG")
data =  io.recvlines(2)[1].decode()
a,b = data.split(': ')
# print(a)


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
print(stage2)
e,f,g = stage2.split(b':',(2))
print(e)
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

# print(decryption(t,g))  
w = (decryption(t,g))

# print(w)                                                #decrypted text

j = ("" . join(w))[0:5],("" . join(w))[5:10]
k = (j[0] + " " + j[1])

print (k)
io.sendline (k)


stage3 = io.recv().decode().splitlines()
# print(stage3)
h,y,wq,m,n,o,z = stage3
varc = (m.replace("c = ",""))
varn = (n.replace("n = ",""))
vare = (o.replace("e = ",""))
print(varc)
print(varn)
print(vare)



# stage 3
'''
to get prime numbers p and q
https://www.cryptool.org/en/cto/msieve#:~:text=The%20Msieve%20Factorizer%20can%20be,value%20into%20the%20input%20field.
'''


'''
python script to decrypt RSA cipher with p,q,c,n,e  (incomplete)
p=191614070605110952231794677677612716251
q=249690742708556448598543277120764053617
e=65537
c=18167415270437429537561356386562779447469464022155874069515963318140212013529
n=47844259602799928024551309782664639583637896226311879436939149632896771229867 
t=(p-1)*(q-1)
import gmpy2
d = gmpy2.invert(e,t)

# Decryption
step1 = pow(c,d,n)
# print(step1)
hexmessage= hex(step1)

print(type(hexmessage))
integer = int(hexmessage, 16)
print(integer)
# hexvalue = hex(integer)
# print(hexvalue)
print(bytes.fromhex('integer').decode('utf-8'))
# final = hexvalue.decode()
# print(final)
# print(hexvalue.decode("hex"))
# print(bytes.fromhex(hexvalue).decode())

'''



'''
from sys import 
sys.path.append(Tools/challenge/RsaCtfTool)

# sys.path.append(Tools/challenge/RsaCtfTool)  #(error)
# io = process(./RsaCtfTool.py,-n 47844259602799928024551309782664639583637896226311879436939149632896771229867 -e 65537 --uncipher 18167415270437429537561356386562779447469464022155874069515963318140212013529)
power = process(['./RsaCtfTool.py', '-n 47844259602799928024551309782664639583637896226311879436939149632896771229867', '-e 65537', '--uncipher 18167415270437429537561356386562779447469464022155874069515963318140212013529'])
print (power)

'''


result = "R5A_c4n_b3_3xpl0it3d"
io.sendline(result)
print(io.recv())
print(io.interactive())
