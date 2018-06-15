from xml.dom import minidom
from urllib.request import urlopen

url_str = 'https://gpodder.net/subscriptions/ashinde21.opml'
xml_str = urlopen(url_str).read()
xmldoc = minidom.parseString(xml_str)

obs_values = xmldoc.getElementsByTagName('base:OBS_VALUE')
# prints the first base:OBS_VALUE it finds
print(obs_values[0].firstChild.nodeValue)

# prints the second base:OBS_VALUE it finds
print(obs_values[1].firstChild.nodeValue)

# prints all base:OBS_VALUE in the XML document
for obs_val in obs_values:
    print(obs_val.firstChild.nodeValue)