from curl_cffi import requests

from action.util import get_cookie
cookie_string = get_cookie()
cookies = dict(item.split("=", 1) for item in cookie_string.split("; "))

csrftoken = cookies["csrftoken"]

print("csrftoken:", csrftoken)

def get_header( cookie_string, csrftoken, referer):
    headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': referer,
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    'sec-ch-ua-full-version-list': '"Chromium";v="146.0.7680.154", "Not-A.Brand";v="24.0.0.0", "Google Chrome";v="146.0.7680.154"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"6.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36',
    'x-asbd-id': '359341',
    'x-csrftoken': csrftoken,
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR30E-Lpvb2GtLinOr0zq6Rjq392LSiu0pgCF2VqaSMu4Qnv',
    'x-instagram-ajax': '1035828954',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-session-id': 'atv8tk:9skufs:u8zmyl',
    'cookie': cookie_string,
    }
    return headers

session = requests.Session(impersonate="chrome120")
def like_ig(tweet_id, session, link):

    headers = get_header(
    cookie_string,
    csrftoken,
    link,
)
    json_data = {
        "variables": {
            "tweet_id": tweet_id
        },
        "queryId": "lI07N6Otwv1PhnEgXILM7A"
    }

    r = session.post(
        "https://x.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet",
        headers=headers,
        json=json_data
    )

    if r.status_code == 200:
              return True
    else:              
              return False



 


