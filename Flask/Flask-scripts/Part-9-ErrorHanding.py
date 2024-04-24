# import new function "abort"
from flask import Flask, render_template, request,redirect, url_for,abort
app = Flask(__name__)


@app.route('/')
def index():
    template = render_template('P9-login.html')
    return(template)

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        if request.form['username'].lower()=='admin':
            redirected_to = redirect(url_for('log_successful'))
        else:
            redirected_to = abort(401)
    else:
        redirected_to = redirect(url_for('index'))
    return(redirected_to)
    
    
@app.route('/success')
def log_successful():
    message = '<body bgcolor="yellow"><h1><font size="50" face="Chiller" color="red">Welcome '+"Successfully logged in!"+'</font></h1></body>'
    return(message)

if __name__ == '__main__':
    app.run(debug = True)