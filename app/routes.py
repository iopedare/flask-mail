from flask import render_template, request, url_for, flash
from flask_mail import Message
from werkzeug.utils import redirect
from app import app, mail
from app.forms import ContactForm, LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dayo'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)



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
    return render_template('contact.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)