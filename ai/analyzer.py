# ai/analyzer.py

def analyze_results(vulnerabilities):
    # تحليل بسيط باستخدام الذكاء الصناعي (نسخة أولية)
    summary = "🤖 تحليل النتائج:\n"
    for vuln in vulnerabilities:
        severity = vuln.get("severity", "غير محدد")
        summary += f"- النوع: {vuln.get('type', 'غير معروف')} | الخطورة: {severity}\n"
    return summary
