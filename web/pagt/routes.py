from flask import (render_template, redirect, request, Blueprint, url_for, make_response)
from web.func_rumus import harris
from web.func_rumus import makan
from web.func_rumus import gizimikro
from web.func_rumus import biokimia
from web.func_rumus import fisik_klinis
from web.pagt.form import pagtform


pagt = Blueprint('pagt', __name__,template_folder='templates')



@pagt.route('/masuk')
def masuk():
    pass

@pagt.route('/daftar')
def daftar():
    pass

@pagt.route('/pagt-form', methods=['POST', 'GET'])
def pagt_page():
    form = pagtform()
    data_diri = ''
    energi = ''
    gizi_makro = ''
    mikro = ''
    permakan_harris = ''
    harris = ''
    
    bb = ''
    tb = ''
    umur = ''
    gender = ''
    stress = ''
    aktivitas = ''
    penyakit =''
    
    
    hb = '' 
    ldl = '' 
    hdl = '' 
    kolesterol = ''
    sgot = '' 
    sgpt = '' 
    bun = '' 
    bilirubin_direk = ''
    bilirubin_indirek = ''  
    bilirubin_total = ''  
    trigliserida = '' 
    glukosa = '' 
    gula_puasa = ''
    gula_sewaktu = ''
    asam_urat = ''  
    ht = '' 
    ureum = '' 
    kalium = ''
    klorida = ''
    ver_mvc = '' 
    kreatinin = ''
    limfosit = '' 
    albumin = '' 
    trombosit = ''
    hematokrit = '' 
    leukosit = '' 
    natrium = '' 

    tekanan_darah = '' 
    suhu =  ''
    nadi =  ''
    respirasi = ''
    malasalah_oral = ''
    luka_bakar = ''
    kelainan_klinis = ''
    
    riwayat_energi = ''
    
    biokimia = ''
    fisik = ''
    riwayat_asupan = ''
    
    
    # Handle form request 
    if request.method == 'POST':
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        gender = request.form.get('gender')
        stress = float(request.form.get('stress'))
        aktivitas = request.form.get('aktivitas')
        
        hb = float(request.form.get('hb'))
        ldl = float(request.form.get('ldl'))
        hdl = float(request.form.get('hdl'))
        kolesterol =float(request.form.get('kolesterol'))
        sgpt = float(request.form.get('sgpt'))
        sgot = float(request.form.get('sgot'))
        bun = float(request.form.get('bun'))
        bilirubin_direk = float(request.form.get('bilirubin_direk'))
        bilirubin_indirek = float(request.form.get('bilirubin_indirek'))  
        bilirubin_total = float(request.form.get('bilirubin_total'))  
        trigliserida = float(request.form.get('trigliserida')) 
        glukosa = float(request.form.get('glukosa'))  
        gula_puasa = float(request.form.get('gula_puasa'))
        gula_sewaktu = float(request.form.get('gula_sewaktu'))
        asam_urat = float(request.form.get('asam_urat'))
        ht = float(request.form.get('ht')) 
        ureum = float(request.form.get('ureum')) 
        kalium = float(request.form.get('kalium'))
        klorida = float(request.form.get('klorida'))
        ver_mvc = float(request.form.get('ver_mvc')) 
        kreatinin = float(request.form.get('kreatinin'))
        limfosit = float(request.form.get('limfosit')) 
        albumin = float(request.form.get('albumin')) 
        trombosit = float(request.form.get('trombosit'))
        hematokrit = float(request.form.get('hematokrit')) 
        leukosit = float(request.form.get('leukosit')) 
        natrium = float(request.form.get('natrium')) 
        
        tekanan_darah = request.form.get('tekanan_darah') 
        suhu =  float(request.form.get('suhu'))
        nadi =  float(request.form.get('nadi'))
        respirasi = float(request.form.get('respirasi'))
        malasalah_oral = request.form.get('malasalah_oral')
        luka_bakar = float(request.form.get('luka_bakar'))
        kelainan_klinis = (request.form.get('kelainan_klinis'))
        
        
        
    # Antropometri handel
        data_diri = {'bb':bb, 'tb':tb, 'gender':gender, 'aktivitas':aktivitas, 'stress':stress}
    
    # perhitungan gizi handle
        makro = gizimikro(umur=umur, gender=gender)
        harris = harris(bb=bb, tb=tb, umur=umur, gender=gender, aktivitas=aktivitas, stress=stress)
        permakan_harris = makan(energi=harris.tee(), protein=harris.protein(), lemak=harris.lemak, karbo=harris.karbo()) 
        
    # Biokimia Handel
        biokimia = biokimia(umur=umur, gender=gender)
    
    # Fisik Klinis Handel
        fisik = fisik_klinis()
    
    # Riwayat Asupan Handel
    
    
    # Diagnosis Handel
    
    # Intervensi Handel
    
    # Rencana Monev Handel
    return render_template('pagt.html', tittle='PAGT FORM', form=form, data_diri=data_diri,
                           harris=harris, permakan_harris=permakan_harris, mikro=mikro,
                           biokimia=biokimia, fisik_klinis=fisik)




@pagt.route('/logout')
def logout():
    pass