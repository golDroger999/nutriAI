from flask import (render_template, redirect, request, Blueprint, url_for, make_response)
from web.beranda.form import (FormDubois, FormHarrisBenneedict, FormMifflin, FormPerkeni, FormHamil, FormMenyusui)
from web.func_rumus.mikro import (gizimikro, gizimikro_hamil, gizimikro_menyusui)
from web.func_rumus.harris import harris
from web.func_rumus.dubois import dubois
from web.func_rumus.mifflin import mifflin
from web.func_rumus.perkeni import perkeni
from web.func_rumus.makan import makan
import pdfkit





beranda = Blueprint('beranda', __name__, template_folder='templates')


# HALAMAN BERANDA 
@beranda.route('/beranda')
@beranda.route('/')
def beranda_page():
    return render_template('beranda.html', tittle='NUTRIECY')
# AKHIR HALAMAN BERANDA




# HALAMANAN FORM DUBOIS
@beranda.route('/dubois', methods=['POST', 'GET'])
def dubois_page():
    form = FormDubois() 
     
    makro = ''
    mikro = ''
    permakan =''
    
    bb ='' 
    tb = ''
    umur =''
    gender = ''
    tidur =''
    aktivitas = ''
    
    if request.method == 'POST':
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        gender = request.form.get('gender')
        aktivitas = float(request.form.get('aktivitas'))
        tidur = int(request.form.get('tidur'))
        
        
        makro = dubois(bb=bb, tb=tb, umur=umur, gender=gender, aktivitas=aktivitas, tidur=tidur)
        permakan = makan(energi=makro.energi(), protein=makro.protein(), lemak=makro.lemak(), karbo=makro.karbo()).makan()
        mikro = gizimikro(umur=umur, gender=gender)
        
        
    if request.form.get('laporan'):
        nama = request.form.get('nama')
        
        rendered = render_template('report.html', nama=nama, bb=bb, tb=tb, umur=umur, 
                                gender=gender, makro=makro, mikro=mikro, permakan=permakan, 
                                energi=makro.energi(), bmr=makro.bmr())
        
        pdf = pdfkit.from_string(rendered)
        response =  make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        return response
    
    return render_template('dubois.html', tittle='DUBOIS',
                           form=form, bb=bb, tb=tb, umur=umur, 
                           gender=gender, makro=makro, mikro=mikro,
                           permakan=permakan)
   
# AKHIR HALAMANAN FORM DUBOIS





# HALAMAN FORM HARRIS BENEDICT
@beranda.route('/harris-bennedict', methods=['POST', 'GET'])
def harris_bennedict_page():
    form = FormHarrisBenneedict()
    
    makro =''
    mikro =''
    permakan = ''
    
    bb =''
    tb = ''
    umur =''
    gender = ''
    aktivitas = ''
    stress = ''
    
    if request.method == 'POST':
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        gender = request.form.get('gender')
        stress = float(request.form.get('stress'))
        aktivitas = float(request.form.get('aktivitas'))
        
        makro = harris(bb=bb, tb=tb, umur=umur, gender=gender, aktivitas=aktivitas, stress=stress)
        permakan = makan(energi=makro.tee(), protein=makro.protein(), lemak=makro.lemak(), karbo=makro.karbo()).makan()
        mikro = gizimikro(umur=umur, gender=gender)
        
    
    if request.form.get('laporan'):
        nama = request.form.get('nama')
        
        rendered = render_template('report.html', nama=nama, bb=bb, tb=tb, umur=umur, 
                                gender=gender, makro=makro, mikro=mikro, permakan=permakan, 
                                energi=makro.tee(), bmr=makro.bee())
        
        pdf = pdfkit.from_string(rendered)
        response =  make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        return response
    
    return render_template('harris.html',tittle='HARRIS BENNEDICT', 
                           form=form, bb=bb, tb=tb, umur=umur, 
                           gender=gender, makro=makro, mikro=mikro,
                           permakan=permakan)
# AKHIR HALAMAN FORM HARRIS BENEDICT
  
  
  
    
    
