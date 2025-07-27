from flask import Blueprint, request, jsonify
import os
from app import db
from app.models import UploadedImage

upload_bp = Blueprint('upload', __name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'server', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@upload_bp.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Save metadata to DB
        record = UploadedImage(filename=file.filename)
        db.session.add(record)
        db.session.commit()

        return jsonify({'message': f'File uploaded ✅: {file.filename}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500