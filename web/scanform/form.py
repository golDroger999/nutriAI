from flask_wtf import FlaskForm
from wtforms import (FileField, SubmitField)
from flask_wtf.file import FileRequired



class document(FlaskForm):
    document = FileField('Silahkan Upload File foto Berformat jpg, jpeg', validators=[FileRequired()])
    analisa = SubmitField('Analisa')