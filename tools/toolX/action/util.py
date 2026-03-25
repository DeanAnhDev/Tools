from pathlib import Path
import time
import random
import os

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def _sleep_with_countdown(duration):
    remaining = max(0, int(round(duration)))
    while remaining > 0:
        print(f"\r⏳ Chờ {remaining}s...", end="", flush=True)
        time.sleep(1)
        remaining -= 1
    print("\r✅ Tiếp tục...     ")

def get_cookie():
    return (DATA_DIR / "cookie.txt").read_text(encoding="utf-8").strip()

def human_sleep():
    t = random.choice([
        random.uniform(1, 2),   # nhanh
        random.uniform(2, 4),   # bình thường
        random.uniform(5, 8)    # chậm
    ])
    _sleep_with_countdown(t)
