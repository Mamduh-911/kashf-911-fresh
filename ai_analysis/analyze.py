def explain_vulns(results):
    if not results:
        return "لم يتم اكتشاف أي ثغرات."

    summary = []
    for item in results:
        if 'vuln' in item:
            if item['vuln'] == "XSS":
                summary.append("ثغرة XSS تُمكن المهاجم من تنفيذ كود خبيث في المتصفح.")
            elif item['vuln'] == "SQL Injection":
                summary.append("ثغرة SQL Injection تتيح التلاعب بقواعد البيانات وتنفيذ استعلامات غير مصرح بها.")
        else:
            summary.append("حدث خطأ أثناء الفحص: " + item.get("error", "غير معروف"))
    return " | ".join(summary)
