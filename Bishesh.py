import os
import requests
import sys
import time

def cks():
    uuid = "BISHESH" + str(os.geteuid()) + str(os.getlogin())
    id = "→".join(uuid)
    os.system('clear')

    print("\033[1;37m [\u001b[36m•\033[1;37m] You Need Approval To Use This Tool   \033[1;37m")
    print("\033[1;37m [\u001b[36m•\033[1;37m] Your Key :\u001b[36m " + id)
    time.sleep(0.1)
    print("\033[1;37m----------------------------------------------")

    try:
        httpChat = requests.get(f"{bis}://{he}.com/{sh}/Bisheshz/blob/main/b.txt").text
        if id in httpChat:
            print("\033[1;97m >> Your Key Has Been Approved !!!")
            msg = str(os.geteuid())
        else:
            print("\x1b[1;97m >> FB Ma Send Han Key Bhaii ")
            time.sleep(0.1)
            input(' >> Click Enter To Send Your Key ')
            os.system('xdg-open https://www.facebook.com/alkesh.hero.hu.yar')
            time.sleep(1)
            sys.exit()
    except Exception as e:
        print(" >> Unable To Fetch Data From Server: ", str(e))
        time.sleep(2)
        sys.exit()

cks()
