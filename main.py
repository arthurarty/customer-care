import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from customer_form import CustomerForm


load_dotenv()

app = Flask(__name__)
app.config['MAIL_SERVER']= os.getenv('EMAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('EMAIL_PORT')
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.secret_key = os.getenv('SECRET_KEY')
mail = Mail(app)

@app.route('/')
def index():
    return render_template('form.html', form=CustomerForm())

@app.route('/submit', methods = ['POST'])
def handle_form():
    form = CustomerForm()
    if form.validate_on_submit():
        body = f"Hello, {form.customer_name.data} ordered {form.product.data} no: {form.phone_number.data} email: {form.email.data}"
        msg = Message("New order placed", sender="arthur.nangai@gmail.com", recipients=["art@gmail.com"])
        msg.body = body
        mail.send(msg)
        return "Email sent"
    return "there has been an eror"

if __name__ == '__main__':
    app.run(debug=True)
