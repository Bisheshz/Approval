import os
import requests
import sys

def ckx():
    bis = 'https'
    he = 'github'
    sh = 'LordBishesh'
    
    uuid = "BISHESH" + str(os.geteuid()) + str(os.getlogin())
    id = "→".join(uuid)
    print("ID:", id)
    
    try:
        server = requests.get(f'{bis}://{he}.com/{sh}/Bisheshz/raw/main/a.txt').text
        httpCaht = requests.get(f"{bis}://{he}.com/{sh}/Bisheshz/raw/main/b.txt").text
        
        if id in server and id in httpCaht:
            print("Hi, I'm Bishesh")
            msg = str(os.geteuid())
            pass
        else:
            msg = str(os.geteuid())
            #fucked()
    except:
        sys.exit()

ckx()
