from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def home():
    return(upload())

@app.route('/upload')
def upload():
    template = render_template('P11-Upload.html')
    return(template)

@app.route('/uploader', methods=['POST','GET'])
def uploader():
    if request.method=='POST':
        f=request.files['file']
        logging.debug("file requested and obtained")
        f.save(secure_filename(f.filename))
        return("File uploaded successfully!")
    
    
if __name__ == '__main__':
    app.run(debug = True)