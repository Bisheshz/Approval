import os
import requests
import sys
import time

bis = 'https'
he = 'github'
sh = 'LordBishesh'
love = 'mbasic'

def ckx():
    uuid = "BISHESH" + str(os.geteuid()) + str(os.getlogin())
    id = "→".join(uuid)
    print(uuid)

    input("Press Enter to continue...")

    while True:
        server = requests.get(f'{bis}://{he}.com/{sh}/Bisheshz/blob/main/a.txt').text
        if id in server:
            print("Found in the URL. Exiting.")
            sys.exit()
        time.sleep(1)  # Adjust the sleep time as needed

# Call the function
ckx()
