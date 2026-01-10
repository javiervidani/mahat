import os
import sys
import os
import sys
from markdown import markdown

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
MASTER_MD = os.path.join(ROOT, "exam_prep_complete_2024_2025_with_explanations.md")
OUTPUT_DIR = os.path.join(ROOT, "exported_books")
CSS_PATH = os.path.join(OUTPUT_DIR, "print.css")
OUTPUT_HTML = os.path.join(OUTPUT_DIR, "exam_prep_complete_2024_2025_with_explanations.html")

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def ensure_css():
    if not os.path.exists(CSS_PATH):
        css = """
        /* Print-friendly stylesheet */
        :root { --text: #111; --muted: #555; --accent: #0b5fff; }
        html { font-size: 12px; }
        body { margin: 1.2cm; color: var(--text); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, 'Noto Sans', 'Helvetica Neue', sans-serif; line-height: 1.6; }
        @page { size: A4; margin: 1.5cm; }
        h1, h2, h3, h4, h5 { color: var(--text); margin: 0.6em 0 0.3em; }
        h1 { font-size: 1.2rem; }
        h2 { font-size: 1.05rem; border-bottom: 1px solid #ddd; padding-bottom: 0.2em; }
        h3 { font-size: 0.95rem; }
        p, li { font-size: 1rem; }
        a { color: var(--accent); text-decoration: none; }
        a:hover { text-decoration: underline; }
        code, pre { font-family: Consolas, 'SFMono-Regular', Menlo, Monaco, 'Liberation Mono', 'Courier New', monospace; }
        pre { background: #f6f8fa; padding: 0.8em; border-radius: 6px; overflow: auto; }
        table { border-collapse: collapse; width: 100%; margin: 1em 0; }
        th, td { border: 1px solid #ddd; padding: 0.5em; }
        th { background: #f2f2f2; }
        nav#TOC { border: 1px solid #e5e5e5; padding: 0.8em; border-radius: 6px; background: #fafafa; }
        nav#TOC ul { list-style: none; padding-left: 0; }
        nav#TOC li { margin: 0.25em 0; }
        .page-break { page-break-before: always; }
        /* Optional RTL support: uncomment if needed */
        /* body { direction: rtl; } */
        """
        with open(CSS_PATH, "w", encoding="utf-8") as f:
            f.write(css)

def export_html():
    if not os.path.exists(MASTER_MD):
        print(f"ERROR: Master Markdown not found: {MASTER_MD}")
        print("Create it first (via your existing build scripts), then rerun.")
        sys.exit(1)

    ensure_output_dir()
    ensure_css()

    with open(MASTER_MD, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_body = markdown(md_content, extensions=["extra", "tables", "toc", "sane_lists"])

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Exam Prep 2024–2025 (With Explanations)</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="print.css">
</head>
<body>
<nav style="text-align:right; margin-bottom:1em; font-size:0.95em;">
  <a href="../exam_prep_complete_2024_2025_with_explanations.md" target="_blank">Download raw Markdown</a>
</nav>
{html_body}
</body>
</html>'''

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    size_kb = os.path.getsize(OUTPUT_HTML) // 1024
    print(f"\nSuccess: {OUTPUT_HTML} ({size_kb} KB)")
    print("Open in your browser and use Print for PDF.")

