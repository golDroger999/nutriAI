from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, FloatField, SubmitField, SelectField, SelectMultipleField, widgets)
from wtforms.validators import (DataRequired, Email)
from flask import (request, render_template)


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

    
class pagtform(FlaskForm):
    
    # DATA DIRI DAN ANTROPOMETRI
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur (dalam tahun, min 10)', validators=[DataRequired(message='data harus diisi')])
    pekerjaan = StringField('Pekerjaan (Boleh Dikosongkan)')
    bb = IntegerField('Berat Badan (dalam kg)', validators=[DataRequired(message='data harus diisi')])
    tb = IntegerField('Tinggi Badan (dalam cm)', validators=[DataRequired(message='data harus diisi')])
    
    aktivitas = SelectField('Aktivitas',
                            choices=[
                                    'bedrest(1.1)', 
                                    'bedrest/bergerak terbatas(1.2)', 
                                    'tidak bedrest/bisa berjalan(1.3)'], 
                                     validators=[DataRequired(message='data harus diisi')
                                    ])
    
    stress = IntegerField('Faktor Stress (Tulis Desimal.)', validators=[DataRequired(message='data harus diisi')])
    
    penyakit = SelectField('Diagnosa Penyakit', 
                           choices=[
                               'tifoid', 'hemoroid', 'diare', 
                               'gastritis', 'hipertensi', 'jantung koroner', 
                               'autis', 'batu ginjal', 'sindrom nefrotik', 
                                'gagal ginjal akut', 'batu empedu', 'sirosis hepatik', 
                                'pasca bedah', 'diabetes melitus', 'diabetes melitus tipe 2',
                                'hiv/aids', 'alergi', 'gout artritis', 'luka bakar'
                                ])
    
    gender = SelectField('Gender', choices=['pria', 'wanita'])
    # AKHIR DIRI DAN ANTROPOMETRI
    
    
    
    
    # DATA BIOKIMIA
    hb = IntegerField('Hb')
    ldl = IntegerField('Ldl')
    hdl = IntegerField('Hdl')
    kolesterol = IntegerField('Kolesterol Total')
    sgot = IntegerField('Sgot')
    sgpt = IntegerField('Sgpt')
    bun = IntegerField('bun')
    bilirubin_direk = IntegerField('Bilirubin Direk')
    bilirubin_indirek = IntegerField('Bilirubin inDirek')
    bilirubin_total = IntegerField('Bilirubin Total')
    trigliserida = IntegerField('Trigliserida')
    glukosa = IntegerField('Glukosa')
    gula_puasa = IntegerField('Gula Puasa')
    gula_sewaktu = IntegerField('Gula Sewaktu')
    asam_urat = IntegerField('Asam Urat')
    ht = IntegerField('Ht')
    ureum = IntegerField('Ureum')
    kalium = IntegerField('Kalium')
    klorida = IntegerField('Klorida')
    ver_mvc = IntegerField('Ver(Mvc)')
    
    # AKHIR DATA BIOKIMIA
    
    
    
    
    # DATA FISIK KLINIS
    tekanan_darah = IntegerField('Tekanan Darah')
    suhu = IntegerField('Suhu Tubuh (C)')
    nadi = IntegerField('Denyut Nadi (kali / Menit)')
    respirasi = IntegerField('Respiratory Rate (menit)')
    
    
    masalah_oral = MultiCheckboxField('Permasalahan Terkait oral', 
                                       choices =[ 
                                            ("1",'Susah Mengunyah'), 
                                            ("2", 'Susah Menelan'),
					                        ("3", 'Tidak Bisa menelan'),
					                        ("4", 'Normal/tidak ada masalah')
                                            ])
    
    
    luka_bakar = IntegerField('Luka Bakar (%) ditulis desimal')
    
    kelainan_fisik = MultiCheckboxField('Kelainan Pada Fisik/Klinis',
                                        choices=[
                                            'bibir pecah-pecah',
                                            'wajah pucat', 
                                            'mata merah',
                                            'kesulitan berbicara',
                                            'sesak napas/napas tidak lancar',
                                            'kesadaran lemah/tidak sadar'
                                            ]) 

    # AKHIR DATA FISIK KLINIS
    
    
    # DATA RIWAYAT MAKAN / ASUPAN
    energi = IntegerField('Riwayat Energi (kkal) ')
    protein = IntegerField('Riwayat Protein (gr)')
    lemak = IntegerField('Riwayat Lemak (gr)')
    karbo = IntegerField('Riwayat Karbohidrat (gr)')
    # AKHIR DATA RIWAYAT MAKAN / ASUPAN
     
    
    analisa = SubmitField('Analisa')
    hasil_pdf = SubmitField('Print Hasil Pdf')
    pdf_form = SubmitField('Print Form')
