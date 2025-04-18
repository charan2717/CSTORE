from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired

class AppUploadForm(FlaskForm):
    name = StringField('App Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = FileField('App Icon/Image')
    file = FileField('App File (ZIP or APK)')
    submit = SubmitField('Upload')
