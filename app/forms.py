from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
class UploadForm (FlaskForm):
    description = TextAreaField(validators=[DataRequired()])
    photo = FileField(validators=[DataRequired()])