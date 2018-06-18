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

lo = locator.Locator('ashinde21')
print(lo.episode_data_uri('http://www.bbc.co.uk/programmes/p01plr2p', 'http://open.live.bbc.co.uk/mediaselector/5/redir/version/2.0/mediaset/audio-nondrm-download-low/proto/http/vpid/p06b64mv.mp3'))
print(lo.podcast_data_uri('http://downloads.bbc.co.uk/podcasts/worldservice/tech/rss.xml'))

client = public.PublicClient()
print(client.get_episode_data('http://www.bbc.co.uk/programmes/p01plr2p', 'http://open.live.bbc.co.uk/mediaselector/5/redir/version/2.0/mediaset/audio-nondrm-download-low/proto/http/vpid/p06b64mv.mp3'))