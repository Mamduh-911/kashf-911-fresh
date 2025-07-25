# ai/analyzer.py

def analyze_results(vulnerabilities):
    analysis = []
    for vuln in vulnerabilities:
        severity = "🔴 عالية" if "SQL" in vuln["type"] or "XSS" in vuln["type"] else "🟡 متوسطة"
        suggestion = "استخدم فلترة المدخلات." if "XSS" in vuln["type"] else "استخدم استعلامات معدّة مسبقًا."
        analysis.append({
            "type": vuln["type"],
            "url": vuln["url"],
            "severity": severity,
            "description": vuln.get("description", "لم يتم تقديم وصف."),
            "suggestion": suggestion,
            "poc": vuln.get("poc", "غير متوفّر.")
        })
    return analysis
