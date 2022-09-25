from flask import (render_template, redirect, request, Blueprint, url_for, make_response)
from web.spreadsheet.form import csv_form
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
import os


sheet = Blueprint('sheet', __name__)




# HALAMAN DASHBOARD CSV
@sheet.route('/gizi-kelompok', methods=['GET', 'POST'])
def csv_page():
    form = csv_form()
    return render_template('spreadsheet.html',form=form)
#  AKHIR HALAMAN DASHBOARD CSV

