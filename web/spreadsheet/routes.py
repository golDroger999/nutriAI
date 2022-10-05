from flask import (render_template, redirect, request, Blueprint, url_for, make_response)
from web.spreadsheet.form import csv_form
from web.spreadsheet.rumusgizi import HitungGiziKelompok as hgk 
import pandas as pd
import numpy as np



sheet = Blueprint('sheet', __name__)


# HALAMAN DASHBOARD CSV
@sheet.route('/gizi-kelompok', methods=['GET', 'POST'])
def csv_page():
    form = csv_form()
    data = ''

    kurus = ''
    ideal = ''
    gemuk = ''
    obesitas = ''
    
    if request.method == 'POST':
        
        try:
            data = pd.read_csv(request.files.get('csv'))
            data = pd.DataFrame(data)
            data['imt'] = (hgk(bb=data['bb'], tb=data['tb'], umur=data['umur'], gender=data['gender']).imt())
            data['status'] =  (hgk(bb=data['bb'], tb=data['tb'], umur=data['umur'], gender=data['gender']).statusgizi())
            data['energi'] = (hgk(bb=data['bb'], tb=data['tb'], umur=data['umur'], gender=data['gender']).energi())
            data['protein'] = (hgk(bb=data['bb'], tb=data['tb'], umur=data['umur'], gender=data['gender']).protein())
            data['lemak'] = (hgk(bb=data['bb'], tb=data['tb'], umur=data['umur'], gender=data['gender']).lemak())
            data['karbo'] = (hgk(bb=data['bb'], tb=data['tb'], umur=data['umur'], gender=data['gender']).karbo())
            data = data.round(0)
            
            kurus = data.loc[data['status']=='kurus']
            ideal = data.loc[data['status']=='ideal']
            gemuk = data.loc[data['status']=='gemuk']
            obesitas = data.loc[data['status']=='obesitas']
            
            print(data)
        
        except:
            return redirect(url_for("sheet.csv_page"))

    return render_template('spreadsheet.html',tittle='GIZI KELOMPOK',form=form, data=data, 
                           kurus=kurus, ideal=ideal, gemuk=gemuk, obesitas=obesitas)
                           
#  AKHIR HALAMAN DASHBOARD CSV

