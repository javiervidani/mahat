#!/usr/bin/env python3
"""
Master utility script for exam file processing
- Extract PDFs (both 2024 and 2025)
- Build master document with all explanations
- Export to PDF
"""

import os
import sys
from pathlib import Path

try:
    import PyPDF2
except ImportError:
    print("PyPDF2 not installed. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    import PyPDF2

def extract_pdf_to_md(pdf_path, output_path):
    """Extract all text from PDF and save to markdown file"""
    try:
        text_content = []
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            
            print(f"Extracting {num_pages} pages from {os.path.basename(pdf_path)}...")
            
            for page_num, page in enumerate(pdf_reader.pages, 1):
                text = page.extract_text()
                text_content.append(f"## Page {page_num}\n\n{text}\n\n")
                print(f"  Page {page_num}/{num_pages} extracted")
        
        # Write to markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"# Extracted from: {os.path.basename(pdf_path)}\n\n")
            f.write(''.join(text_content))
        
        print(f"✓ Saved to {os.path.basename(output_path)}\n")
        return True
        
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return False

def extract_all_pdfs():
    """Extract all exam PDFs (both 2024 and 2025)"""
    base_dir = Path(r"c:\Users\$USERNAME\dev\mahat")
    pdf_dir = base_dir / "pdf"
    markdown_dir = base_dir / "markdown_files"
    
    pdf_files = [
        ("קיץ_2024_א_97104.pdf", "exam_text_2024.md"),
        ("קיץ_2024_א_פתרון_97104.pdf", "solutions_text_2024.md"),
        ("קיץ_2025_א_97104.pdf", "exam_text_2025.md"),
        ("קיץ_2025_א_פתרון_97104.pdf", "solutions_text_2025.md")
    ]
    
    success_count = 0
    
    for pdf_filename, md_filename in pdf_files:
        pdf_path = pdf_dir / pdf_filename
        md_path = markdown_dir / md_filename
        
        if not os.path.exists(pdf_path):
            print(f"Warning: {pdf_filename} not found, skipping...")
            continue
        
        if extract_pdf_to_md(str(pdf_path), str(md_path)):
            success_count += 1
    
    print(f"\nComplete! Extracted {success_count} PDF file(s).")

def build_master_document():
    """Build comprehensive master document with all questions"""
    base_dir = Path(r"c:\Users\$USERNAME\dev\mahat")
    output_file = base_dir / "exam_prep_complete_2024_2025_with_explanations.md"
    
    exam_2024_dir = base_dir / "exam_files"
    exam_2025_dir = base_dir / "exam_files_2025"
    summary_file = base_dir / "markdown_files" / "summery_for_exam.md"
    
    print("📖 Building master document with explanations...")
    
    if summary_file.exists():
        with open(summary_file, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = "# 📘 חוברת הכנה למבחן מה״ט\n\n"
    
    content += "\n\n<div style=\"page-break-after: always;\"></div>\n\n"
    content += "# חלק ב׳ – שאלות מבחן 2024 (קיץ תשפ״ד)\n\n"
    
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
    
    # Write to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"\n✅ Master document created: {output_file}")
    return output_file

def main():
    print("=" * 60)
    print("📚 EXAM FILE PROCESSOR - Master Utility")
    print("=" * 60)
    
    print("\n1️⃣  Extracting PDFs...")
    extract_all_pdfs()
    
    print("\n2️⃣  Building master document...")
    master_file = build_master_document()
    
    print("\n" + "=" * 60)
    print("✨ COMPLETE!")
    print("=" * 60)
    print(f"📁 Master document: {master_file}")
    print("\nYour study guide is ready for review!")

if __name__ == "__main__":
    main()
