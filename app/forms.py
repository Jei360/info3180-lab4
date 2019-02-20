from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email

class UploadForm(FlaskForm):
    file= FileField('form', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])