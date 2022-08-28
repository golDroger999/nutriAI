from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, FloatField, SubmitField, RadioField, SelectField, DecimalField)
from wtforms.validators import (DataRequired, Email)



# FORM DUBOIS
class FormDubois(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur', validators=[DataRequired(message='data harus diisi')])
    bb = IntegerField('Berat Badan (kg)', validators=[DataRequired(message='data harus diisi')])
    tb = IntegerField('Tinggi Badan (cm)', validators=[DataRequired(message='data harus diisi')])
    aktivitas = FloatField('Aktivitas', validators=[DataRequired(message='data harus diisi')])
    tidur = IntegerField('Waktu Tidur', validators=[DataRequired(message='data harus diisi')])
    gender = SelectField('Gender', choices=['pria', 'wanita'])
    hitung = SubmitField('Hitung')
    laporan = SubmitField('Laporan')
    save = SubmitField('Save Data')
# AKHIR FORM DUBOIS

# FORM HARRIS BENEDICT
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
# AKHIR FORM HARRIS BENEDICT

# FORM MIFFLIN
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
# AKHIR FORM MIFFLIN
    
# FORM PERKENI
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
# AKHIR FORM PERKENI    

# FORM IBU HAMIL    
class FormHamil(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur', validators=[DataRequired(message='data harus diisi')])
    bb = IntegerField('Berat Badan (kg)', validators=[DataRequired(message='data harus diisi')])
    tb = IntegerField('Tinggi Badan (cm)', validators=[DataRequired(message='data harus diisi')])
    aktivitas = IntegerField('Aktivitas', validators=[DataRequired(message='data harus diisi')])
    tidur = IntegerField('Waktu Tidur', validators=[DataRequired(message='data harus diisi')])
    umurhamil = IntegerField('Umur Kehamilan(minggu)',validators=[DataRequired(message='data harus diisi')] )
    trimester = SelectField('Trimester', choices=['Trimester 1', 'Trimester 2','Trimester 3'])
    hitung = SubmitField('Hitung')
    laporan = SubmitField('Laporan')
    save = SubmitField('Save Data')
# AKHIR FORM IBU HAMIL
    
# FORM IBU MENYUSUI 
class FormMenyusui(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur', validators=[DataRequired(message='data harus diisi')])
    bb = IntegerField('Berat Badan (kg)', validators=[DataRequired(message='data harus diisi')])
    tb = IntegerField('Tinggi Badan (cm)', validators=[DataRequired(message='data harus diisi')])
    aktivitas = IntegerField('Aktivitas', validators=[DataRequired(message='data harus diisi')])
    tidur = IntegerField('Waktu Tidur', validators=[DataRequired(message='data harus diisi')])
    siklus = SelectField('Siklus Menyusui', choices=['6 bulan pertama', '6 bulan kedua'])
    hitung = SubmitField('Hitung')
    laporan = SubmitField('Laporan')
    save = SubmitField('Save Data')
# AKHIR FORM IBU MENYUSUI

# FORM GIZI PENYAKIT GINJAL
class FormGinjal(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur', validators=[DataRequired(message='data harus diisi')])
    bb = IntegerField('Berat Badan (kg)', validators=[DataRequired(message='data harus diisi')])
    tb = IntegerField('Tinggi Badan (cm)', validators=[DataRequired(message='data harus diisi')])
    aktivitas = IntegerField('Aktivitas', validators=[DataRequired(message='data harus diisi')])
    stress = IntegerField('Faktor Stress', validators=[DataRequired(message='data harus diisi')])
    siklus = SelectField('siklus', choices=['6 BULAN PERTAMA', '6 BULAN KEDUA'])
    gender = SelectField('Gender', choices=['pria', 'wanita'])
    hitung = SubmitField('Hitung')
    laporan = SubmitField('Laporan')
    save = SubmitField('Save Data')
#  AKHIR FORM GIZI PENYAKIT GINJAL