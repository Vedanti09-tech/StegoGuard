from flask import Flask
from flask_cors import CORS
from app.routes.upload import upload_bp

app = Flask(__name__)
CORS(app)  # ✅ Enables frontend-backend communication

app.config['UPLOAD_FOLDER'] = 'uploads/'

# Register upload route
app.register_blueprint(upload_bp, url_prefix='/api')

@app.route('/')
def home():
    return "Flask server running ✅"

if __name__ == '__main__':
    app.run(debug=True)
