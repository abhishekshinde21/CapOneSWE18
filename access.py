from mygpoclient import public, testing, locator
import requests
from urllib.request import urlopen
import xmltodict
import xml.etree.ElementTree as ET

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
	# for podcast in search_list:
	# 	print(podcast.title, ":", podcast.description)

def top(client):
	return client.get_toplist()
	# toplist = client.get_toplist()
	# for index, entry in enumerate(toplist):
	#     print(index+1, entry.title, entry.subscribers)

# generates XML file, so have to parse it to retrieve data
def get_user_subscriptions(username):
	l = locator.Locator(username)
	uri = l.subscriptions_uri()
	parseXML(uri)

# parses the xml website and retrieves the data on the user's podcasts 
def parseXML(xmlfile):
	response = requests.get(xmlfile)
	tree = ET.fromstring(response.content)
	root = tree.getroot()
	dump(tree)
	# print()
	# file = urlopen(xmlfile)
	# data = parse(file)  
	# dump(data)
	# data = file.read()
 #    # file.close()

	# data = xmltodict.parse(data)
	# print(data)
def toptags():
	tags = client.get_toptags()
	for tag in tags:
		print(tag)
	# response = requests.get(xmlfile)
	# tree = ET.fromstring(response.content)
	# # root = tree.getroot()
	# # print(root[0][0].text)
	# podcastitems = []
	
def podcasts_by_genre(query):
	client = public.PublicClient()
	genre_list = client.get_podcasts_of_a_tag(query)
	return genre_list

# l = locator.Locator(None)
# print(l.episode_data_uri('Tech Tent','Nowhere To Hide'))
# toptags()
# get_user_subscriptions('ashinde21')
# search(client, "sports")


