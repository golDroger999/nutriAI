from flask import (render_template, redirect, request, Blueprint, url_for, make_response)
from web.spreadsheet.form import csv_form
import pandas as pd
import numpy as np



sheet = Blueprint('sheet', __name__)


# HALAMAN DASHBOARD CSV
@sheet.route('/gizi-kelompok', methods=['GET', 'POST'])
def csv_page():
    form = csv_form()
    data = ''
    if request.method == 'POST':
        data = pd.read_csv(request.files.get('csv'))
        data = pd.DataFrame(data)
        print(data)
    return render_template('spreadsheet.html',title='GIZI KELOMPOK',form=form, data=data)
#  AKHIR HALAMAN DASHBOARD CSV

