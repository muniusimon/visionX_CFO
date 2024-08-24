from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from flaskblog.models import User

class RegistrationForm (FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max = 20)])
    email = StringField ('email', validators=[DataRequired(), Email()])
    password  = PasswordField('Password', validators=[DataRequired()])
    confirm_password  = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError ('That username is taken, please choose another username')
        
    def validate_email(self, email):
        email = User.query.filter_by(email = email.data).first()
        if email:
            raise ValidationError ('That email is taken, please choose another email')

class LoginForm (FlaskForm):
    email = StringField ('email', validators=[DataRequired(), Email()])
    password  = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class UpdateAccountForm (FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max = 20)])
    email = StringField ('email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError ('That username is taken, please choose another username')
        
    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email = email.data).first()
            if email:
                raise ValidationError ('That email is taken, please choose another email')
