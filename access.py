from mygpoclient import public, testing, locator
import requests

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

# toptags()


