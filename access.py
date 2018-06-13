from mygpoclient import public
from mygpoclient import testing
from mygpoclient import locator

# client = simple.SimpleClient('ashinde21', 'Marco21reus')
# subscriptions = client.get_subscriptions('123')
# for url in subscriptions:
#     print('Subscribed to:' + url)

# Functions
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

def get_user_subscriptions(username):
	l = locator.Locator(username)
	uri = l.subscriptions_uri()
	print(uri)

get_user_subscriptions('ashinde21')
# search(client, "sports")


