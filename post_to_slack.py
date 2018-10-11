# coding: utf-8

import requests 

endpoint = "" # Replace with you Slack webhook
data = {"text":"Hello, World! From Ipython"}
requests.post(endpoint, json=data)
