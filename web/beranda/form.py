from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, FloatField, SubmitField, RadioField, SelectField)
from wtforms.validators import (DataRequired, Email)




class FormDubois(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur', validators=[DataRequired(message='data harus diisi')])
    bb = IntegerField('Berat Badan', validators=[DataRequired(message='data harus diisi')])
    tb = IntegerField('Tinggi Badan', validators=[DataRequired(message='data harus diisi')])
    aktivitas = FloatField('Aktivitas', validators=[DataRequired(message='data harus diisi')])
    waktu_tidur = IntegerField('Waktu Tidur', validators=[DataRequired(message='data harus diisi')])
    gender = SelectField('Gender', choices=['pria', 'wanita'])
    hitung = SubmitField('Hitung', validators=[DataRequired(message='data harus diisi')])
    laporan = SubmitField('Laporan', validators=[DataRequired(message='data harus diisi')])
    

class FormHarrisBenneedict(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur', validators=[DataRequired(message='data harus diisi')])
    bb = FloatField('Berat Badan', validators=[DataRequired(message='data harus diisi')])
    tb = FloatField('Tinggi Badan', validators=[DataRequired(message='data harus diisi')])
    aktivitas = FloatField('Aktivitas', validators=[DataRequired(message='data harus diisi')])
    stress = FloatField('Faktor Stress', validators=[DataRequired(message='data harus diisi')])
    gender = SelectField('Gender', choices=['PRIA', 'WANITA'])
    hitung = SubmitField('Hitung', validators=[DataRequired(message='data harus diisi')])
    laporan = SubmitField('Laporan', validators=[DataRequired(message='data harus diisi')])
    

class FormMifflin(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur', validators=[DataRequired(message='data harus diisi')])
    bb = FloatField('Berat Badan', validators=[DataRequired(message='data harus diisi')])
    tb = FloatField('Tinggi Badan', validators=[DataRequired(message='data harus diisi')])
    aktivitas = FloatField('Aktivitas', validators=[DataRequired(message='data harus diisi')])
    stress = FloatField('Faktor Stress', validators=[DataRequired(message='data harus diisi')])
    gender = SelectField('Gender', choices=['PRIA', 'WANITA'])
    hitung = SubmitField('Hitung', validators=[DataRequired(message='data harus diisi')])
    laporan = SubmitField('Laporan', validators=[DataRequired(message='data harus diisi')])
    
    