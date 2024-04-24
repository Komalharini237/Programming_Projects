# import new function "flash"
from flask import Flask, render_template, request,redirect, url_for,flash
app = Flask(__name__)
app.secret_key = 'Hash123'

@app.route('/')
def msgflash():
    template = render_template('P10b-MsgFlashing.html')
    return(template)

@app.route('/login', methods=['POST','GET'])
def login():
    error=None
    if request.method=='POST':
        if request.form['username'].lower()!='admin' or request.form['password']!='admin008':
            error = "Invalid username or password. Try again!"
        else:
            flash("Successfully logged in!")
            flash("Log out before logging in again!")
            return(redirect(url_for('msgflash')))
    # else:
    redirected_to=render_template('P10a-Login-Error.html', error=error)
    return(redirected_to)
    
    
if __name__ == '__main__':
    app.run(debug = True)