from flask import Blueprint,request,jsonify
from services.pdf_service import extract_pdf_text
analyze_bp=Blueprint('analyze',__name__)
@analyze_bp.post('/analyze')
def analyze():
 data=request.json or {}
 return jsonify({'summary':'Demo analysis pipeline ready','findings':[{'title':'File processed','confidence':100}]})