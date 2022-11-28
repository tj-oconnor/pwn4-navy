from pwn import *

binary = args.BIN
HOST = args.HOST

context.terminal = ["tmux", "splitw", "-h"]
e = context.binary = ELF(binary)
r = ROP(e)

gs = '''
continue
'''


def start():
    if args.GDB:
        return gdb.debug(e.path, gdbscript=gs)
    elif args.REMOTE:
        return remote(HOST, 1337)
    else:
        return process(e.path)

'''
00400d4c  e007c1a8   ldp     x0, x1, [sp], #0x10 {arg1} {arg2}
00400d50  fd7bc1a8   ldp     x29, x30, [sp], #0x10 {arg3} {arg_18}
00400d54  c0035fd6   ret     
'''

p = start()

'''
Build your chain here
'''

p.interactive()
