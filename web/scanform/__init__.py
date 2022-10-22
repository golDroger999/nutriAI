from flask import Flask, request, Blueprint
from web.scanform.routes import scanner


scanner_routing = Blueprint('scanner_routing ','__name__')
scanner_routing.register_blueprint(scanner, url_prefix='/')
