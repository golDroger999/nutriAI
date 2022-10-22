from flask import Flask, request, Blueprint
from web.spreadsheet.routes import sheet


spreadsheet_routing = Blueprint('spreadsheet_routing','__name__')
spreadsheet_routing.register_blueprint(sheet, url_prefix='/')
