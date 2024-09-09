from flask import Flask
from .views import views
from .auth import auth

# create a flask application and return it
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']=='deadpoolandwolverine' # encrypt cookies and session data
    
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    
    return app