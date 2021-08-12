from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Userame is already Exist! Please try with different name')
    
    def validate_email_address(self,email_address_to_check):
        email=User.query.filter_by(email_address=email_address_to_check.data).first()
        if email:
            raise ValidationError('Email address is already Exist! Please try with different email address')

    username = StringField(label='User Name:', validators=[
                           Length(min=2, max=30),DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(),DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Passowrd:', validators=[
                              EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Create Account:')



class LoginForm(FlaskForm):

    username = StringField(label='User Name:', validators=[
                           Length(min=2, max=30),DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=6),DataRequired()])
    
    submit = SubmitField(label='Login')

class PurchaseForm(FlaskForm):
    submit = SubmitField(label='Purchase Item')

class SellingForm(FlaskForm):
    submit = SubmitField(label='Selling Item')