from flask import Flask, render_template
app = Flask(__name__)

post = [
	{
		'author': 'Aadesh Mirajkar',
		'title': 'Nerdy Brat',
		'content': 'trial',
		'date_posted': 'May 16, 2020'
	},
	{
		'author': 'Aman Roy',
		'title': 'chomu',
		'content': 'trial',
		'date_posted': 'May 17, 2020'
	},
	{
		'author': 'Kuldeep',
		'title': 'flutter dev',
		'content': 'trial',
		'date_posted': 'May 18, 2020'
	}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=post)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)