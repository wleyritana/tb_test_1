from flask import Blueprint,jsonify
analyze_bp=Blueprint("analyze",__name__)
@analyze_bp.post("/analyze")
def analyze(): return jsonify({"pipeline":"ocr->pii->grounding->analysis->verification"})
