from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, FloatField, SubmitField, SelectField, SelectMultipleField, widgets, TextAreaField)
from wtforms.validators import (DataRequired, Email)
from flask import (request, render_template)


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

    
class pagtform(FlaskForm):
    
    # DATA DIRI DAN ANTROPOMETRI
    nama = StringField('Nama', validators=[DataRequired(message='data harus diisi')])
    umur = IntegerField('Umur (dalam tahun, min 17th)', validators=[DataRequired(message='data harus diisi')])
    pekerjaan = StringField('Pekerjaan (Boleh Dikosongkan)')
    bb = IntegerField('Berat Badan (dalam kg)', validators=[DataRequired(message='data harus diisi')])
    tb = IntegerField('Tinggi Badan (dalam cm)', validators=[DataRequired(message='data harus diisi')])
    lila = IntegerField('Lingkar Lengan Atas (dalam cm)', validators=[DataRequired(message='data harus diisi')])
    
    catatan_personal = TextAreaField('Catatan Personal Lain-lainnya (Jika ada)', render_kw={'rows':5})
    
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
                                'hiv/aids', 'alergi', 'gout artritis', 'luka bakar', 
                                'penyakit saluran ceran atas', 'penyakit saluran cerna bawah',
                                'kanker', 'penyakit autoimun (lupus)', 'ablasi tiroid'
                                ])
    
    gender = SelectField('Gender', choices=['pria', 'wanita'])
    # AKHIR DIRI DAN ANTROPOMETRI
    
    
    
    
    # DATA BIOKIMIA
    hb = IntegerField('Hb (g/dl)')
    ldl = IntegerField('Ldl (mg/dl)')
    hdl = IntegerField('Hdl (mg/dl)')
    kolesterol = IntegerField('Kolesterol Total (mg/dl)')
    sgot = IntegerField('Sgot')
    sgpt = IntegerField('Sgpt')
    bun = IntegerField('Bun (mg/dl)')
    bilirubin_direk = IntegerField('Bilirubin Direk (mg/dl)')
    bilirubin_indirek = IntegerField('Bilirubin inDirek (mg/dl)')
    bilirubin_total = IntegerField('Bilirubin Total (mg/dl)')
    trigliserida = IntegerField('Trigliserida (mg/dl)')
    glukosa = IntegerField('Glukosa (mg/dl)')
    gula_puasa = IntegerField('Gula Puasa (mg/dl)')
    gula_sewaktu = IntegerField('Gula Sewaktu (mg/dl)')
    asam_urat = IntegerField('Asam Urat (mg/dl)')
    ht = IntegerField('Ht')
    ureum = IntegerField('Ureum (mg/dl)')
    kalium = IntegerField('Kalium (mmol/l)')
    klorida = IntegerField('Klorida (mmol/l)')
    ver_mvc = IntegerField('Ver(Mvc)')
    kreatinin = IntegerField('kreatinin (mg/dl)')
    limfosit = IntegerField('Limfosit')
    albumin = IntegerField('Albumin (g/dl)')
    trombosit = IntegerField('Trombosit (/ml)')
    hematokrit = IntegerField('Hematokrit')
    leukosit = IntegerField('Leukosit (/ml)')
    natrium = IntegerField('Natrium (mmol/l)')
    # AKHIR DATA BIOKIMIA
    
    
    
    
    # DATA FISIK KLINIS
    tekanan_darah = IntegerField('Tekanan Darah (mmhg)')
    suhu = IntegerField('Suhu Tubuh (derajat C)')
    nadi = IntegerField('Denyut Nadi (kali / Menit)')
    respirasi = IntegerField('Respiratory Rate (menit)')
    
    
    masalah_oral = MultiCheckboxField('Permasalahan Terkait oral', 
                                       choices =[ 
                                            ("1",'Susah Mengunyah'), 
                                            ("2", 'Susah Menelan'),
					                        ("3", 'Tidak Bisa menelan'),
					                        ("4", 'Normal/tidak ada masalah')
                                            ])
    
    
    luka_bakar = IntegerField('Luka Bakar (jika ada) % ditulis desimal')
    
    kelainan_fisik = MultiCheckboxField('Kelainan Pada Fisik/Klinis',
                                        choices=[
                                            'bibir pecah-pecah',
                                            'wajah pucat', 
                                            'mata merah',
                                            'kesulitan berbicara',
                                            'sesak napas/napas tidak lancar',
                                            'kesadaran lemah/tidak sadar'
                                            ]) 
    
    lainnya = TextAreaField('Lain-lainnya', render_kw={'rows':5})


    # AKHIR DATA FISIK KLINIS
    
    
    # DATA RIWAYAT MAKAN / ASUPAN
    energi = IntegerField('Riwayat Energi (kkal) ')
    protein = IntegerField('Riwayat Protein (gr)')
    lemak = IntegerField('Riwayat Lemak (gr)')
    karbo = IntegerField('Riwayat Karbohidrat (gr)')
    kebiasaan_makan = TextAreaField('Riwayat Kebiasaan Makan (Jika ada)', render_kw={'rows':5})

    # AKHIR DATA RIWAYAT MAKAN / ASUPAN
     
     
    #  FORMULIR INPUT INTERVENSI DAN DIAGNOSA DAN PRESPEKTIF DIET OPSIONAL
    
    # diagnosa
    problem  = TextAreaField('Problem')
    etiologi = TextAreaField('Etiologi')
    sign_tom = TextAreaField('Sign/Signtom')
    # akhir diagnosa
    
    # intervensi
    tujuan = TextAreaField('Tujuan')
    cara   = TextAreaField('Cara')
    target = TextAreaField('Target')
    # akhir intervensi
    
    # rencana diet
    jenis_diet = SelectField('Jenis Diet', choices=['TETP', 'DASH','']) 
    # akhir rencana diet
    
    # rencana monev
    
    # akhir rencana monev
    
    # AKHIR FORMULIR INPUT INTERVENSI DAN DIAGNOSA DAN PRESPEKTIF DIET OPSIONAL
    
    
    
    
    analisa = SubmitField('Analisa')
    hasil_pdf = SubmitField('Print Hasil Pdf')
    pdf_form = SubmitField('Save Data')
