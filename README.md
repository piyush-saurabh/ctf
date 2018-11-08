# ctf
This repository contains the exploit scripts I used in different CTFs

#jail.py
This python script helps to interact with the network services. It is as BOF script which exploits a network service which other wise can be accessed via telnet/nc. The payload is "socket reuse" shellcode which can be found at https://www.exploit-db.com/exploits/34060/

#calamity.py
This is a buffer overflow exploit script using ret2libc method to "execl" function and get the shell using wrapper(wrapper.c).

#wrapper.c
This is a wrapper function which helps in privilege escalation if setuid bit is set. "system" drops the effective user id so it is important to use a wrapper function to explicitly set the "setuid" and "setgid" bits before opening a shell

#webshell.war
Java webshell for deployment via tomcat.

#webshell.jsp
Java webshell for deployment via file upload.

#cors-csrf.html
If a website contain **access-control-allow-credentials: true** in response, then it can be used to exploit CSRF. Using the script, we can send cross domain AJAX request via GET and POST method. This file contains the javascript to parse the CSRF token from AJAX response and exploit CSRF vulnerability. 

#blind-sql.py
This script is used to perform **Blind SQL Injection** in mongodb. Edit the script to give the list of allowed characters for brute forcing. This script sends the GET request to the remote server with the SQL Injection payload.


