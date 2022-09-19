from flask import (render_template, redirect, request, Blueprint, url_for, make_response)
from web.spreadsheet.form import csv_form
import pandas as pd
import numpy as np

sheet = Blueprint('sheet', __name__)




# HALAMAN DASHBOARD CSV
@sheet.route('/csv-tools', methods=['GET', 'POST'])
def csv_page():
    form = csv_form()
    return render_template('spreadsheet.html', form=form)
#  AKHIR HALAMAN DASHBOARD CSV






# HALAMAN DASHBOARD CSV
@sheet.route('/gizi-kelompok', methods=['GET', 'POST'])
def excel_page():
    form = csv_form()
    return render_template('spreadsheet.html', title='GIZI KELOMPOK', form=form)
#  AKHIR HALAMAN DASHBOARD CSV