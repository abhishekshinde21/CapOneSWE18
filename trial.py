from mygpoclient import public, testing, locator, api, simple
import requests
import json


l = locator.Locator('ashinde21')

username = 'ashinde21'
password = 'Marco21reus'
url = l.subscriptions_uri(format='json')
r = requests.get(url, auth=(username, password))  
page = r.content
# print(page)
j = json.loads(page)
for sub in j:
	print(sub)