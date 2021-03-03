from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo


class UserInfoForm(FlaskForm):
    first_name = StringField('First_name', validators=[DataRequired()])
    last_name = StringField('Last_name', validators=[DataRequired()])
    phone_number = StringField('Phone_number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField()