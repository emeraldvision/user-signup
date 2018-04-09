#BONUS: use base template for index and home
#BONUS: use regex https://docs.python.org/3/library/re.html

from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def signup():
    #pull all user entries from post data and assign to variables
    username = username_error = password_error = confirmation_error = email = email_error = ''
    username = request.form['username']
    password = request.form['password']
    confirmation = request.form['confirmation']
    email = request.form['email']

    u_has_error = p_has_error = c_has_error = e_has_error = False
    #check username for: blank, <3 char, >20 char, contains space
    if username:
        if username.count(' ') != 0:
            u_has_error = True
        elif not 3 <= len(username) <= 20:
            u_has_error = True
    else:
        u_has_error = True
    if u_has_error:
        username_error = 'The username must contain 3-20 characters with no spaces'
    #check password for: blank, <3 char, >20 char, contains space
    if password:
        if password.count(' ') != 0:
            p_has_error = True
        elif not 3 <= len(password) <= 20:
            p_has_error = True
    else:
        p_has_error = True
    if p_has_error:
        password_error = 'The password must contain 3-20 characters with no spaces'
    #check confirmation for: blank, doesn't match password
    if confirmation:
        if password != confirmation:
            c_has_error = True
    else:
        c_has_error = True
    if c_has_error:
        confirmation_error = 'The passwords do not match'
    #if email, check for '@' != 1, '.' != 1, contains space, <3 char, >20 char
    if email:
        if email.count('@') != 1:
            e_has_error = True
        elif email.count('.') != 1:
            e_has_error = True
        elif email.count(' ') != 0:
            e_has_error = True
        elif not 3 <= len(email) <= 20:
            e_has_error = True
    if e_has_error:
        email_error = 'The email is invalid'
    #escape all user-created varibles
    username = cgi.escape(username)
    email = cgi.escape(email)
    #if problems, re-render template with errors.
    if u_has_error or p_has_error or c_has_error or e_has_error:
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