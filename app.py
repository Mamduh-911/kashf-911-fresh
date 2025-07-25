from flask import Flask, request, render_template
from scanner.scan import run_all_scans
from ai_analysis.analyze import explain_vulns

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    explanation = ""
    if request.method == 'POST':
        url = request.form['url']
        results = run_all_scans(url)
        explanation = explain_vulns(results)
    return render_template('index.html', results=results, explanation=explanation)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
