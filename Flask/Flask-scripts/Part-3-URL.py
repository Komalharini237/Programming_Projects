from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
    return("Hello World.")

@app.route('/guest/<guest>')
def hello_guest(guest):
    if guest=="admin":
        redirected_to = redirect(url_for('hello_admin', name=guest))
    elif guest=="guest" or guest=="user":
        redirected_to = ("Hello %s. I didn't catch your name." %guest)
    else:
        redirected_to = ("Hello %s. You are a guest here." % guest)
    return(redirected_to)

@app.route('/<name>')
def hello_admin(name):
    if name=="admin":
        redirected_to = ("Hello Admin. Its nice to meet you.")
    else:# name=="guest" or name=="user":
        redirected_to = redirect(url_for('hello_guest', guest=name))
    # else:
    #     redirected_to = ("Hello World... and %s."%name)
    return(redirected_to)

@app.route('/user/<user>')
def hello_user(user):
    # if user=="admin":
    #     redirected_to = redirect(url_for('hello_admin', name=user))
    # else:
    #     redirected_to = redirect(url_for('hello_guest', guest=user))
    # return(redirected_to)
    redirected_to = redirect(url_for('hello_admin', name=user))
    return(redirected_to)


if __name__ == '__main__':
    app.run(debug = True)