from mygpoclient import public, testing, locator, api, simple
import requests
import json


l = locator.Locator('ashinde21')
print(l.subscriptions_uri(format='json'))

username = 'ashinde21'
password = 'Marco21reus'
url = 'https://gpodder.net/subscriptions/ashinde21.json'
r = requests.get(url, auth=(username, password))  
page = r.content
print(page)
j = json.loads(page)
print(j[0]['title'])