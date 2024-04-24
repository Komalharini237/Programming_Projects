# import new function "make_response"
from flask import Flask, render_template, request, make_response
app = Flask(__name__)


@app.route('/')
def index():
    template = render_template('P8a-setcookie.html')
    return(template)

@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
    if request.method=='POST':
        user = request.form['nm']
        response = make_response(render_template("P8b-readcookie.html"))
        response.set_cookie('userID', user)
    # else:
    #     user=request.args.get('nm')
        return(response)
    
    
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    message = '<body bgcolor="Pink"><h1><font size="50" face="Algerian" color="Purple">Welcome '+name+'</font></h1></body>'
    
    return(message)

if __name__ == '__main__':
    app.run(debug = True)