#!/usr/local/bin/python3

import requests 
import json

response = requests.get("https://mobile.fmcsa.dot.gov/qc/services/carriers/name/greyhound?&size=5&webKey=5aaae40cb05d32250644c60be54940db879aafec")

data = json.dumps(response.json(), indent=4)

print(data)
# print(response.json())