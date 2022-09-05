from flask import Flask

app = Flask('__name__', template_folder='web/templates', static_folder='web/static')
app.config['SECRET_KEY']='denutridash'

from web.beranda.routes import beranda
from web.adminpage.routes import admin
from web.spreadsheet.routes import sheet

app.register_blueprint(beranda)
app.register_blueprint(admin)
app.register_blueprint(sheet)
