from pathlib import Path


def read_text_file(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"{path} not found")
    return file_path.read_text(encoding="utf-8")


def write_text_file(path: str, content: str):
    file_path = Path(path)
    file_path.write_text(content, encoding="utf-8")
