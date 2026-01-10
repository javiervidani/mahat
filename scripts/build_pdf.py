#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import sys
from pathlib import Path

def _strip_yaml_front_matter(text: str) -> str:
    """Remove leading YAML front matter (--- block at top) if present.

    Pandoc treats a top-of-file '---' ... '---' block as YAML metadata.
    If the summary contains '---' at the top, it can capture a huge
    portion of the document and cause parse errors. This sanitizes it.
    """
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        # Find closing '---' after the opening
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                # Drop the YAML block and return the remainder
                return "\n".join(lines[i+1:])
        # No closing '---' found; drop the opening line to be safe
        return "\n".join(lines[1:])
    return text

def build_master_with_explanations():
    """Rebuild the master document with all explanations from individual files."""
    
    base_dir = Path(r"c:\Users\$USERNAME\dev\mahat")
    output_file = base_dir / "exam_prep_complete_2024_2025_with_explanations.md"
    
    exam_2024_dir = base_dir / "exam_files"
    exam_2025_dir = base_dir / "exam_files_2025"
    summary_file = base_dir / "summery_for_exam.md"
    
    # Start with summary
    print("📖 Building master document with explanations...")
    with open(summary_file, "r", encoding="utf-8") as f:
        content = _strip_yaml_front_matter(f.read())
    
    content += "\n\n<div style=\"page-break-after: always;\"></div>\n\n"
    content += "# חלק ב׳ – שאלות מבחן 2024 (קיץ תשפ״ד)\n\n"
    content += "## מבנה המבחן 2024\n"
    content += "- **חלק א׳**: 4 מתוך 7 שאלות (12 נק' כל אחת)\n"
    content += "- **חלק ב׳**: 2 מתוך 4 שאלות (15 נק' כל אחת)\n"
    content += "- **חלק ג׳**: 1 מתוך 3 שאלות (22 נק')\n"
    content += "- **סה״כ**: 100 נקודות\n\n---\n\n"
    
    # Add 2024 questions
    print("Adding 2024 questions with explanations...")
    for i in range(1, 15):
        q_file = exam_2024_dir / f"question_{i}.md"
        if q_file.exists():
            with open(q_file, "r", encoding="utf-8") as f:
                q_content = f.read()
            content += f"\n<div style=\"page-break-after: always;\"></div>\n\n"
            content += q_content
            print(f"  ✓ Added 2024 Q{i}")
    
    # Section break
    content += "\n\n<div style=\"page-break-after: always;\"></div>\n\n"
    content += "# חלק ג׳ – שאלות מבחן 2025 (קיץ תשפ״ה)\n\n"
    content += "## מבנה המבחן 2025\n"
    content += "- **חלק א׳**: 3 מתוך 4 שאלות (12 נק' כל אחת)\n"
    content += "- **חלק ב׳**: 2 מתוך 3 שאלות (15 נק' כל אחת)\n"
    content += "- **חלק ג׳**: 2 מתוך 3 שאלות (17 נק' כל אחת)\n"
    content += "- **סה״כ**: 100 נקודות\n\n---\n\n"
    
    # Add 2025 questions
    print("Adding 2025 questions with explanations...")
    for i in range(1, 11):
        q_file = exam_2025_dir / f"question_{i}.md"
        if q_file.exists():
            with open(q_file, "r", encoding="utf-8") as f:
                q_content = f.read()
            content += f"\n<div style=\"page-break-after: always;\"></div>\n\n"
            content += q_content
            print(f"  ✓ Added 2025 Q{i}")
    
    # Add final sections
    content += "\n\n<div style=\"page-break-after: always;\"></div>\n\n"
    content += "# 📋 רשימת ביקורת – לפני המבחן\n\n"
    content += """## ✅ בדוק את הבנתך

- [ ] יכול לכתוב תוכנית Java בסיסית עם `main`?
- [ ] מבין את ההבדל בין `int`, `double`, `String`?
- [ ] יכול לכתוב לולאה `for` ו-`while`?
- [ ] יודע להשתמש בתנאים `if`, `else if`, `else`?
- [ ] יכול לעבוד עם מערכים חד-ממדיים?
- [ ] יכול לעבוד עם מטריצות?
- [ ] מבין את עקרון הרקורסיה?
- [ ] יכול לקרוא ולכתוב סינטקס OOP בסיסי?

## ✅ בדוק את הקוד שלך

- [ ] כל המשתנים מאותחלים?
- [ ] כל סוגריים סגורים?
- [ ] השתמשת ב-`==` (לא `=`)?
- [ ] בדקת תנאים קצה?
- [ ] הדפסות בחוץ מהלולאה (אם צריך)?
- [ ] בדקת עם דוגמה?

---

**מסמך זה מוכן להדפסה וצפייה דיגיטלית.**  
**קיץ תשפ״ה (2025)**
"""
    
    # Write to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"\n✅ Master document created: {output_file}")
    return output_file

def export_to_pdf(md_file):
    """Convert markdown to PDF using Pandoc."""
    
    pdf_file = md_file.with_suffix(".pdf")
    
    print(f"\n📄 Converting to PDF...")
    print(f"   Input:  {md_file}")
    print(f"   Output: {pdf_file}")
    
    try:
        # Check if Pandoc is installed
        result = subprocess.run(
            ["pandoc", "--version"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print("\n⚠️  Pandoc not found!")
            print("   Install with: choco install pandoc  (or brew/apt)")
            return None
        
        # Pick an available PDF engine
        def _is_available(cmd):
            try:
                return subprocess.run([cmd, "--version"], capture_output=True, text=True).returncode == 0
            except Exception:
                return False

        pdf_engine = None
        for engine in ("xelatex", "lualatex", "pdflatex", "wkhtmltopdf", "weasyprint"):
            if _is_available(engine):
                pdf_engine = engine
                break

        if pdf_engine is None:
            print("\n⚠️  No PDF engine found (xelatex/lualatex/pdflatex/wkhtmltopdf/weasyprint).")
            print("   Install MiKTeX (LaTeX) or wkhtmltopdf/weasyprint, then retry.")
            return None

        # Convert to PDF
        cmd = [
            "pandoc",
            "-f", "markdown-yaml_metadata_block",
            str(md_file),
            "-o", str(pdf_file),
            "--pdf-engine", pdf_engine,
            "-V", "lang=he",
            "-V", "mainfont=Arial",
            "-V", "geometry:margin=1in",
            "--toc",
            "--toc-depth=2"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"\n✅ PDF created successfully!")
            print(f"   📁 {pdf_file}")
            return pdf_file
        else:
            print(f"\n❌ Pandoc error:")
            print(result.stderr)
            return None
    
    except FileNotFoundError:
        print("\n⚠️  Pandoc not found on system")
        print("   Install Pandoc from: https://pandoc.org/installing.html")
        return None

if __name__ == "__main__":
    # Build master document
    md_file = build_master_with_explanations()
    
    # Try to export to PDF
    if md_file:
        pdf_file = export_to_pdf(md_file)
        
        if pdf_file:
            print("\n" + "="*60)
            print("🎉 SUCCESS!")
            print("="*60)
            print(f"📘 Markdown: {md_file}")
            print(f"📄 PDF:      {pdf_file}")
            print("\nYour study guide is ready for printing or digital review!")
        else:
            print("\n💡 Markdown file created, but PDF conversion failed.")
            print("   You can still:")
            print(f"   - Open {md_file} in any markdown viewer")
            print(f"   - Print to PDF from browser (using VS Code preview)")
