from flask import (render_template, redirect, Request, Blueprint, url_for)
from web.beranda.form import (FormDubois, FormHarrisBenneedict, FormMifflin)


beranda = Blueprint('beranda', __name__)

@beranda.route('/beranda')
@beranda.route('/')
def beranda_page():
    return render_template('beranda.html')


@beranda.route('/alat-analisis')
def analisis_page():
    return render_template('alat_analisis.html')


@beranda.route('/dashboard-page')
def dashboard_page():
    return render_template('dashboard.html')


@beranda.route('/dubois')
def dubois_page():
    form = FormDubois() 
    return render_template('dubois.html', form=form )


@beranda.route('/harris-bennedict')
def harris_bennedict_page():
    form = FormHarrisBenneedict() 
    return render_template('harris.html', form=form)


@beranda.route('/mifflin')
def mifflin_page():
    form = FormMifflin()
    return render_template('mifflin.html', form=form)