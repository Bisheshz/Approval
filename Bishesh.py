import os
import requests
import sys
import time

protocol = 'https'
host = 'github'
username = 'LordBishesh'
repository = 'Bisheshz'
file_path = 'a.txt'

def check_id_key():
    uid = str(os.geteuid())
    login = str(os.getlogin())
    id_key = f"BISHESH → {uid} → {login}"
    print("ID Key:", id_key)

    input("Press Enter to continue...")

    while True:
        url = f'{protocol}://{host}.com/{username}/{repository}/blob/main/{file_path}'
        try:
            server = requests.get(url).text
            print("Content retrieved:", server)

            if "Id" in server and id_key in server:
                print("Thanks for purchasing my tool.")
                sys.exit()
            else:
                print("Id key not found. Exiting...")
                sys.exit()

        except requests.RequestException as e:
            print(f"Error: {e}")
        
        time.sleep(1)  # Adjust the sleep time as needed

# Call the function
check_id_key()
