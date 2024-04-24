from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'xxxx xxxx xxxx xxxx' # 'your-app-password'

# How to get app password-
# Refer to "Get-App-password.txt"

mail=Mail(app)

@app.route('/')
def index():
    msg= Message('Hello Amigo!', sender='your-email@gmail.com',recipients=['recipient-email@gmail.com'])
    msg.body = "This the first message sent from Flask-Mail"
    mail.send(msg)
    return("Message sent successfully")

    
if __name__ == '__main__':
    app.run(debug = True)