from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired,Email

class RegisterForm (FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    email = StringField('E~mail', validators = [DataRequired(), Email()])
    password= PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Register')

class SigninForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators= [DataRequired()])
    submit = SubmitField('Sign in')