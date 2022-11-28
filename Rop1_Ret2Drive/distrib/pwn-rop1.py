from pwn import *

binary = args.BIN
HOST   = args.HOST
CMD    = args.CMD

KEYS = {'u':b'w','d':b's','l':b'a','r':b'd','t':b't'}

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
        return remote(HOST,1337)
    else:
        return process(e.path)

p = start()

'''
Build you chain here
'''

p.interactive()

