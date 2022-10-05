from flask import (render_template, redirect, Request, Blueprint)
from web.scanform.form import document


scanner = Blueprint('scanner', __name__)


@scanner.route('/scan-form', methods=['GET', 'POST'])
def scanner_page():
    form = document()
    return render_template('scanner_form.html', tittle='SCANNER FORMULIR', form=form) 
