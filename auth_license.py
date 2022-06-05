# Github: SkullCode

# U NEED REQUESTS INSTALLED
# Install Command: 'pip install requests'

# Any bugs contact SkullCode#1878



import requests
import time

key = input("License key: ")

url = "https://pastebin.com/raw/key"

r = requests.get(url)

try:
    if key in r.text:
        print("Valid Key")
        pass
    else:
        print("Invalid Key!")
        time.sleep(30)
        exit()
except:   
    print("Something went wrong")
    time.sleep(30)
    exit()