from flask import render_template, request, url_for, flash, redirect
from werkzeug.urls import url_parse
from flask_mail import Message
from flask_login import current_user, login_user, logout_user, login_required
from app import app, mail
from app.forms import ContactForm, LoginForm
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data

        msg = Message(subject, sender="djetlii@live.com", body=f"Name: {name}\nEmail: {email}\n\nMessage: \n{message}", recipients=["djetlii@live.com"])
        # message.body = msg
        mail.send(msg)
        success = "Thanks for the message. We'll get back to you shortly."
        return render_template("thankyou.html", success=success)
    return render_template('contact.html',title="Contact Us", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))