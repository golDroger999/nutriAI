from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, FloatField, SubmitField, SelectField)
from wtforms.validators import (DataRequired, Email)
from flask import (request, render_template)

class pagtform(FlaskForm):
    
    # DATA DIRI DAN ANTROPOMETRI
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur (dalam tahun, min 10)', validators=[DataRequired(message='data harus diisi')])
    pekerjaan = StringField('Pekerjaan (Boleh Dikosongkan)')
    bb = IntegerField('Berat Badan (dalam kg)', validators=[DataRequired(message='data harus diisi')])
    tb = IntegerField('Tinggi Badan (dalam cm)', validators=[DataRequired(message='data harus diisi')])
    aktivitas = IntegerField('Aktivitas', validators=[DataRequired(message='data harus diisi')])
    stress = IntegerField('Faktor Stress', validators=[DataRequired(message='data harus diisi')])
    
    penyakit = SelectField('Diagnosa Penyakit', choices=['tifoid', 'hemoroid', 'diare', 'gastritis', 'hipertensi', 
                                                         'jantung koroner', 'autis', 'batu ginjal', 'sindrom nefrotik', 
                                                         'gagal ginjal akut', 'batu empedu', 'sirosis hepatik', 'pasca bedah', 
                                                         'diabetes melitus', 'diabetes melitus tipe 2', 'hiv/aids', 'alergi' ])
    
    gender = SelectField('Gender', choices=['pria', 'wanita'])
    # AKHIR DIRI DAN ANTROPOMETRI
    
    
    
    
    # DATA BIOKIMIA
    hb = IntegerField('Kadar Hb')
    ldl = IntegerField('Kadar Ldl')
    hdl = IntegerField('Kadar Hdl')
    kolesterol = IntegerField('Kadar Kolesterol Total')
    sgot = IntegerField('Kadar Sgot')
    sgpt = IntegerField('Kadar Sgpt')
    bun = IntegerField('kadar bun')
    bilirubin_direk = IntegerField('Kadar Bilirubin Direk')
    bilirubin_total = IntegerField('Kadar Bilirubin Total')
    trigliserida = IntegerField('Kadar Trigliserida')
    glukosa = IntegerField('Kadar Glukosa')
    gula_puasa = IntegerField('Kadar Gula Puasa')
    gula_sewaktu = IntegerField('Kadar Gula Sewaktu')
    asam_urat = IntegerField('Kadar Asam Urat')
    # AKHIR DATA BIOKIMIA
    
    
    
    
    # DATA FISIK KLINIS
    tekanan_darah = IntegerField('Tekanan Darah')
    suhu = IntegerField('Suhu Tubuh')
    nadi = IntegerField('Denyut Nadi')
    masalah_oral = SelectField('Permasalahan Terkait oral', choices=['Susah Mengunyah', 
                                                                     'Susah Menelan',
                                                                     'Tidak Bisa menelan',
                                                                     'Normal/tidak ada masalah'])
    # AKHIR DATA FISIK KLINIS
    
    
    # DATA RIWAYAT MAKAN / ASUPAN
    energi = IntegerField('Riwayat Energi (kkal) ')
    protein = IntegerField('Riwayat Protein (gr)')
    lemak = IntegerField('Jumlah Riwayat Lemak (gr)')
    karbo = IntegerField('Riwayat Karbohidrat (gr)')
    # AKHIR DATA RIWAYAT MAKAN / ASUPAN
     
    
    analisa = SubmitField('Analisa')
    hasil_pdf = SubmitField('Print Hasil Pdf')
    pdf_form = SubmitField('Print Form')
