from flask_wtf import FlaskForm
from wtforms import (FileField, SubmitField)
from flask_wtf.file import FileRequired


class csv_form(FlaskForm):
    csv = FileField('Silahkan Upload File Berformat CSV', validators=[FileRequired()])
    analisa = SubmitField('Analisa')