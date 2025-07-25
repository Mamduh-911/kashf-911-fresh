from flask import Flask, render_template, request
from scanner.scan import run_scan  # تم تعديل الاستيراد

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        url = request.form['url']
        results = run_scan(url)  # تم تعديل اسم الدالة
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
