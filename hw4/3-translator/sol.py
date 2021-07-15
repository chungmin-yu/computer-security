from pwn import *
#Task3: translater
conn = remote('140.113.207.240',8833)
conn = process('./translator')

r=conn.recv()
#print(r.decode('ascii'))
conn.sendline('<6A;')
r=conn.recv()
#print(r.decode('ascii'))
conn.sendline('n')
r=conn.recv()
#print(r.decode('ascii'))
conn.sendline('<6A;')
r=conn.recvrepeat()
print(r)
conn.close()

