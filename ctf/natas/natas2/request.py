#!/usr/bin/env python

NATAS="natas2"

import requests

r = requests.get("http://" + NATAS + ".natas.labs.overthewire.org/files/" , auth=(NATAS, 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'))

#from PIL import Image
#from io import BytesIO
#i = Image.open(BytesIO(r.content))
#print(i) 
#image = Image.open(r.text) 
#print(image)
print(r.status_code)
print(r.text)
print(r.encoding)
print(r.headers)

