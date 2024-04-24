# Import "render_template" function
from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def index():
    template=render_template('P5-Template.html')
    return(template)

if __name__ == '__main__':
    app.run(debug = True)