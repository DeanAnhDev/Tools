from curl_cffi import requests
from action.util import get_cookie
cookie_string = get_cookie()
cookies = dict(item.split("=", 1) for item in cookie_string.split("; "))

ct0 = cookies["ct0"]

authorization = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

def get_header(authorization, cookie_string, ct0, referer):
    headers = {
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Google Chrome";v="145.0.7632.160", "Chromium";v="145.0.7632.160"',
    'sec-ch-ua-platform': '"Android"',
    'authorization': authorization,
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-mobile': '?1',
    'x-twitter-active-user': 'yes',
    'sec-ch-ua-arch': '""',
    'sec-ch-ua-full-version': '"145.0.7632.160"',
    'content-type': 'application/x-www-form-urlencoded',
    'x-csrf-token': ct0,
    'Referer': referer,
    'x-twitter-client-language': 'en',
    'x-client-transaction-id': 'RSMoNggLJ9i2Py9qgD3+MD/cwppQg0zP3RF14rwDbUyv0phw9kh4KxFWaJdQp2lxl0B6LUB0MpftUjK+JO8woOPSidz1Rg',
    'x-twitter-auth-type': 'OAuth2Session',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform-version': '"6.0"',
    'cookie': cookie_string,
    }
    return headers

session = requests.Session(impersonate="chrome120")

def retweet(user_id, session, link):
        json_data = {
            'variables': {
                'tweet_id': user_id,
            },
            'queryId': 'mbRO74GrOvSfRcJnlMapnQ',
        }

        headers = get_header(
            authorization,
            cookie_string,
            ct0,
            link,
        )

        r = session.post(
            "https://x.com/i/api/graphql/mbRO74GrOvSfRcJnlMapnQ/CreateRetweet",
            headers=headers,
            json=json_data
        )

        if r.status_code == 200:
              return True
        else:              
              return False


