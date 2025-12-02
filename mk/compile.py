import os
import re
import markdown
from weasyprint import HTML, CSS
import shutil

# Root dir
SOURCE_DIR = "."
# PDF output dir
OUTPUT_DIR = "dist"
# Ignore dir
IGNORE_DIRS = {".git", ".github", "mk", "dist"}
# Ignore File
IGNORE_FILES = {"README.md", "ref.md", "LICENSE"}

# CSS config for "compile" markdown
# Added styles for centered images/captions and specific alerts
PDF_CSS = CSS(string="""
    @page { size: A4; margin: 2cm; }
    body { font-family: "Noto Sans CJK SC", "Microsoft YaHei", sans-serif; font-size: 14px; line-height: 1.6; }
    h1, h2, h3 { color: #333; }
    
    /* Image handling */
    img { max-width: 100%; height: auto; display: block; margin: 1em auto; }
    
    /* Support for <p align="center"> legacy HTML */
    p[align="center"] { text-align: center; }
    
    /* Code blocks */
    code { background-color: #f4f4f4; padding: 2px 4px; border-radius: 4px; font-family: monospace; }
    pre { background-color: #f4f4f4; padding: 1em; border-radius: 4px; overflow-x: auto; }
    
    /* Custom style for "!" code blocks (converted to class .warning) */
    pre.warning { 
        background-color: #fff3cd; 
        border: 1px solid #ffeeba; 
        border-left: 5px solid #ffc107;
    }
    
    blockquote { border-left: 4px solid #ddd; padding-left: 1em; color: #666; }
    table { border-collapse: collapse; width: 100%; margin: 1em 0; }
    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
    th { background-color: #f2f2f2; }
""")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def preprocess_markdown(text):
    """
    Pre-process markdown text to handle non-standard syntax.
    """
    # Replace ```! with ```text (or a custom class if we use attr_list, 
    # but here we simply handle it by replacing it with a recognizable pattern 
    # or just treating it as text to avoid parser errors).
    # Strategy: Replace ```! with ```text, but maybe wrap it or mark it?
    # For simplicity and robustness: Let's treat ```! as a warning block.
    # We replace ```! with ```text and inject a warning marker, 
    # OR we can use a specific language identifier if we had a custom highlighter.
    # 
    # Better approach: Replace ```! with ```text
    # If you want specific styling, Python-Markdown's fenced_code allows {.class} syntax.
    # So we replace ```! with ```text {.warning}
    
    # Regex to find ```! and replace with ```text {.warning}
    # This requires the 'attr_list' extension to work perfectly with fenced_code 
    # or just rely on the fact that fenced_code might put the class on the pre/code tag.
    # Actually, standard fenced_code in python-markdown supports ```lang
    # Let's just map ```! to ```text. 
    # If we want styling, we can try ```text\n<div class="warning">...</div> (too complex).
    
    # Simple fix: Replace ```! with ```text
    text = re.sub(r'^```!$', '```text', text, flags=re.MULTILINE)
    
    return text

def convert_md_to_pdf(file_path, output_path, base_path):
    """
    Convert a single MD file to PDF
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        # 0. Pre-process text
        text = preprocess_markdown(text)

        # 1. Markdown -> HTML
        # 'md_in_html': Allow markdown syntax inside HTML blocks (optional but good)
        # 'tables', 'fenced_code': Standard requirements
        # 'attr_list': Allows defining attributes like {: .myclass}
        html_body = markdown.markdown(
            text, 
            extensions=['tables', 'fenced_code', 'md_in_html', 'attr_list']
        )

        # 2. HTML Struct
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                /* Inject some base styles directly just in case */
                img {{ max-width: 100%; }}
            </style>
        </head>
        <body>
        {html_body}
        </body>
        </html>
        """

        # 3. HTML -> PDF
        # base_url is critical for relative image paths (src="pic/foo.png")
        HTML(string=html_content, base_url=base_path).write_pdf(output_path, stylesheets=[PDF_CSS])
        
        print(f"[Success] Generated: {output_path}")
        return True
    except Exception as e:
        print(f"[Error] Failed to convert {file_path}: {e}")
        return False

def main():
    # Clean and rebuild the output directory
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    ensure_dir(OUTPUT_DIR)

    print("Starting PDF compilation...")

    # Traversing the directory
    for root, dirs, files in os.walk(SOURCE_DIR):
        # Filter out directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            if file.endswith(".md") and file not in IGNORE_FILES:
                
                source_path = os.path.join(root, file)
                rel_path = os.path.relpath(root, SOURCE_DIR)
                
                target_dir = os.path.join(OUTPUT_DIR, rel_path)
                ensure_dir(target_dir)
                
                pdf_filename = os.path.splitext(file)[0] + ".pdf"
                target_path = os.path.join(target_dir, pdf_filename)

                convert_md_to_pdf(source_path, target_path, root)

    print("Compilation finished.")

if __name__ == "__main__":
    main()