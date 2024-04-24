from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, validators, ValidationError

class ContactForm(FlaskForm):
    name = StringField("Name",[validators.DataRequired("Please enter your full-name.")])
    Gender = RadioField("Gender",choices=[("M", "Male"),("F", "Female"),("O", "Other")])
    Address = TextAreaField("Address")
    email = StringField("Email",[validators.DataRequired("Please enter your email id."), validators.Email("Please enter your email-id.")])
    Age = IntegerField("Age")
    language = SelectField("Languages", choices=[("ENG", "English"),("HN", "Hindi"),("MR", "Marathi"),("GJ", "Gujarati"),("PN", "Panjabi"),("FR", "French")])
    submit = SubmitField("Register!")
