# Abhishek Shinde
# The dependencies used for this project and for the functions listed below
from mygpoclient import public, testing, locator
import requests
import json
import pprint

client = public.PublicClient()

# ** Functions **

# searches for podcasts based on user input into search bar, and returns a list object
def search(query):
	client = public.PublicClient()
	search_list = client.search_podcasts(query)
	return search_list

# provided a client object, function returns a list of top podcasts (live data)
def top(client):
	return client.get_toplist()

# returns a list of top tags from the website (live data)
def toptags():
	client = public.PublicClient()
	tags = client.get_toptags()
	return tags

# returns a list of podcasts specific to the genre input
def podcasts_by_genre(query):
	client = public.PublicClient()
	genre_list = client.get_podcasts_of_a_tag(query)
	return genre_list

# returns a json object of the user's subscriptions (need to supply username and password)
def subscription(username, password):
	l = locator.Locator(username)
	url = l.subscriptions_uri(format='json')
	r = requests.get(url, auth=(username, password))
	page = r.content
	jsn = json.loads(page)
	return jsn

# helper function that sorts based on specified key
def sort_by_subscribers(d):
    return d['subscribers']

# returns a sorted list based on the number of subscribers for each podcast
def sort_subscriptions(username, password):
	l = locator.Locator(username)
	url = l.subscriptions_uri(format='json')
	r = requests.get(url, auth=(username, password))
	page = r.content
	jsn = json.loads(page)
	return sorted(jsn, key=sort_by_subscribers)



