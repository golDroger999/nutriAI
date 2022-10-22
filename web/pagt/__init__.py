from flask import Flask, request, Blueprint
from web.pagt.routes import pagt


pagt_routing = Blueprint('pagt_routing ','__name__')
pagt_routing.register_blueprint(pagt, url_prefix='/')
