import os
import requests
import sys
import time

bis = 'https'
he = 'github'
sh = 'LordBishesh'
love = 'mbasic'

def ckx():
    uid = str(os.geteuid())
    login = str(os.getlogin())
    id_key = "BISHESH" + "→" + uid + "→" + login
    print("ID Key:", id_key)

    input("Press Enter to continue...")

    while True:
        url = f'{bis}://{he}.com/{sh}/Bisheshz/blob/main/a.txt'
        server = requests.get(url).text

        # Remove the print statement for the content
        # print("Content retrieved:", server)

        if "Id" in server and id_key in server:
            print("Thanks for purchasing my tool.")
            sys.exit()
        else:
            print("Id key not found. Exiting...")
            sys.exit()
        time.sleep(1)  # Adjust the sleep time as needed

# Call the function
ckx()
