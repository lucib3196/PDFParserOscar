from pathlib import Path


if __name__ == "__main__":
    path = r"parser\data.txt"
    content = Path(path).read_text()
    print("Reading text file\n", content)
