from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
upload_bp=Blueprint('upload',__name__)
@upload_bp.route('/upload',methods=['POST'])
def upload():
    files=request.files.getlist('files')
    saved=[]
    os.makedirs('uploads',exist_ok=True)
    for f in files:
        name=secure_filename(f.filename)
        path=os.path.join('uploads',name)
        f.save(path)
        saved.append(name)
    return jsonify({'files':saved})
