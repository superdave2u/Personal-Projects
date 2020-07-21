#!/usr/bin/env python

import requests

r = requests.get("http://natas0.natas.labs.overthewire.org" , auth=('natas0', 'natas0'))
print(r.status_code)
print(r.text)

