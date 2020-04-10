from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email


class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    gender = SelectField('Gender', choices = [('Male','male'),('Female','female')])
    email = StringField('Email',validators = [DataRequired()],Email())
    location = StringField('Location', validators = [DataRequired()])
    biography = TextAreaField('Biography', validators = [DataRequired()])
    profile_pic = FileField('Profile Picture', validators = [FileRequired(), FileAllowed(['jpg','jpeg','png'], 'Only images please.')])
    submit = SubmitField("Add Profile")
