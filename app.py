from flask import Flask, render_template, request
import requests

app = Flask(__name__)

VPS_API_URL = "https://kashf-vps.onrender.com/scan"  # تأكد إنه هذا رابطك الصحيح

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            try:
                response = requests.post(VPS_API_URL, json={"url": url})
                if response.status_code == 200:
                    result = response.json()
                else:
                    result = {"error": "فشل في الاتصال بالسيرفر الخارجي"}
            except Exception as e:
                result = {"error": str(e)}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
