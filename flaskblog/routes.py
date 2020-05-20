from flask import render_template, url_for, redirect, flash
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required


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
    	hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    	user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created', 'success')
        return redirect(url_for('login'))
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
