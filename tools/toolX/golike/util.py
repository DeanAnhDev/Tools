import time
import random
import os
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def human_sleep():
    t = random.choice([
        random.uniform(1, 2),   # nhanh
        random.uniform(2, 4),   # bình thường
        random.uniform(5, 8)    # chậm
    ])
    time.sleep(t)

def job_complete_sleep():
    t = random.choice([
        random.uniform(40, 50),   # nhanh
        random.uniform(50, 60),   # bình thường
        random.uniform(60, 70)    # chậm
    ])
    time.sleep(t)

def job_sleep():
    t = random.choice([
        random.uniform(15, 20),   # nhanh
        random.uniform(20, 30),   # bình thường
        random.uniform(30, 40)    # chậm
    ])
    time.sleep(t)

def get_authorization():
    return (DATA_DIR / "authorization.txt").read_text(encoding="utf-8").strip()

def get_account_id():
    return (DATA_DIR / "xaccount.txt").read_text(encoding="utf-8").strip()

