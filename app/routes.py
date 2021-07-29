from flask import render_template, request, url_for
from flask_mail import Message
from app import app, mail

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

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        msg = Message(subject, sender="djetlii@live.com", body=f"Email: {email}\n\nMessage: \n{message}", recipients=["djetlii@live.com"])
        # message.body = msg
        mail.send(msg)
        success = "Message Sent"
        return render_template("contact.html", success=success)
    return render_template("contact.html" )