# HALAMAN FORM MIFFLIN    
@beranda.route('/mifflin', methods=['POST', 'GET'])
def mifflin_page():
    form = FormMifflin()
    
    makro = ''
    mikro = ''
    permakan = ''
    
    bb =''
    tb = ''
    umur =''
    gender = ''
    aktivitas = ''
    stress = ''

    
    if request.method == 'POST':
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        gender = request.form.get('gender')
        stress = float(request.form.get('stress'))
        aktivitas = float(request.form.get('aktivitas'))
   
        makro = harris(bb=bb, tb=tb, umur=umur, gender=gender, aktivitas=aktivitas, stress=stress)
        permakan = makan(energi=makro.tee(), protein=makro.protein(), lemak=makro.lemak(), karbo=makro.karbo()).makan()
        mikro = gizimikro(umur=umur, gender=gender)
    
       
    if request.form.get('laporan'):
        nama = request.form.get('nama')
        
        rendered = render_template('report.html', nama=nama, bb=bb, tb=tb, umur=umur, 
                                gender=gender, makro=makro, mikro=mikro, permakan=permakan, 
                                energi=makro.tee(), bmr=makro.bee())
        
        pdf = pdfkit.from_string(rendered)
        response =  make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        return response
    
    return render_template('mifflin.html',tittle='MIFFLIN', 
                           form=form, bb=bb, tb=tb, umur=umur, 
                           gender=gender, makro=makro, mikro=mikro, 
                           permakan=permakan)
# AKHIR HALAMAN FORM MIFFLIN    
   
   
   
    
    
# HALAMAN FORM PERKENI 
@beranda.route('/perkeni', methods=['GET', 'POST'])
def perkeni_page():
    form = FormPerkeni()
    
    makro = ''
    mikro = ''
    permakan = ''
    
    bb =''
    tb = ''
    umur =''
    gender = ''
    
    if request.method == 'POST': 
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        gender = request.form.get('gender')
        aktivitas = float(request.form.get('aktivitas'))
    
        makro = perkeni(bb=bb, tb=tb, umur=umur, gender=gender, aktivitas=aktivitas)
        permakan = makan(energi=makro.energi(), protein=makro.protein(), lemak=makro.lemak(), karbo=makro.karbo()).makan()
        mikro = gizimikro(umur=umur, gender=gender)
    
        
    if request.form.get('laporan'):
        nama = request.form.get('nama')
        
        rendered = render_template('report.html', nama=nama, bb=bb, tb=tb, umur=umur, 
                           gender=gender, makro=makro, mikro=mikro, permakan=permakan)
        
        pdf = pdfkit.from_string(rendered)
        response =  make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        return response
    
    return render_template('perkeni.html',tittle='PERKENI', 
                           form=form, bb=bb, tb=tb, umur=umur, 
                           gender=gender, makro=makro, mikro=mikro,
                           permakan=permakan)
# AKHIR HALAMAN FORM PERKENI 
  
  
  
    
    
