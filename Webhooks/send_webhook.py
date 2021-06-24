import requests
import json

webhook_url = 'http://127.0.0.1:5000/webhook'

to_send = {'name': 'Nishant Nirmal',
        'email': 'nirmalnishant645@gmail.com',
        'city': 'Mumbai'}

r = requests.post(webhook_url, data=json.dumps(to_send), headers={'Content-Type': 'application/json'})  # Sending data using Post() request as webhook