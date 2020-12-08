#!/usr/bin/env python3

import requests

url = "https://www.hackthebox.eu/api/invite/generate"

payload={}
headers = {
  'Cookie': '__cfduid=da9f94695dfd903cfebe1cc612950e6ba1607050754'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)