# HALAMAN FORM IBU HAMIL      
@beranda.route('/gizi-ibu-hamil', methods=['POST', 'GET'])
def gizihamil_page():
    form = FormHamil()
    bb =''
    tb = ''
    umur =''
    tidur = ''
    umurhamil = ''
    trimester = ''
    
    imt = ''
    bbi = ''
    bbih = ''
    bmr = ''
    energi = ''
    protein = ''
    lemak = ''
    karbo = ''
    
    energi_pagi = ''
    protein_pagi = ''
    lemak_pagi = ''
    karbo_pagi = ''
    
    energi_siang = ''
    protein_siang = ''
    lemak_siang = ''
    karbo_siang = ''
    
    energi_malam = ''
    protein_malam = ''
    lemak_malam = ''
    karbo_malam = ''
    
    vitamin_a   = ''
    vitamin_d   = ''
    vitamin_e   = ''
    vitamin_k   = ''
    vitamin_b1  = ''
    vitamin_b2  = ''
    vitamin_b3  = ''
    vitamin_b5  = ''
    vitamin_b6  = ''
    vitamin_b12 = ''
    folat =''
    biotin = ''
    kolin = ''
    vitamin_c = ''
    
    kalsium =''
    fosfor =''
    magnesium =''
    besi =''
    iodium = ''
    seng = ''
    selenium = ''
    mangan = ''
    fluor = ''
    kromium = ''
    kalium =''
    natrium = ''
    klor =''
    tembaga=''
    
    
    if request.method == 'POST' and 'bb' in request.form and 'tb' in request.form and 'umur' in request.form and 'trimester' in request.form and 'umurhamil' in request.form  and 'aktivitas' in request.form  and 'tidur' in request.form:
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        tidur = int(request.form.get('tidur'))
        aktivitas = float(request.form.get('aktivitas'))
        umurhamil = float(request.form.get('umurhamil'))
        trimester = (request.form.get('trimester'))
        
        imt = round ((bb /(tb/100)**2),2)
        
        if tb >=160:
            bbi = tb - 110
            
        elif tb <=160: 
            bbi = tb - 105
        
        bbi = round(bbi,2)
        bbih = round(bbi + (umurhamil * 0.35),2)
        bmr = round((0.90 * 24 * bbih),2)
        koreksi_tidur = round((0.1 * tidur * bbih ),2)  
        
        c_kalori = round((bmr - koreksi_tidur),2)
        aktivitas  = round((aktivitas * c_kalori),2)
        e_kalori  = round((c_kalori + aktivitas),2)
        sda = round((0.1 * e_kalori),2)
        
        if request.form.get('trimester') == 'Trimester 1':
            energi = round((e_kalori + sda + 180 ),2)
            protein = round((0.15 * energi)/4 + 1, 2)
            lemak = round((0.25 * energi)/9 + 2.3, 2)   
            karbo  = round((0.65 * energi)/4 + 25, 2) 
            
        elif request.form.get('trimester') == 'Trimester 2':
            energi = round((e_kalori + sda + 300 ),2)
            protein = round((0.15 * energi)/4 + 10, 2)
            lemak = round((0.25 * energi)/9 + 2.3, 2)   
            karbo  = round((0.65 * energi)/4 + 40, 2)
            
        elif request.form.get('trimester') == 'Trimester 3':
            energi = round((e_kalori + sda + 300 ),2)
            protein = round((0.15 * energi)/4 + 30, 2)
            lemak = round((0.25 * energi)/9 + 2.3, 2)   
            karbo  = round((0.65 * energi)/4 + 40, 2)
        
       
        
        energi_pagi = round((0.35 * energi),2)
        protein_pagi = round((0.35 * protein),2)
        lemak_pagi = round((0.35 * lemak),2)
        karbo_pagi = round((0.35 * karbo),2)
        
        energi_siang = round((0.35 * energi),2)
        protein_siang = round((0.35 * protein),2)
        lemak_siang = round((0.35 * lemak),2)
        karbo_siang = round((0.35 * karbo),2)
        
        energi_malam = round((0.30 * energi),2)
        protein_malam = round((0.30 * protein),2)
        lemak_malam = round((0.30 * lemak),2)
        karbo_malam = round((0.30 * karbo),2)
     
        vitamin_a = gizimikro_hamil(umur=umur, trimester=trimester).vitamin_a()
        vitamin_d = gizimikro_hamil(umur=umur, trimester=trimester).vitamin_d()
        vitamin_e = gizimikro_hamil(umur=umur, trimester=trimester).vitamin_e()
        vitamin_k = gizimikro_hamil(umur=umur, trimester=trimester).vitamin_k()
        vitamin_b1 = gizimikro_hamil(umur=umur, trimester=trimester).vitamin_b1()
        vitamin_b2 = gizimikro_hamil(umur=umur, trimester=trimester).vitamin_b2()
        vitamin_b3 = gizimikro_hamil(umur=umur, trimester=trimester).vitamin_b3()
        vitamin_b5 = gizimikro_hamil(umur=umur, trimester=trimester).vitamin_b5()
        vitamin_b6 = gizimikro_hamil(umur=umur, trimester=trimester).vitamin_b6()
        vitamin_b12 = gizimikro_hamil(umur=umur, trimester=trimester).vitamin_b12()
        folat = gizimikro_hamil(umur=umur, trimester=trimester).folat()
        biotin = gizimikro_hamil(umur=umur, trimester=trimester).biotin()
        kolin = gizimikro_hamil(umur=umur, trimester=trimester).kolin()
        vitamin_c = gizimikro_hamil(umur=umur, trimester=trimester).vitamin_c()
        
        
        kalsium = gizimikro_hamil(umur=umur, trimester=trimester).kalsium()
        fosfor = gizimikro_hamil(umur=umur, trimester=trimester).fosfor()
        magnesium = gizimikro_hamil(umur=umur, trimester=trimester).magnesium()
        besi = gizimikro_hamil(umur=umur, trimester=trimester).besi()
        iodium = gizimikro_hamil(umur=umur, trimester=trimester).iodium()
        seng = gizimikro_hamil(umur=umur, trimester=trimester).seng()
        selenium = gizimikro_hamil(umur=umur, trimester=trimester).selenium()
        mangan = gizimikro_hamil(umur=umur, trimester=trimester).mangan()
        fluor = gizimikro_hamil(umur=umur, trimester=trimester).fluor()
        kromium = gizimikro_hamil(umur=umur, trimester=trimester).kromium()
        kalium = gizimikro_hamil(umur=umur, trimester=trimester).kalium()
        natrium = gizimikro_hamil(umur=umur, trimester=trimester).natrium()
        klor = gizimikro_hamil(umur=umur, trimester=trimester).klor()
        tembaga = gizimikro_hamil(umur=umur, trimester=trimester).tembaga()
        
    if request.form.get('laporan'):
        nama = request.form.get('nama')
        rendered = render_template('report.html', nama=nama, bb=bb, tb=tb, umur=umur, 
                           imt=imt, bbi=bbi, bmr=bmr, energi=energi, 
                           protein=protein, lemak=lemak, karbo=karbo,
                           energi_pagi=energi_pagi, protein_pagi=protein_pagi,
                           lemak_pagi=lemak_pagi, karbo_pagi=karbo_pagi,
                           energi_siang=energi_siang, protein_siang=protein_siang,
                           lemak_siang=lemak_siang, karbo_siang=karbo_siang,
                           energi_malam=energi_malam, protein_malam=protein_malam,
                           lemak_malam=lemak_malam, karbo_malam=karbo_malam)
        
        pdf = pdfkit.from_string(rendered)
        response =  make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        return response 
    
    return render_template('hamil.html', tittle='GIZI IBU HAMIL', 
                           form=form, bb=bb, tb=tb, umur=umur, trimester=trimester, umurhamil=umurhamil, 
                           imt=imt, bbi=bbi,bbih=bbih,bmr=bmr, energi=energi, 
                           protein=protein, lemak=lemak, karbo=karbo,
                           energi_pagi=energi_pagi, protein_pagi=protein_pagi,
                           lemak_pagi=lemak_pagi, karbo_pagi=karbo_pagi,
                           energi_siang=energi_siang, protein_siang=protein_siang,
                           lemak_siang=lemak_siang, karbo_siang=karbo_siang,
                           energi_malam=energi_malam, protein_malam=protein_malam,
                           lemak_malam=lemak_malam, karbo_malam=karbo_malam,
                           
                           vitamin_a=vitamin_a, vitamin_d=vitamin_d, vitamin_e=vitamin_e,
                           vitamin_k=vitamin_k, vitamin_b1=vitamin_b1, vitamin_b2=vitamin_b2,
                           vitamin_b3=vitamin_b3, vitamin_b5=vitamin_b5, vitamin_b6=vitamin_b6,
                           vitamin_b12=vitamin_b12, folat=folat, biotin=biotin, kolin=kolin, vitamin_c=vitamin_c,
                           kalsium=kalsium, fosfor=fosfor, magnesium=magnesium, besi=besi, iodium=iodium,
                           seng=seng, selenium=selenium, mangan=mangan, fluor=fluor, kromium=kromium,
                           kalium=kalium, natrium=natrium, klor=klor, tembaga=tembaga)
