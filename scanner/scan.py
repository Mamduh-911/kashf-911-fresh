# scan.py

def run_scan(url):
    # هنا مثال بسيط لنتائج وهمية
    return [
        {
            "type": "XSS",
            "url": url,
            "description": "تم اكتشاف ثغرة XSS في المعلمة `q`",
            "poc": f"{url}/?q=<script>alert(1)</script>"
        },
        {
            "type": "SQL Injection",
            "url": url,
            "description": "تم اكتشاف ثغرة SQLi في المعلمة `id`",
            "poc": f"{url}/?id=1' OR '1'='1"
        }
    ]
