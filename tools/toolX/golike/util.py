import time
import random
import os
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _sleep_with_countdown(duration):
    remaining = max(0, int(round(duration)))
    while remaining > 0:
        print(f"\r⏳ Chờ {remaining}s...", end="", flush=True)
        time.sleep(1)
        remaining -= 1
    print("\r✅ Tiếp tục...     ")

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def human_sleep():
    t = random.choice([
        random.uniform(1, 2),   # nhanh
        random.uniform(2, 4),   # bình thường
        random.uniform(5, 8)    # chậm
    ])
    _sleep_with_countdown(t)

def job_complete_sleep():
    t = random.choice([
        random.uniform(40, 50),   # nhanh
        random.uniform(50, 60),   # bình thường
        random.uniform(60, 70)    # chậm
    ])
    _sleep_with_countdown(t)

def job_sleep():
    t = random.choice([
        random.uniform(15, 20),   # nhanh
        random.uniform(20, 30),   # bình thường
        random.uniform(30, 40)    # chậm
    ])
    _sleep_with_countdown(t)

def get_authorization():
    return (DATA_DIR / "authorization.txt").read_text(encoding="utf-8").strip()

def get_account_id():
    return (DATA_DIR / "xaccount.txt").read_text(encoding="utf-8").strip()

