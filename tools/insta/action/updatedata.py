from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def save_authorization():
    auth = input("Nhập authorization Golike: ")
    with open(DATA_DIR / "authorization.txt", "w", encoding="utf-8") as f:
        f.write(auth)
    print("Đã lưu authorization!")

def save_cookie():
    cookie = input("Nhập cookie: ")
    with open(DATA_DIR / "cookie.txt", "w", encoding="utf-8") as f:
        f.write(cookie)
    print("Đã lưu cookie!")

def add_proxy():
    proxy = input("Nhập proxy (ip:port hoặc user:pass@ip:port): ")

    with open(DATA_DIR / "proxy.txt", "a", encoding="utf-8") as f:
        f.write(proxy + "\n")

    print("Đã lưu proxy!")

def add_account(account):
    with open(DATA_DIR / "xaccount.txt", "w", encoding="utf-8") as f:
        f.write(str(account))
    print("Đã lưu account X!")