from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, FloatField, SubmitField, RadioField, SelectField, DecimalField)
from wtforms.validators import (DataRequired, Email)
from flask import (request, render_template)

class pagtform(FlaskForm):
    
    # DATA DIRI DAN ANTROPOMETRI
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur (dalam tahun, min 10)', validators=[DataRequired(message='data harus diisi')])
    bb = IntegerField('Berat Badan (dalam kg)', validators=[DataRequired(message='data harus diisi')])
    tb = IntegerField('Tinggi Badan (dalam cm)', validators=[DataRequired(message='data harus diisi')])
    aktivitas = IntegerField('Aktivitas', validators=[DataRequired(message='data harus diisi')])
    stress = IntegerField('Faktor Stress', validators=[DataRequired(message='data harus diisi')])
    penyakit = StringField('Diagnosa Penyakit', validators=[DataRequired(message='data harus diisi')])
    gender = SelectField('Gender', choices=['pria', 'wanita'])
    
    # DATA BIOKIMIA
    hb = IntegerField('Kadar Hb')
    ldl = IntegerField('Kadar Ldl')
    hdl = IntegerField('Kadar Hdl')
    kolesterol = IntegerField('Kadar kolestero')
    
    # DATA FISIK KLINIS
    tekanan_darah = IntegerField('Tekanan Darah')
    suhu = IntegerField('Suhu Tubuh')
    
    
    analisa = SubmitField('Analisa')
    hasil_pdf = SubmitField('Print Hasil Pdf')
    pdf_form = SubmitField('Print Form')
