from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_debugtoolbar import DebugToolbarExtension

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
toolbar = DebugToolbarExtension()

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    toolbar.init_app(app)

    from app.views.dashboard import dashboard
    app.register_blueprint(dashboard)

    from app.views.authentication import auth
    app.register_blueprint(auth, url_prefix='/auth')

    from app.views.cdr import cdr
    app.register_blueprint(cdr, url_prefix="/cdr")
    # @app.route('/')
    # def index():
    #     return "alochym"

    return app