# AKHIR HALAMAN FORM IBU HAMIL





# HALAMAN FORM IBU MENYUSUI
@beranda.route('/gizi-ibu-menyusui', methods=['POST', 'GET'])
def gizimenyusui_page():
    form = FormMenyusui()
    bb = ''
    tb = ''
    umur =''
    tidur = ''
    siklus = '' 
       
    imt = ''
    bbi = ''
    bmr = ''
    energi = ''
    protein = ''
    lemak = ''
    karbo = ''
    
    energi_pagi = ''
    protein_pagi = ''
    lemak_pagi = ''
    karbo_pagi = ''
    
    energi_siang = ''
    protein_siang = ''
    lemak_siang = ''
    karbo_siang = ''
    
    energi_malam = ''
    protein_malam = ''
    lemak_malam = ''
    karbo_malam = ''
    
    vitamin_a   = ''
    vitamin_d   = ''
    vitamin_e   = ''
    vitamin_k   = ''
    vitamin_b1  = ''
    vitamin_b2  = ''
    vitamin_b3  = ''
    vitamin_b5  = ''
    vitamin_b6  = ''
    vitamin_b12 = ''
    folat =''
    biotin = ''
    kolin = ''
    vitamin_c = ''
    
    kalsium =''
    fosfor =''
    magnesium =''
    besi =''
    iodium = ''
    seng = ''
    selenium = ''
    mangan = ''
    fluor = ''
    kromium = ''
    kalium =''
    natrium = ''
    klor =''
    tembaga=''
    
    
    if request.method == 'POST' and 'bb' in request.form and 'tb' in request.form and 'umur' in request.form and 'siklus' in request.form   and 'aktivitas' in request.form  and 'tidur' in request.form:
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        tidur = int(request.form.get('tidur'))
        aktivitas = float(request.form.get('aktivitas'))
        siklus = request.form.get('siklus')
        
        
        imt = round ((bb /(tb/100)**2),2)
        bbi = round (0.9 * (tb-100),2)

        bmr = round((0.90 * 24 * bbi),2)
        koreksi_tidur = round((0.1 * tidur * bbi ),2)  
        c_kalori = round((bmr - koreksi_tidur),2)
        aktivitas  = round((aktivitas * c_kalori),2)
        e_kalori  = round((c_kalori + aktivitas),2)
        sda = round((0.1 * e_kalori),2)

        if request.form.get('siklus') == '6 bulan pertama':
            energi = round((e_kalori + sda + 330),2)
            protein = round((0.15 * energi)/4 + 20, 2)
            lemak = round((0.25 * energi)/9 + 2.2, 2)   
            karbo  = round((0.65 * energi)/4 +45, 2)

        else:
            energi = round((e_kalori + sda + 400),2)
            protein = round((0.15 * energi)/4 + 15, 2)
            lemak = round((0.25 * energi)/9 + 2.2, 2)   
            karbo  = round((0.65 * energi)/4 + 55, 2)

        energi_pagi = round((0.35 * energi),2)
        protein_pagi = round((0.35 * protein),2)
        lemak_pagi = round((0.35 * lemak),2)
        karbo_pagi = round((0.35 * karbo),2)

        energi_siang = round((0.35 * energi),2)
        protein_siang = round((0.35 * protein),2)
        lemak_siang = round((0.35 * lemak),2)
        karbo_siang = round((0.35 * karbo),2)

        energi_malam = round((0.30 * energi),2)
        protein_malam = round((0.30 * protein),2)
        lemak_malam = round((0.30 * lemak),2)
        karbo_malam = round((0.30 * karbo),2)
    
        vitamin_a = gizimikro_menyusui(umur=umur, siklus=siklus).vitamin_a()
        vitamin_d = gizimikro_menyusui(umur=umur, siklus=siklus).vitamin_d()
        vitamin_e = gizimikro_menyusui(umur=umur, siklus=siklus).vitamin_e()
        vitamin_k = gizimikro_menyusui(umur=umur, siklus=siklus).vitamin_k()
        vitamin_b1 = gizimikro_menyusui(umur=umur, siklus=siklus).vitamin_b1()
        vitamin_b2 = gizimikro_menyusui(umur=umur, siklus=siklus).vitamin_b2()
        vitamin_b3 = gizimikro_menyusui(umur=umur, siklus=siklus).vitamin_b3()
        vitamin_b5 = gizimikro_menyusui(umur=umur, siklus=siklus).vitamin_b5()
        vitamin_b6 = gizimikro_menyusui(umur=umur, siklus=siklus).vitamin_b6()
        vitamin_b12 = gizimikro_menyusui(umur=umur, siklus=siklus).vitamin_b12()
        folat = gizimikro_menyusui(umur=umur, siklus=siklus).folat()
        biotin = gizimikro_menyusui(umur=umur, siklus=siklus).biotin()
        kolin = gizimikro_menyusui(umur=umur, siklus=siklus).kolin()
        vitamin_c = gizimikro_menyusui(umur=umur, siklus=siklus).vitamin_c()
        
        
        kalsium = gizimikro_menyusui(umur=umur, siklus=siklus).kalsium()
        fosfor = gizimikro_menyusui(umur=umur, siklus=siklus).fosfor()
        magnesium = gizimikro_menyusui(umur=umur, siklus=siklus).magnesium()
        besi = gizimikro_menyusui(umur=umur, siklus=siklus).besi()
        iodium = gizimikro_menyusui(umur=umur, siklus=siklus).iodium()
        seng = gizimikro_menyusui(umur=umur, siklus=siklus).seng()
        selenium = gizimikro_menyusui(umur=umur, siklus=siklus).selenium()
        mangan = gizimikro_menyusui(umur=umur, siklus=siklus).mangan()
        fluor = gizimikro_menyusui(umur=umur, siklus=siklus).fluor()
        kromium = gizimikro_menyusui(umur=umur, siklus=siklus).kromium()
        kalium = gizimikro_menyusui(umur=umur, siklus=siklus).kalium()
        natrium = gizimikro_menyusui(umur=umur, siklus=siklus).natrium()
        klor = gizimikro_menyusui(umur=umur, siklus=siklus).klor()
        tembaga = gizimikro_menyusui(umur=umur, siklus=siklus).tembaga()
       
    if request.form.get('laporan'):
        nama = request.form.get('nama')
        rendered = render_template('report.html', nama=nama, bb=bb, tb=tb, umur=umur, 
                           imt=imt, bbi=bbi, bmr=bmr, energi=energi, 
                           protein=protein, lemak=lemak, karbo=karbo,
                           energi_pagi=energi_pagi, protein_pagi=protein_pagi,
                           lemak_pagi=lemak_pagi, karbo_pagi=karbo_pagi,
                           energi_siang=energi_siang, protein_siang=protein_siang,
                           lemak_siang=lemak_siang, karbo_siang=karbo_siang,
                           energi_malam=energi_malam, protein_malam=protein_malam,
                           lemak_malam=lemak_malam, karbo_malam=karbo_malam)
        
        pdf = pdfkit.from_string(rendered)
        response =  make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        return response 
    
    return render_template('menyusui.html', tittle='GIZI IBU MENYUSUI',
                         form=form,  bb=bb, tb=tb, umur=umur, siklus=siklus, 
                           imt=imt, bbi=bbi, bmr=bmr, energi=energi, 
                           protein=protein, lemak=lemak, karbo=karbo,
                           energi_pagi=energi_pagi, protein_pagi=protein_pagi,
                           lemak_pagi=lemak_pagi, karbo_pagi=karbo_pagi,
                           energi_siang=energi_siang, protein_siang=protein_siang,
                           lemak_siang=lemak_siang, karbo_siang=karbo_siang,
                           energi_malam=energi_malam, protein_malam=protein_malam,
                           lemak_malam=lemak_malam, karbo_malam=karbo_malam,
                           
                           vitamin_a=vitamin_a, vitamin_d=vitamin_d, vitamin_e=vitamin_e,
                           vitamin_k=vitamin_k, vitamin_b1=vitamin_b1, vitamin_b2=vitamin_b2,
                           vitamin_b3=vitamin_b3, vitamin_b5=vitamin_b5, vitamin_b6=vitamin_b6,
                           vitamin_b12=vitamin_b12, folat=folat, biotin=biotin, kolin=kolin, vitamin_c=vitamin_c,
                           kalsium=kalsium, fosfor=fosfor, magnesium=magnesium, besi=besi, iodium=iodium,
                           seng=seng, selenium=selenium, mangan=mangan, fluor=fluor, kromium=kromium,
                           kalium=kalium, natrium=natrium, klor=klor, tembaga=tembaga)
# AKHIR HALAMAN FORM IBU MENYUSUI




#  FORM PENYAKIT GINJAL

# AKHIR FROM PENYAKIT GINJAL