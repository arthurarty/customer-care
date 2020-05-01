import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_mail import Mail, Message

load_dotenv()

app = Flask(__name__)
app.config['MAIL_SERVER']= os.getenv('EMAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('EMAIL_PORT')
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods = ['POST'])
def handle_form():
    name = request.form['customer_name']
    phone_number = request.form['phone_number']
    product = request.form['product']
    email = request.form['email']
    body = f"Hello, {name} just ordered {product} reach him on {phone_number} or at {email}"
    msg = Message("New order placed", sender="arthur.nangai@gmail.com", recipients=["martinkatamba@gmail.com"])
    msg.body = body
    mail.send(msg)
    return body

if __name__ == '__main__':
    app.run(debug=True)
