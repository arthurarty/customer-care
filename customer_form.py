from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class CustomerForm(FlaskForm):
    """Customer form"""

    customer_name = StringField('Customer Name', validators=[DataRequired()])
    product = StringField('Product you interested in', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
