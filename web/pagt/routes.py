from flask import (render_template, redirect, request, Blueprint, url_for, make_response)



pagt = Blueprint('pagt', __name__)

@pagt.route('/pagt-form')
def pagt_page():
    pass