
from flask import Flask, render_template, request, flash, redirect, url_for
# since we have hyphens in our script name we can use the below module_name function
# refer to module_name_correction document for the detailed explanation
import importlib.util

def module_name(name):
    # Load the module from the script file
    # Create a specification object that describes where to find and how to load the module.
    spec = importlib.util.spec_from_file_location(name.replace('-','_'), name)

    # Create an empty module object based on the provided specification.
    module = importlib.util.module_from_spec(spec)

    # Load and execute the module's code using the provided specification.
    spec.loader.exec_module(module)
    return(module)

module = module_name("Part-13a-WTFExtension.py")
# Now you can directly access the ContactForm class
ContactForm = module.ContactForm

app = Flask(__name__)
app.secret_key = 'Hash123'

@app.route('/')
def index():
    return(redirect(url_for('contact')))

@app.route('/contact',methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            template = render_template('P13a-contact.html', form = form)
        else:
            template = render_template('P13b-success.html')
    elif request.method == 'GET':
        template = render_template('P13a-contact.html', form = form)
    return(template)

if __name__ == '__main__':
    app.run(debug = True)
