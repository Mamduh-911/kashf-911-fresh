# ai/analyzer.py

def analyze_results(vulnerabilities):
    # تحليل النتائج بالذكاء الصناعي (بشكل بسيط حالياً)
    summary = "🤖 تحليل ذكاء صناعي:\n"
    for vuln in vulnerabilities:
        severity = vuln.get("severity", "N/A")
        summary += f"- الثغرة: {vuln.get('type', 'غير معروف')} | الخطورة: {severity}\n"
    return summary
