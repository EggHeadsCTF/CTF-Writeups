from pwn import *

p = remote('cfta-nm01.allyourbases.co', 8017)

def solve():
    eq = p.recv()
    eq = str(eq).replace("x", "").replace("\\", "").replace("b", "").replace("'", "").replace("n", "")
    print(eq)
    val = bytearray.fromhex(eq).decode()
    print(val)
    p.sendline(val)


solve()
solve()

p.interactive()