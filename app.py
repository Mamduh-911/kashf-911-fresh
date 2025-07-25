from flask import Flask, render_template, request
from scanner.scan import run_all_scans
from ai.analyzer import analyze_results

app = Flask(__name__, template_folder='web/templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    scan_result = ''
    ai_result = ''
    if request.method == 'POST':
        target_url = request.form['url']
        scan_result = run_all_scans(target_url)
        ai_result = analyze_results(scan_result)
    return render_template('index.html', result=scan_result, ai_result=ai_result)

if __name__ == '__main__':
    app.run(debug=True)
