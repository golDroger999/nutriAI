from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, FloatField, SubmitField, RadioField, SelectField, DecimalField)
from wtforms.validators import (DataRequired, Email)




class FormDubois(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur', validators=[DataRequired(message='data harus diisi')])
    bb = IntegerField('Berat Badan (kg)', validators=[DataRequired(message='data harus diisi')])
    tb = IntegerField('Tinggi Badan (cm)', validators=[DataRequired(message='data harus diisi')])
    aktivitas = FloatField('Aktivitas', validators=[DataRequired(message='data harus diisi')])
    waktu_tidur = IntegerField('Waktu Tidur', validators=[DataRequired(message='data harus diisi')])
    gender = SelectField('Gender', choices=['pria', 'wanita'])
    hitung = SubmitField('Hitung')
    laporan = SubmitField('Laporan')
    save = SubmitField('Save Data')

class FormHarrisBenneedict(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur', validators=[DataRequired(message='data harus diisi')])
    bb = IntegerField('Berat Badan (kg)', validators=[DataRequired(message='data harus diisi')])
    tb = IntegerField('Tinggi Badan (cm)', validators=[DataRequired(message='data harus diisi')])
    aktivitas = IntegerField('Aktivitas', validators=[DataRequired(message='data harus diisi')])
    stress = IntegerField('Faktor Stress', validators=[DataRequired(message='data harus diisi')])
    gender = SelectField('Gender', choices=['pria', 'wanita'])
    hitung = SubmitField('Hitung')
    laporan = SubmitField('Laporan')
    save = SubmitField('Save Data')
    

class FormMifflin(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur', validators=[DataRequired(message='data harus diisi')])
    bb = IntegerField('Berat Badan (kg)', validators=[DataRequired(message='data harus diisi')])
    tb = IntegerField('Tinggi Badan (cm)', validators=[DataRequired(message='data harus diisi')])
    aktivitas = FloatField('Aktivitas', validators=[DataRequired(message='data harus diisi')])
    stress = FloatField('Faktor Stress', validators=[DataRequired(message='data harus diisi')])
    gender = SelectField('Gender', choices=['pria', 'wanita'])
    hitung = SubmitField('Hitung')
    laporan = SubmitField('Laporan')
    save = SubmitField('Save Data')
    
    

class FormPerkeni(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur', validators=[DataRequired(message='data harus diisi')])
    bb = IntegerField('Berat Badan (kg)', validators=[DataRequired(message='data harus diisi')])
    tb = IntegerField('Tinggi Badan (cm)', validators=[DataRequired(message='data harus diisi')])
    aktivitas = FloatField('Aktivitas', validators=[DataRequired(message='data harus diisi')])
    gender = SelectField('Gender', choices=['pria', 'wanita'])
    hitung = SubmitField('Hitung')
    laporan = SubmitField('Laporan')
    save = SubmitField('Save Data')