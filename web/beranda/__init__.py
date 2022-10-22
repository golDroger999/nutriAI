from flask import Flask, request, Blueprint
from web.beranda.routes import beranda


beranda_routing = Blueprint('beranda_routing','__name__')
beranda_routing.register_blueprint(beranda, url_prefix='/')
