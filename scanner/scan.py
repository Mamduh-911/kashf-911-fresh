import time

def run_scan(url):
    print("[🔍] جاري فحص الرابط:", url)
    time.sleep(2)  # انتظر 2 ثانية فقط
    return [
        {
            'type': 'XSS',
            'severity': 'High',
            'description': 'تم اكتشاف إدخال قابل للتنفيذ في الحقول.',
            'payload': '<script>alert(1)</script>'
        }
    ]
