#!/usr/bin/env python

import requests

r = requests.get("http://natas1.natas.labs.overthewire.org" , auth=('natas1', 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'))
print(r.status_code)
print(r.text)

