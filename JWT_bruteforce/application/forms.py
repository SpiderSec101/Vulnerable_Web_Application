from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User

class RegistrationForm(FlaskForm):

	username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Register')

	def validate_username(self, username):
	    user = User.query.filter_by(username=username.data).first()
	    if user:
	        raise ValidationError('This username alredy exists :(')



class LoginForm(FlaskForm):

	username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember_Me')
	submit = SubmitField('Login')


	
	