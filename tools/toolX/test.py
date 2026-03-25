from curl_cffi import requests
from action.util import get_cookie
from action.updatedata import save_cookie
cookie_string = get_cookie()
cookies = dict(item.split("=", 1) for item in cookie_string.split("; "))
ct0 = cookies["ct0"]
authorization = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': authorization,
    'origin': 'https://x.com',
    'priority': 'u=1, i',
    'referer': 'https://x.com/',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36',
    'x-client-transaction-id': 'oau33Uje8BtFM6AfR4ldQ3O3MNXuRa3O3T0KYfiEmk2I3UE5ncrx5OAzfgm3ee+VZUdtzaQTv/lNsSEkEmw+7XsOJkFFog',
    'x-csrf-token': ct0,
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
    'cookie': cookie_string,
}

params = {
    'include_ext_sharing_audiospaces_listening_data_with_followers': 'true',
    'include_mention_filter': 'true',
    'include_nsfw_user_flag': 'true',
    'include_nsfw_admin_flag': 'true',
    'include_ranked_timeline': 'true',
    'include_alt_text_compose': 'true',
    'include_ext_dm_av_call_settings': 'true',
    'ext': 'ssoConnections',
    'include_country_code': 'true',
    'include_ext_dm_nsfw_media_filter': 'true',
}

session = requests.Session(impersonate="chrome120")

def test_cookie():
    response = session.get('https://api.x.com/1.1/account/settings.json', params=params, headers=headers)

    if response.status_code == 200:
        print("Cookie live")
    else:
        print("Cookie die nhập lại cookie")
        save_cookie()

test_cookie()