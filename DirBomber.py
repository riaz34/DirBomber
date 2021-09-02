#!//usr/bin/python

import requests

domain = input("Enter the Domain name: ")

file = open("dir.txt")

content = file.read()

directories = content.splitlines()

for dir in directories:

    response = requests.get(f"http://{domain}/{dir}")
    url = f"http://{domain}/{dir}"

    if response.status_code == 200:
        print("[*] Discoverd Directory:",url)

    elif response.status_code == 404:
        pass 
