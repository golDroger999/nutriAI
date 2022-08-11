from flask import (render_template, redirect, Request, Blueprint, url_for)
from web.userpage.form import (FormDubois, FormHarrisBenneedict)


user = Blueprint('user', __name__)

@user.route('/')
@user.route('/beranda')
def beranda():
    return render_template('beranda.html')


@user.route('/alat-analisis')
def analisis():
    return render_template('alat_analisis.html')


@user.route('/user-dashboard')
def dashboard_user():
    return render_template('dashboard.html')


