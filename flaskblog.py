from flask import Flask, render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#secret key for protection againt cookies
app.config['SECRET_KEY'] = 'e194fb5513a73312'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) #instance of database


class User(db.Model):  #user class to hold the users 
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(10), unique=True, nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(20), nullable=False)

	def __repr__(self): #this method tells how users object is printed out
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



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
	return render_template('about.html', title = 'About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
	app.run(debug=True)