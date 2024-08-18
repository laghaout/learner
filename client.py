# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 19:20:54 2024

@author: amine
"""

'''
Script for inferencing the deployed model
'''

import json
import requests

data = [{"age": 100, "city": "Toronto"},
        {"age": 42, "city": "Rabat"},
        {"age": 12, "city": "Amizmiz"}]

url = 'http://localhost:8000/predict/'

predictions = []
for record in data:
    payload = {'features': record}
    payload = json.dumps(record)
    response = requests.post(url, data=payload)
    predictions.append(response.json()['prediction'])

print(predictions)

