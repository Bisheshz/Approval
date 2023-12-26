import platform
import requests
import hashlib
import sys

def get_device_model():
    return platform.uname().machine

def generate_device_code(device_model):
    # Use a combination of device model and a secret key to generate a unique code
    secret_key = "your_secret_key"
    code = hashlib.sha256(f"{device_model}{secret_key}".encode()).hexdigest()
    return code

def check_code_on_links(code, links):
    for link in links:
        response = requests.get(link)
        if code in response.text:
            return True
    return False

def main():
    device_model = get_device_model()
    device_code = generate_device_code(device_model)
    
    # Update the links with your actual URLs
    links_to_check = [
        f'{bis}://{he}.com/{sh}/Bisheshz/blob/main/a.txt',
        f'{bis}://{he}.com/{sh}/Bisheshz/blob/main/b.txt'
    ]

    if check_code_on_links(device_code, links_to_check) and id in httpCaht:
        print("Device approved. Proceed with the task.")
        # Add your task logic here
    else:
        print("Device not approved. Exiting...")
        sys.exit()

if __name__ == "__main__":
    main()

