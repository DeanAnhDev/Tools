from action.updatedata import save_authorization, save_cookie, add_proxy, add_account
from getinfo import choose_account, get_account_golike
from getjob import run_job
from action import testcookie


def menu():
    get_account_golike()
    testcookie.test_cookie()
    print("\n===== MENU =====")
    print("1. Chay tools")
    print("2. Cap nhat authorization Golike")
    print("3. Cap nhat cookie Instagram")
    print("4. Cap nhat proxy")
    print("5. Cap nhat account Instagram lam Golike")
    print("6. Thoát")

while True:
    # clear()  
    menu()
    choice = input("Chọn: ")

    if choice == "1":
        run_job()
    elif choice == "2":
        save_authorization()
    elif choice == "3":
        save_cookie()
    elif choice == "4":
        add_proxy()
    elif choice == "5":
        account_id = choose_account()
        add_account(account_id)
    elif choice == "6":
        print("Thoat chuong trinh!")
        break

    input("\nNhan Enter de tiep tuc...")