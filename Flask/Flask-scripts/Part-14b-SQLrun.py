from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def homepage():
    template = render_template("P14a-homepage.html")
    return(template)

@app.route('/enternew')
def new_record():
    template = render_template("P14b-record.html")
    return(template)

@app.route('/add_record',methods=["GET", "POST"])
def add_record():
    if request.method == 'POST':
        try:
            office_id = request.form['office_id']
            address = request.form['address']
            city = request.form['city']
            state = request.form['state']
            with sql.connect("sql_hr.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO offices (office_id,address,city,state) VALUES (?,?,?,?)", (office_id,address,city,state))
                con.commit()
                message = "Record registered successfully!"
        except:
            con.rollback()
            message="Error occurred!"
        finally:
            template = render_template("P14c-result.html", message=message)
            return(template)
            con.close()

@app.route('/list')
def list():
    con=sql.connect("sql_hr.db")
    con.row_factory=sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM offices")
    rows=cur.fetchall()
    template = render_template("P14d-list.html", rows=rows)
    return(template)
        
if __name__ == '__main__':
    app.run(debug = True)
