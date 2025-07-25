def run_all_scans(url):
    results = []

    # محاكاة فحص SQLi
    if "id=" in url:
        results.append({
            "vuln": "SQL Injection",
            "severity": "High",
            "description": "الموقع يحتوي على مدخل vulnerable إلى حقن استعلامات SQL.",
            "poc": f"{url}' OR 1=1 --",
            "fix": "استخدم استعلامات محمية (prepared statements)."
        })

    # محاكاة فحص XSS
    if "search=" in url:
        results.append({
            "vuln": "XSS",
            "severity": "Medium",
            "description": "يمكن تنفيذ كود جافا سكربت داخل صفحة الموقع.",
            "poc": f"{url}<script>alert('XSS')</script>",
            "fix": "استخدم فلترة المدخلات وتشفير الإخراج."
        })

    return results
