#!//usr/bin/python

import requests

domain = input("Enter the Domain name: ")

file = open("dir.txt")

content = file.read()

directories = content.splitlines()

for dir in directories:
    
    url = f"http://{domain}:3333/{dir}"
    try:

        requests.get(url)
        print("[*] Discovered Directory:", url)

    except requests.ConnectionError:

        pass
