from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def get_cookie():
    return (DATA_DIR / "cookie.txt").read_text(encoding="utf-8").strip()


