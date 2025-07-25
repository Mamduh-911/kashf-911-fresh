# scan.py

import subprocess
import tempfile
import os

def run_dalfox(url):
    try:
        result = subprocess.check_output(
            ["dalfox", "url", url], stderr=subprocess.STDOUT, timeout=30
        ).decode()
        return [{
            "type": "XSS",
            "url": url,
            "description": "Dalfox وجد نتيجة.",
            "poc": result.strip().split("\n")[0]
        }]
    except Exception as e:
        return [{"type": "XSS", "url": url, "description": str(e), "poc": "N/A"}]

def run_sqlmap(url):
    try:
        with tempfile.NamedTemporaryFile(delete=False, mode='w') as f:
            f.write(url)
            target_file = f.name

        result = subprocess.check_output(
            ["sqlmap", "-u", url, "--batch", "--level=1", "--risk=1", "--crawl=1", "--output-dir=/tmp"],
            stderr=subprocess.STDOUT,
            timeout=60
        ).decode()
        return [{
            "type": "SQL Injection",
            "url": url,
            "description": "sqlmap وجد نتيجة.",
            "poc": result[:300]  # نعرض أول 300 حرف فقط
        }]
    except Exception as e:
        return [{"type": "SQL Injection", "url": url, "description": str(e), "poc": "N/A"}]

def run_nuclei(url):
    try:
        result = subprocess.check_output(
            ["nuclei", "-u", url],
            stderr=subprocess.STDOUT,
            timeout=30
        ).decode()
        return [{
            "type": "Nuclei Scan",
            "url": url,
            "description": "Nuclei تقرير مفصل.",
            "poc": result.strip().split("\n")[0]
        }]
    except Exception as e:
        return [{"type": "Nuclei", "url": url, "description": str(e), "poc": "N/A"}]

def run_scan(url):
    results = []
    results += run_dalfox(url)
    results += run_sqlmap(url)
    results += run_nuclei(url)
    return results
