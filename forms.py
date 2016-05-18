from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired


class SignupForm(Form):
    first_name = StringField('First Name',validators=[DataRequired("Please enter First Name")])
    last_name = StringField('Last Name',validators=[DataRequired("Please enter Last Name")])
    email = StringField('Email',validators=[DataRequired("Please enter Email")])
    password = PasswordField('Password',validators=[DataRequired("Please enter Password")])
    submit  =  SubmitField('Sign up')
