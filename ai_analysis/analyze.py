def analyze_results(results):
    if not results:
        return "✅ لا توجد ثغرات حرجة حسب الفحص المبدئي."

    analysis = "🤖 تحليل النتائج:\n"
    for vuln in results:
        analysis += f"""
🔍 النوع: {vuln['vuln']}
🚨 الخطورة: {vuln['severity']}
📄 الوصف: {vuln['description']}
🧪 مثال استغلال: {vuln['poc']}
🛡️ الحل المقترح: {vuln['fix']}
---------------------------
"""
    return analysis
