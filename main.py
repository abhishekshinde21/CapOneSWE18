# Abhishek Shinde
# Dependencies
from flask import Flask, render_template, request
from access import top, search, podcasts_by_genre, toptags, subscription, sort_subscriptions
from mygpoclient import public

# main application: root path
app = Flask(__name__)

# Gets a client for the gpodder.net “anonymous” API (no authentication required)
client = public.PublicClient()
top_list = top(client)

# @ signifies a decorator - way to wrap a function and modifying its behavior (route corresponds to the return of the function)
# routing, this is the root directory
@app.route('/')
def index():
	tag_list = toptags()
	return render_template('home.html', tags=tag_list)

# renders the data visuals page
@app.route('/data-visuals')
def data_visuals():
	return render_template('data-visuals.html')

# renders the searched data visuals page
@app.route('/data_visuals_search', methods = ['POST'])
def data_visuals_search():
	user_input = request.form['search']
	search_list = search(user_input)
	return render_template('data-visuals-search.html', search=search_list)

# renders the smart search page
@app.route('/smart-search')
def smart_search():
	return render_template('smart-search.html', top=top_list)

# renders the requested smart search page
@app.route('/smart_visual_search', methods = ['POST'])
def smart_visual_search():
	user_input = request.form['search']
	p_g = podcasts_by_genre(user_input)
	return render_template('smart-visual-search.html', search=p_g, genre=user_input, top=top_list)

# renders the subscriptions page
@app.route('/subscriptions', methods = ['POST'])
def subscriptions():
	user = request.form['username']
	pw = request.form['password']
	try:
		j = subscription(user, pw)
		return render_template('subscriptions.html', json=j)
	except Exception as e:
		print(e)

# renders the smart sort page
@app.route('/smart-sort')
def smart_sort():
	return render_template('smart-sort.html')

# renders the sorted-podcasts page
@app.route('/smart_sort_search', methods = ['POST'])
def smart_sort_search():
	user = request.form['username']
	pw = request.form['password']
	try:
		j = sort_subscriptions(user, pw)
		return render_template('smart-sort-search.html', json=j)
	except Exception as e:
		print(e)
	
# runs the app from this file 
if __name__ == "__main__":
	app.run(debug=True) # run this app
