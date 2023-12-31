import os
import requests
import time

def approval():
    uuid = str(os.geteuid()) + "DS" + str(os.geteuid())
    id = "A7S-" + "".join(uuid)
    os.system('clear')

    print("\033[1;37m [\u001b[36m•\033[1;37m] You Need Approval To Use This Tool   \033[1;37m")
    print("\033[1;37m [\u001b[36m•\033[1;37m] Your Key :\u001b[36m " + id)
    time.sleep(0.1)
    print("\033[1;37m----------------------------------------------")
    
    try:
        httpChat = requests.get("https://github.com/LordBishesh/Bisheshz/blob/main/a.txt").text
        if id in httpChat:
            print("\033[1;97m >> Your Key Has Been Approved !!!")
            msg = str(os.geteuid())
            time.sleep(1)
        else:
            print("\x1b[1;97m >> FB Ma Send Han Key Bhaii ")
            time.sleep(0.1)

            input(' >> Click Enter To Send Your Key ')

            os.system('xdg-open https://www.facebook.com/alkesh.hero.hu.yar')

            time.sleep(1)

            exit()

    except Exception as e:
        print(" >> Unable To Fetch Data From Server: ", str(e))
        time.sleep(2)
        exit()

approval()
