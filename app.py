from flask import Flask,render_template
from routes.upload import upload_bp
from routes.analyze import analyze_bp
app=Flask(__name__)
app.register_blueprint(upload_bp,url_prefix='/api')
app.register_blueprint(analyze_bp,url_prefix='/api')
@app.get('/')
def home(): return render_template('index.html')
@app.get('/health')
def health(): return {'status':'healthy'}
