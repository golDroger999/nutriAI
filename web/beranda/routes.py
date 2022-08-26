from flask import (render_template, redirect, request, Blueprint, url_for)
from web.beranda.form import (FormDubois, FormHarrisBenneedict, FormMifflin, FormPerkeni, FormHamil, FormMenyusui)



beranda = Blueprint('beranda', __name__)



# HALAMAN BERANDA 
@beranda.route('/beranda')
@beranda.route('/')
def beranda_page():
    return render_template('beranda.html', tittle='NUTRIECY')
# AKHIR HALAMAN BERANDA





# HALAMAN ROBOT
@beranda.route('/alat-analisis')
def robot_page():
    return render_template('alat_analisis.html', tittle='ANALISIS GIZI')
# AKHIR HALAMAN ROBOT





# HALAMAN SPREADSHEET TOOL
@beranda.route('/dashboard-page')
def spreadsheet_page():
    return render_template('dashboard.html', tittle='DASHBOARD')
# AKHIR HALAMAN SPREADSHEET TOOL





# HALAMANAN FORM DUBOIS
@beranda.route('/dubois', methods=['POST', 'GET'])
def dubois_page():
    form = FormDubois() 
    bb =''
    tb = ''
    umur =''
    gender = ''
    
    imt = ''
    bbi = ''
    bmr = ''
    energi = ''
    tidur = ''
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
    
    if request.method == 'POST' and 'bb' in request.form and 'tb' in request.form and 'umur' in request.form and 'gender' in request.form  and 'aktivitas' in request.form  and 'tidur' in request.form:
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        gender = request.form.get('gender')
        aktivitas = float(request.form.get('aktivitas'))
        tidur = int(request.form.get('tidur'))
        
    if request.form.get('hitung'):
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        gender = request.form.get('gender')
        tidur = int(request.form.get('tidur'))
        
        imt = round ((bb /(tb/100)**2),2)
        bbi = round (0.9 * (tb-100),2)
        
        if request.form.get('gender') == 'pria':
            bmr = 1 * 24 * bbi
        else:
            bmr = 0.90 * 24 * bbi
        
        bmr = round(bmr,2)
        koreksi_tidur = round((0.1 * tidur * bbi ),2)  
        c_kalori = round((bmr - koreksi_tidur),2)
        aktivitas  = round((aktivitas * c_kalori),2)
        e_kalori  = round((c_kalori + aktivitas),2)
        sda = round((0.1 * e_kalori),2)
        
        energi = round((e_kalori + sda),2)
        protein = round((0.15 * energi)/4, 2)
        lemak = round((0.25 * energi)/9, 2)   
        karbo  = round((0.65 * energi)/4, 2) 
        
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
        
    return render_template('dubois.html', tittle='DUBOIS', form=form, bb=bb, tb=tb, umur=umur, 
                           gender=gender,imt=imt, bbi=bbi, bmr=bmr, energi=energi, 
                           protein=protein, lemak=lemak, karbo=karbo,
                           energi_pagi=energi_pagi, protein_pagi=protein_pagi,
                           lemak_pagi=lemak_pagi, karbo_pagi=karbo_pagi,
                           energi_siang=energi_siang, protein_siang=protein_siang,
                           lemak_siang=lemak_siang, karbo_siang=karbo_siang,
                           energi_malam=energi_malam, protein_malam=protein_malam,
                           lemak_malam=lemak_malam, karbo_malam=karbo_malam)
# AKHIR HALAMANAN FORM DUBOIS





