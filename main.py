#signup header
#username
#password
#password confirmation
#email (required form, optional submission)

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

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('base.html')

app.run()