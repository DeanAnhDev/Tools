from curl_cffi import requests
from action.util import get_cookie
from golike.util import human_sleep
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

session = requests.Session()

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

        headers_home = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-arch': '""',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"146.0.7680.154"',
        'sec-ch-ua-full-version-list': '"Chromium";v="146.0.7680.154", "Not-A.Brand";v="24.0.0.0", "Google Chrome";v="146.0.7680.154"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-model': '"Nexus 5"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"6.0"',
        }
        session.get("https://x.com/home", headers=headers_home)
        human_sleep()

        session.get(link, headers=headers)
        human_sleep()

        r = session.post(
            "https://x.com/i/api/graphql/mbRO74GrOvSfRcJnlMapnQ/CreateRetweet",
            headers=headers,
            json=json_data
        )

        print(r.status_code)
        print(r.text)   # raw

        return check_retweet(r)

        # if r.status_code == 200:
        #       return True
        # else:              
        #       return False

def check_retweet(res):
    try:
        data = res.json()
    except:
        return False

    # ❌ Có lỗi
    if "errors" in data:
        code = data["errors"][0].get("code")

        if code == 327:
            return False
        else:
            return False

    # ✅ Thành công
    if "data" in data:
        create_rt = data["data"].get("create_retweet")

        if create_rt:
            return True

    return False

# result = retweet("2024981547997429792", session, "https://x.com/RobertLee209/status/2024981547997429792")
# print(result)