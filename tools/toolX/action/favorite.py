from curl_cffi import requests

from action.util import get_cookie
cookie_string = get_cookie()
cookies = dict(item.split("=", 1) for item in cookie_string.split("; "))

ct0 = cookies["ct0"]
authorization = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

print(ct0)


def get_header(authorization, cookie_string, ct0, referer):
   headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': authorization,
    'content-type': 'application/json',
    'origin': 'https://x.com',
    'priority': 'u=1, i',
    'referer': referer,
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-arch': '""',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"145.0.7632.160"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Google Chrome";v="145.0.7632.160", "Chromium";v="145.0.7632.160"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"6.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36',
    'x-client-transaction-id': '6w4FT50nVgUUNNl9hBflfqmsMWw/GU9sCzWCx+rEzchPRGVByBF0xIakzPhgtTrBP32mjO6d5yQ2Wc5Wx96ZPKZj/rqy6A',
    'x-csrf-token': ct0,
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
    'cookie': cookie_string,
    } 
   return headers

session = requests.Session(impersonate="chrome120")
def like_tweet(tweet_id, session, link):

    headers = get_header(
    authorization,
    cookie_string,
    ct0,
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

    print(tweet_id, r.status_code)
    print(r.text)



 


