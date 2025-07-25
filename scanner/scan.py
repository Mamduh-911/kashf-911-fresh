import requests

def scan_xss(url):
    payload = "<script>alert('XSS')</script>"
    test_url = f"{url}?q={payload}"
    res = requests.get(test_url)
    if payload in res.text:
        return {"vuln": "XSS", "url": test_url, "severity": "High"}
    return None

def scan_sql_injection(url):
    payload = "' OR '1'='1"
    test_url = f"{url}?id={payload}"
    res = requests.get(test_url)
    if "sql" in res.text.lower() or "syntax" in res.text.lower():
        return {"vuln": "SQL Injection", "url": test_url, "severity": "Critical"}
    return None

def run_all_scans(target):
    results = []
    for func in [scan_xss, scan_sql_injection]:
        try:
            result = func(target)
            if result:
                results.append(result)
        except Exception as e:
            results.append({"error": str(e)})
    return results
