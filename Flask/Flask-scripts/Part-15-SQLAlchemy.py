from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Offices.sqlite3'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)



class officesdb(db.Model):
    id = db.Column('office_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    add = db.Column(db.String(1000))
    city = db.Column(db.String(50))
    state = db.Column(db.String(20))

    def __init__(self, name, add, city, state):
        self.name = name
        self.add = add
        self.city = city
        self.state = state

# Create tables based on the model definitions within the application context
with app.app_context():
    db.create_all()

@app.route('/')
def show_all():
    data=officesdb.query.all()
    template = render_template("P15a-show_all.html", officesdb=data)
    return(template)

@app.route('/add_record',methods=["GET", "POST"])
def add_record():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['add']:
            flash("Please enter all the fields", "error")
        else:
            office_data = officesdb(request.form['name'],
                                    request.form['add'],
                                    request.form['city'],
                                    request.form['state'])
            db.session.add(office_data)
            db.session.commit()
            flash("Record successfully added!")
            run = redirect(url_for('show_all'))
            return(run)
    template = render_template("P15b-newrecord.html")
    return(template)
        
if __name__ == '__main__':
    app.run(debug = True)
