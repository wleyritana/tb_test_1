from flask import Blueprint,request,jsonify
from werkzeug.utils import secure_filename
import os,uuid
upload_bp=Blueprint('upload',__name__)
@upload_bp.post('/upload')
def upload():
 files=request.files.getlist('files')
 job=str(uuid.uuid4())
 os.makedirs('uploads',exist_ok=True)
 saved=[]
 for f in files:
  n=secure_filename(f.filename)
  f.save(os.path.join('uploads',n))
  saved.append(n)
 return jsonify({'job_id':job,'files':saved})