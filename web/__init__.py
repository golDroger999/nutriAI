from flask import Flask

app = Flask('__name__', template_folder='web/templates', static_folder='web/static')
app.config['SECRET_KEY']='denutridash'


from web.userpage.routes import user
from web.adminpage.routes import admin

app.register_blueprint(user)
app.register_blueprint(admin)
