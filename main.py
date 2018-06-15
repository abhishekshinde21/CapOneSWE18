from flask import Flask, render_template, request
from access import top, search, podcasts_by_genre
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
	return render_template('home.html', top=top_list)

@app.route('/data-visuals')
def data_visuals():
	return render_template('data-visuals.html')

@app.route('/data_visuals_search', methods = ['POST'])
def data_visuals_search():
	user_input = request.form['search']
	search_list = search(user_input)
	return render_template('data-visuals-search.html', search=search_list)

@app.route('/smart-search')
def smart_search():
	return render_template('smart-search.html', top=top_list)

@app.route('/smart-visual_search', methods = ['POST'])
def smart_visual_search():
	user_input = request.form['search']
	p_g = podcasts_by_genre(user_input)
	return render_template('smart-visual-search.html', search=p_g, genre=user_input, top=top_list)


if __name__ == "__main__":
	app.run(debug=True) # run this app
