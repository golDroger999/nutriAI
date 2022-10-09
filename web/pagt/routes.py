from flask import (render_template, redirect, request, Blueprint, url_for, make_response)
from web.pagt.form import pagtform


pagt = Blueprint('pagt', __name__)

@pagt.route('/pagt-form')
def pagt_page():
    form = pagtform()
    
    # Antropometri handel
    
    # Biokimia Handel
    
    # Fisik Klinis Handel
    
    # Riwayat Personal Handel
    
    # Diagnosis Handel
    
    # Intervensi Handel
    
    # Rencana Monev Handel
    return render_template('pagt.html', tittle='PAGT FORM', form=form)