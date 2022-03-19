# Made by ads#2000 (although im 90% sure that someones just gonna remove this line and take it as their own)
# You can not use this code for commerical purposes unless allowed to by the rightful owner, ads#2000.

# Make sure you have all of these modules installed by using pip :D
import time
import requests
import json
import sys

first = '{"custom_status":{"text":"Skill tree application coming out in"}}'
second = '{"custom_status":{"text":"November 2022"}}'
url = 'https://discord.com/api/v9/users/@me/settings'
contento = 'application/json'
auth = 'Put your discord token here' # Search up how to find your discord token, once you have it, replace the text with your token.

while True: # The loop that switches the statuses, you don't have to touch anything in here
    header = {
        'authorization': auth,
        'content-type': "application/json"
        }

    r = requests.patch(url,
                       data=first, headers=header)

    time.sleep(3)
    r = requests.patch(url,
                       data=second, headers=header)
    time.sleep(3)
