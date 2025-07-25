def run_scan(url):
    print("[🔍] جاري فحص الرابط:", url)
    
    # نتيجة تجريبية مؤقتة
    return [{
        'type': 'XSS',
        'severity': 'High',
        'description': 'تم اكتشاف إدخال قابل للتنفيذ في الحقول.',
        'payload': '<script>alert(1)</script>'
    }]
