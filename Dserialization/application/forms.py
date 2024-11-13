from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import string 

banned_characters = list(string.punctuation)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=10)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_username(self, username):
        if (username.data).lower() == 'admin' or (username.data).lower() == 'administrator':
            raise ValidationError('You are not Admin, Permission Denied :(')
        
        # Use spaces for consistent indentation
        for i in banned_characters:
            if i in (username.data) or i in (self.password.data):
                raise ValidationError('Well tried ;)')
