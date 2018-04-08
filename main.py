#trigger errors:
#username or password or confirmation blank
#username or password <3 OR >20 OR contains space character
#password and confirmation don't match
#email not valid (needs a single @, a single ., no spaces, 3<=length<=20)

#errors are next to field where error occurs

#preserve email and username after submissions

#if all valid, bring to welcome page which greets by username

#use template for index/home and welcome pages

from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def signup():
    #pull all user entries from post data, escape, and assign to variables
    #if problems, create errors and re-render template.
    if False:
        username = username_error = password_error = confirmation_error = email = email_error = ''
        return render_template('index.html',
            username = username,
            username_error = username_error,
            password_error = password_error,
            confirmation_error = confirmation_error,
            email = email,
            email_error = email_error)
    #else redirect to welcome
    #help from https://stackoverflow.com/questions/15473626/make-a-post-request-while-redirecting-in-flask
    else:
        return redirect('/welcome', code=307)

@app.route('/welcome', methods=['POST'])
def create_account():
    username = cgi.escape(request.form['username'])
    return render_template('welcome.html', username = username)

app.run()