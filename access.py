from mygpoclient import public, testing, locator
import requests
import json
# client = simple.SimpleClient('ashinde21', 'Marco21reus')
# subscriptions = client.get_subscriptions('123')
# for url in subscriptions:
#     print('Subscribed to:' + url)
client = public.PublicClient()
# ** Functions **

def search(query):
	client = public.PublicClient()
	search_list = client.search_podcasts(query)
	return search_list

def top(client):
	return client.get_toplist()

def toptags():
	client = public.PublicClient()
	tags = client.get_toptags()
	return tags
	
def podcasts_by_genre(query):
	client = public.PublicClient()
	genre_list = client.get_podcasts_of_a_tag(query)
	return genre_list

def subscription(username, password):
	l = locator.Locator(username)
	url = l.subscriptions_uri(format='json')
	r = requests.get(url, auth=(username, password))
	page = r.content
	jsn = json.loads(page)
	return jsn

toptags()