# HALAMAN FORM HARRIS BENEDICT
@beranda.route('/harris-bennedict', methods=['POST', 'GET'])
def harris_bennedict_page():
    form = FormHarrisBenneedict()
    bb =''
    tb = ''
    umur =''
    gender = ''
    
    imt = ''
    bbi = ''
    bee = ''
    tee = ''
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
    
    if request.method == 'POST' and 'bb' in request.form and 'tb' in request.form and 'umur' in request.form and 'gender' in request.form and 'stress' in request.form and 'aktivitas' in request.form:
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        gender = request.form.get('gender')
        stress = float(request.form.get('stress'))
        aktivitas = float(request.form.get('aktivitas'))
        
    if request.form.get('hitung'):
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        gender = request.form.get('gender')
        
        imt = round ((bb /(tb/100)**2),2)
        bbi = round (0.9 * (tb-100),2)
        
        if request.form.get('gender') == 'pria':
            bee = 66 + (13.7 * bb) + (5 * tb) - (6.8 * umur)
        else:
            bee = 655 + (9.6 * bb) + (1.8 * tb) - (4.7 * umur)

        bee= round(bee,2)
        tee = round((bee * aktivitas * stress),2 )
        protein = round((0.15 * tee)/4, 2)
        lemak = round((0.25 * tee)/9, 2)   
        karbo  = round((0.65 * tee)/4, 2) 
        
        energi_pagi = round((0.35 * tee),2)
        protein_pagi = round((0.35 * protein),2)
        lemak_pagi = round((0.35 * lemak),2)
        karbo_pagi = round((0.35 * karbo),2)
        
        energi_siang = round((0.35 * tee),2)
        protein_siang = round((0.35 * protein),2)
        lemak_siang = round((0.35 * lemak),2)
        karbo_siang = round((0.35 * karbo),2)
        
        energi_malam = round((0.30 * tee),2)
        protein_malam = round((0.30 * protein),2)
        lemak_malam = round((0.30 * lemak),2)
        karbo_malam = round((0.30 * karbo),2)
        
    return render_template('harris.html',tittle='HARRIS BENNEDICT', 
                           form=form, bb=bb, tb=tb, umur=umur, 
                           gender=gender,imt=imt, bbi=bbi, bee=bee, tee=tee, 
                           protein=protein, lemak=lemak, karbo=karbo,
                           energi_pagi=energi_pagi, protein_pagi=protein_pagi,
                           lemak_pagi=lemak_pagi, karbo_pagi=karbo_pagi,
                           energi_siang=energi_siang, protein_siang=protein_siang,
                           lemak_siang=lemak_siang, karbo_siang=karbo_siang,
                           energi_malam=energi_malam, protein_malam=protein_malam,
                           lemak_malam=lemak_malam, karbo_malam=karbo_malam)
# AKHIR HALAMAN FORM HARRIS BENEDICT
  
  
  
    
    
# HALAMAN FORM MIFFLIN    
@beranda.route('/mifflin', methods=['POST', 'GET'])
def mifflin_page():
    form = FormMifflin()
    bb =''
    tb = ''
    umur =''
    gender = ''
    
    imt = ''
    bbi = ''
    bee = ''
    tee = ''
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
    
    if request.method == 'POST' and 'bb' in request.form and 'tb' in request.form and 'umur' in request.form and 'gender' in request.form and 'stress' in request.form and 'aktivitas' in request.form:
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        gender = request.form.get('gender')
        stress = float(request.form.get('stress'))
        aktivitas = float(request.form.get('aktivitas'))
        
    if request.form.get('hitung'):
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        gender = request.form.get('gender')
        
        imt = round ((bb /(tb/100)**2),2)
        bbi = round (0.9 * (tb-100),2)
        
        if request.form.get('gender') == 'pria':
            bee = (10 * bb) + (6.25 * tb) - (5 * umur) + 5
        else:
            bee = (10 * bb) + (6.25 * tb) - (5 * umur) - 161

        bee= round(bee,2)
        tee = round((bee * aktivitas * stress),2 )
        protein = round((0.15 * tee)/4, 2)
        lemak = round((0.25 * tee)/9, 2)   
        karbo  = round((0.65 * tee)/4, 2) 
        
        energi_pagi = round((0.35 * tee),2)
        protein_pagi = round((0.35 * protein),2)
        lemak_pagi = round((0.35 * lemak),2)
        karbo_pagi = round((0.35 * karbo),2)
        
        energi_siang = round((0.35 * tee),2)
        protein_siang = round((0.35 * protein),2)
        lemak_siang = round((0.35 * lemak),2)
        karbo_siang = round((0.35 * karbo),2)
        
        energi_malam = round((0.30 * tee),2)
        protein_malam = round((0.30 * protein),2)
        lemak_malam = round((0.30 * lemak),2)
        karbo_malam = round((0.30 * karbo),2)
        
    return render_template('mifflin.html',tittle='MIFFLIN', 
                           form=form, bb=bb, tb=tb, umur=umur, 
                           gender=gender,imt=imt, bbi=bbi, bee=bee, tee=tee, 
                           protein=protein, lemak=lemak, karbo=karbo,
                           energi_pagi=energi_pagi, protein_pagi=protein_pagi,
                           lemak_pagi=lemak_pagi, karbo_pagi=karbo_pagi,
                           energi_siang=energi_siang, protein_siang=protein_siang,
                           lemak_siang=lemak_siang, karbo_siang=karbo_siang,
                           energi_malam=energi_malam, protein_malam=protein_malam,
                           lemak_malam=lemak_malam, karbo_malam=karbo_malam)
# AKHIR HALAMAN FORM MIFFLIN    
   
   
   
    
    
