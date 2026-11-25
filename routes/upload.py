from flask import Blueprint,request,jsonify
upload_bp=Blueprint("upload",__name__)
@upload_bp.post("/upload")
def upload(): return jsonify({"status":"uploaded"})
