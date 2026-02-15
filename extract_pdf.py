import sys

def extract_text(pdf_path):
    try:
        from pypdf import PdfReader
        print("Using pypdf")
    except ImportError:
        try:
            import PyPDF2
            from PyPDF2 import PdfReader
            print("Using PyPDF2")
        except ImportError:
            print("No pypdf or PyPDF2 found")
            return

    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        print(text)
    except Exception as e:
        print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        extract_text(sys.argv[1])
    else:
        print("Usage: python3 extract_pdf.py <pdf_file>")