# HALAMAN FORM PERKENI 
@beranda.route('/perkeni', methods=['GET', 'POST'])
def perkeni_page():
    form = FormPerkeni()
    bb =''
    tb = ''
    umur =''
    gender = ''
    
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
    
    if request.method == 'POST' and 'bb' in request.form and 'tb' in request.form and 'umur' in request.form and 'gender' in request.form  and 'aktivitas' in request.form:
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        gender = request.form.get('gender')
        aktivitas = float(request.form.get('aktivitas'))
        
    if request.form.get('hitung'):
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        gender = request.form.get('gender')
        
        imt = round ((bb /(tb/100)**2),2)
        bbi = round (0.9 * (tb-100),2)
        
        if request.form.get('gender') == 'pria':
            bmr = 30 * bbi
        else:
            bmr = 25 * bbi 
        
        bmr = round(bmr,2)
            
        energi = round((bmr + aktivitas) - faktor_usia, 2)
        protein = round((0.15 * energi)/4, 2)
        lemak = round((0.25 * energi)/9, 2)   
        karbo  = round((0.65 * energi)/4, 2) 
        
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
  
    return render_template('perkeni.html',tittle='PERKENI', 
                           form=form, bb=bb, tb=tb, umur=umur, 
                           gender=gender,imt=imt, bbi=bbi, bmr=bmr, energi=energi, 
                           protein=protein, lemak=lemak, karbo=karbo,
                           energi_pagi=energi_pagi, protein_pagi=protein_pagi,
                           lemak_pagi=lemak_pagi, karbo_pagi=karbo_pagi,
                           energi_siang=energi_siang, protein_siang=protein_siang,
                           lemak_siang=lemak_siang, karbo_siang=karbo_siang,
                           energi_malam=energi_malam, protein_malam=protein_malam,
                           lemak_malam=lemak_malam, karbo_malam=karbo_malam)
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
    
    if request.method == 'POST' and 'bb' in request.form and 'tb' in request.form and 'umur' in request.form and 'trimester' in request.form and 'umurhamil' in request.form  and 'aktivitas' in request.form  and 'tidur' in request.form:
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
        tidur = int(request.form.get('tidur'))
        aktivitas = float(request.form.get('aktivitas'))
        umurhamil = float(request.form.get('umurhamil'))
        trimester = (request.form.get('trimester'))
        
    if request.form.get('hitung'):
        bb = float(request.form.get('bb'))
        tb = float(request.form.get('tb'))
        umur = int(request.form.get('umur'))
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
        
    return render_template('hamil.html', tittle='GIZI IBU HAMIL', 
                           form=form, bb=bb, tb=tb, umur=umur, trimester=trimester, umurhamil=umurhamil, 
                           imt=imt, bbi=bbi, bmr=bmr, energi=energi, 
                           protein=protein, lemak=lemak, karbo=karbo,
                           energi_pagi=energi_pagi, protein_pagi=protein_pagi,
                           lemak_pagi=lemak_pagi, karbo_pagi=karbo_pagi,
                           energi_siang=energi_siang, protein_siang=protein_siang,
                           lemak_siang=lemak_siang, karbo_siang=karbo_siang,
                           energi_malam=energi_malam, protein_malam=protein_malam,
                           lemak_malam=lemak_malam, karbo_malam=karbo_malam,)
# AKHIR HALAMAN FORM IBU HAMIL





# HALAMAN FORM IBU MENYUSUI
@beranda.route('/gizi-ibu-menyusui')
def gizimenyusui_page():
    form = FormMenyusui()
    bb =''
    tb = ''
    umur =''
    gender = ''
    
    imt = ''
    bbi = ''
    bee = ''
    tee = ''
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
    
        
       
    
    return render_template('menyusui.html', tittle='GIZI IBU MENYUSUI',
                           form=form, bb=bb, tb=tb, umur=umur, 
                           gender=gender,imt=imt, bbi=bbi, bmr=bmr, energi=energi, 
                           protein=protein, lemak=lemak, karbo=karbo,
                           energi_pagi=energi_pagi, protein_pagi=protein_pagi,
                           lemak_pagi=lemak_pagi, karbo_pagi=karbo_pagi,
                           energi_siang=energi_siang, protein_siang=protein_siang,
                           lemak_siang=lemak_siang, karbo_siang=karbo_siang,
                           energi_malam=energi_malam, protein_malam=protein_malam,
                           lemak_malam=lemak_malam, karbo_malam=karbo_malam)
# AKHIR HALAMAN FORM IBU MENYUSUI