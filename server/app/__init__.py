from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['UPLOAD_FOLDER'] = 'uploads/'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/stegoguard'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Import routes and register
    from app.routes.upload import upload_bp
    app.register_blueprint(upload_bp, url_prefix='/api')

    # DB models
    from app.models import UploadedImage
    with app.app_context():
        db.create_all()

    return app