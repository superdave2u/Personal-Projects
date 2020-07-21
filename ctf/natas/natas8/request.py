#!/usr/bin/env python

import requests
import json
NATAS = "natas8"
PASS = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
URL = "http://" + NATAS + ".natas.labs.overthewire.org"
#payload = { 'secret': 'FOEIUWGHFEEUHOFUOIU', 'submit': True }
#r = requests.get(URL , auth=(NATAS, PASS))
r = requests.post(URL , auth=(NATAS, PASS), data={'secret': 'oubWYf2kBq', 'submit': True })
print(r.text)
print(r.history)
print(r.status_code)


print(r.headers)
