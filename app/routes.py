from flask import Blueprint, render_template, request, send_from_directory
import os
from . import UPLOAD_FOLDER

bp = Blueprint('routes', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

@bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return 'File uploaded and saved.', 200

@bp.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)
