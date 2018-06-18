# CapOneSWE18

This application utilized the gpodder.net client in Python
Development was in Python, Flask, HTML, and CSS, including dependencies of Flask, gunicorn, requests, mygpoclient

GET Requests were made to retrieve data from the gpodder.net API to get the top lists, podcasts of a specific genre, user's subscriptions, and many more.
POST Requests were made to retrieve user login information or queries

Tasks::
```
Data Visuals: Display the podcasts returned via search function, as well as key information about each podcast returned. Similarly, display the podcasts a user is subscribed to, as well as information that user might want to know at a glance about the subscriptions.
```
For this, a search bar is included that enables the user to search for any podcast, and get information on it. In addition, the title has a link to its website.
The user also has the option to enter their login information, so that he/she can get information on their subscriptions.
```
Smart Searching: Give users the ability to search for podcasts by genre and by popularity.
This tab consists of two parts: popularity and genres.
On the left side, a GET request was made to get the top list of podcasts and present the information to the user.
On the right side, there is a form for the user, which makes a HTTP POST request, and return the top podcasts for that specific genre.
```
Smart Sorting: Based on how frequently each subscribed podcast has new episodes, which subscribed podcasts should the user listen to first in order to avoid falling behind? Assume the user is subscribed to the top 25 podcasts.
Many attempts were made to retrieve episode information, however could not achieve getting media urls, even after parsing XML sites for the podcasts.
Best alternative for time permitting was to query the podcasts for the number of subscribers, because I am assuming that the user frequently watches the most subscribed podcasts, and the user most likely forgets the subscribed unpopular podcasts.
For this reason, the podcasts are sorted by subscribers with the sort function, and the results are returned to the user.
```
