# ctf
This repository contains the exploit scripts I used in different CTFs

#jail.py
This python script helps to interact with the network services. It is as BOF script which exploits a network service which other wise can be accessed via telnet/nc. The payload is "socket reuse" shellcode which can be found at https://www.exploit-db.com/exploits/34060/

#calamity.py
This is a buffer overflow exploit script using ret2libc method to "execl" function and get the shell using wrapper(wrapper.c).
