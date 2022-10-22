from flask import Flask, request
    
def create_app():
    app = Flask('__name__', template_folder='web/templates', static_folder='web/static')
    app.config['SECRET_KEY']='denutridash'
    

    from web.beranda import beranda_routing
    from web.scanform import scanner_routing
    from web.spreadsheet import spreadsheet_routing
    from web.pagt import pagt_routing

    app.register_blueprint(beranda_routing)
    app.register_blueprint(scanner_routing)
    app.register_blueprint(spreadsheet_routing)
    app.register_blueprint(pagt_routing)
    
    return app
