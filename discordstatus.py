import time
import requests
import json
import sys
url = 'https://discord.com/api/v9/users/@me/settings'
contento = 'application/json'
dataz = '{"custom_status":{"text":"November 2022"}}'
dato = '{"custom_status":{"text":"Skill tree application coming out in"}}'
auth = 'Put your discord token here'

while True:
    header = {
        'authorization': auth,
        'content-type': "application/json"
        }

    r = requests.patch(url,
                       data=dato, headers=header)

    time.sleep(3)
    r = requests.patch(url,
                       data=dataz, headers=header)
    time.sleep(3)
