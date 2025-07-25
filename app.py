from flask import Flask, render_template, request
from scan import run_scan
from ai.analyzer import analyze_results
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_target():
    url = request.form.get('url')
    if not url:
        return render_template("index.html", error="❌ يرجى إدخال رابط.")
    
    raw_results = run_scan(url)
    analyzed = analyze_results(raw_results)
    
    return render_template("index.html", results=analyzed, target=url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # يستخدم البورت الصحيح لـ Render
    app.run(host="0.0.0.0", port=port)  # ربط التطبيق على 0.0.0.0 لتجنب مشكلة Render
