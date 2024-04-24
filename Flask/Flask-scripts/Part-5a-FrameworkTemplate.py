from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    str="""
<html>
<body>
<h1>Hello world</h1>
</body></html>"""
    return(str)

if __name__ == '__main__':
    app.run(debug = True)