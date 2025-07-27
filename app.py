from flask import Flask, render_template, request
import requests

app = Flask(__name__)

VPS_API_URL = "https://kashf-vps.onrender.com/scan"  # تأكد من الرابط

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            try:
                response = requests.post(VPS_API_URL, json={"url": url})
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text}")
                if response.status_code == 200:
                    result = response.json()
                else:
                    error = f"فشل الاتصال بالسيرفر الخارجي: {response.status_code}"
            except Exception as e:
                error = f"خطأ أثناء الاتصال بالسيرفر: {str(e)}"
    return render_template("index.html", result=result, error=error)
