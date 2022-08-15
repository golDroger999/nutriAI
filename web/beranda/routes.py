from flask import (render_template, redirect, Request, Blueprint, url_for)
from web.beranda.form import (FormDubois, FormHarrisBenneedict, FormMifflin)
 


beranda = Blueprint('beranda', __name__)

@beranda.route('/beranda')
@beranda.route('/')
def beranda_page():
    return render_template('beranda.html', tittle='NUTRIECY')


@beranda.route('/alat-analisis')
def analisis_page():
    return render_template('alat_analisis.html', tittle='ANALISIS GIZI')


@beranda.route('/dashboard-page')
def dashboard_page():
    return render_template('dashboard.html', tittle='DASHBOARD')


@beranda.route('/dubois')
def dubois_page():
    form = FormDubois() 
    return render_template('dubois.html', form=form, tittle='DUBOIS')


@beranda.route('/harris-bennedict')
def harris_bennedict_page():
    form = FormHarrisBenneedict() 
    return render_template('harris.html', form=form, tittle='HARRIS BENNEDICT')


@beranda.route('/mifflin')
def mifflin_page():
    form = FormMifflin()
    return render_template('mifflin.html', form=form, tittle='MIFFLIN')