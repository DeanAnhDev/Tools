from curl_cffi import requests
from golike.util import human_sleep, get_authorization


authorization = get_authorization()

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': authorization,
    'content-type': 'application/json;charset=utf-8',
    'origin': 'https://app.golike.net',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    't': 'VFZSak0wMTZZM2xQUkZsNVRtYzlQUT09',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36',
    }

session = requests.Session(impersonate="chrome120")

def get_account_golike():

    response = session.get('https://gateway.golike.net/api/users/me', headers=headers).json()

    account_id = response['data']['id']
    account_name = response['data']['name']
    coin = response['data']['coin']
    print(f"Account ID: {account_id} | Name: {account_name} | Coin: {coin}")
    
human_sleep()

def get_account_X_in_golike():
    response = session.get(
        'https://gateway.golike.net/api/twitter-account',
        headers=headers
    )

    accounts = []  # list để chứa account

    for acc in response["data"]:
        account_info = {
            "id": acc["id"],
            "screen_name": acc["screen_name"],
            "twitter_id": acc["twitter_id"]
        }
        accounts.append(account_info)

    return accounts

def choose_account():
    list_acc = get_account_X_in_golike()

    # In danh sách
    for i, acc in enumerate(list_acc, start=1):
        print(f"{i}. {acc['screen_name']} | ID: {acc['id']}")

    # Nhập lựa chọn
    while True:
        try:
            choice = int(input("Chọn account (nhập số): "))
            if 1 <= choice <= len(list_acc):
                selected_acc = list_acc[choice - 1]
                return selected_acc["id"]
            else:
                print(" Số không hợp lệ, nhập lại!")
        except ValueError:
            print(" Vui lòng nhập số!")