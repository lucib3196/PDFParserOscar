import fitz  # PyMuPDF
from pathlib import Path


def inspect_pdf(pdf_path: str | Path):
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    doc = fitz.open(pdf_path)

    print("=" * 60)
    print(f"PDF Path: {pdf_path}")
    print(f"Number of pages: {len(doc)}")
    print("=" * 60)

    # --- Metadata ---
    print("\n--- Metadata ---")
    for k, v in doc.metadata.items(): # type: ignore
        print(f"{k}: {v}")

    # --- Inspect first page ---
    page = doc[0]
    print("\n--- First Page Info ---")
    print(f"Page size: {page.rect}")
    print(f"Rotation: {page.rotation}")

    # --- Extract text ---
    text = page.get_text()
    print("\n--- First Page Text (first 1000 chars) ---")
    print(text[:1000])

    # --- Images ---
    images = page.get_images(full=True)
    print(f"\nNumber of images on first page: {len(images)}")

    doc.close()


if __name__ == "__main__":
    # 👇 Replace this with your PDF path
    from pathlib import Path
    PDF_PATH = Path("parser/data/example_output.pdf").resolve()

    inspect_pdf(PDF_PATH)
