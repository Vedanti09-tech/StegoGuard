from flask import Blueprint, request, jsonify
import os

upload_bp = Blueprint('upload', __name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'server', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@upload_bp.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    try:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        # ✅ FilePond expects a plain string or {id: ...}
        return file.filename, 200
    except Exception as e:
        return f"Upload failed: {str(e)}", 500
