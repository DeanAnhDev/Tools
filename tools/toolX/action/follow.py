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
    'x-twitter-auth-type': 'OAuth2Session',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform-version': '"6.0"',
    'cookie': cookie_string,
    }
    return headers

session = requests.Session()

def follow(user_id, link):
        data = {
            'include_profile_interstitial_type': '1',
            'include_blocking': '1',
            'include_blocked_by': '1',
            'include_followed_by': '1',
            'include_want_retweets': '1',
            'include_mute_edge': '1',
            'include_can_dm': '1',
            'include_can_media_tag': '1',
            'include_ext_is_blue_verified': '1',
            'include_ext_verified_type': '1',
            'include_ext_profile_image_shape': '1',
            'skip_status': '1',
            'user_id': user_id,
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

        session.get(link, headers=headers_home)
        human_sleep()

        username = get_username_from_url(link)

        res = get_user_UserByScreenName(username, link)
        data_for_check_follow = res.json()
        following = data_for_check_follow["data"]["user"]["result"]["relationship_perspectives"]["following"]

        if(following == False):
            r = session.post(
                "https://x.com/i/api/1.1/friendships/create.json",
                headers=headers,
                data=data
            )
            print(r.status_code)
            print(r.text)
            return True
        else :
            print("Đã follow trước đó, bỏ qua...") 
            return False


def get_header_check(authorization, cookie_string, ct0, referer):
    headers = {
   'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': authorization,
    'content-type': 'application/json',
    'priority': 'u=1, i',
    'referer': referer,
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    'sec-ch-ua-arch': '""',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"146.0.7680.154"',
    'sec-ch-ua-full-version-list': '"Chromium";v="146.0.7680.154", "Not-A.Brand";v="24.0.0.0", "Google Chrome";v="146.0.7680.154"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"6.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': ct0,
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
    'cookie': cookie_string,
    }
    return headers

def get_params(screen_name):
    params = {
        'variables': f'{{"screen_name":"{screen_name}","withGrokTranslatedBio":false}}',
        'features': '{"hidden_profile_subscriptions_enabled":true,"profile_label_improvements_pcf_label_in_post_enabled":true,"responsive_web_profile_redirect_enabled":false,"rweb_tipjar_consumption_enabled":false,"verified_phone_label_enabled":false,"subscriptions_verification_info_is_identity_verified_enabled":true,"subscriptions_verification_info_verified_since_enabled":true,"highlights_tweets_tab_ui_enabled":true,"responsive_web_twitter_article_notes_tab_enabled":true,"subscriptions_feature_can_gift_premium":true,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
        'fieldToggles': '{"withPayments":false,"withAuxiliaryUserLabels":true}',
    }
    return params



from urllib.parse import urlparse

def get_user_UserByScreenName(screen_name, link):
    return requests.get(
        'https://x.com/i/api/graphql/IGgvgiOx4QZndDHuD3x9TQ/UserByScreenName',
        params=get_params(screen_name),
        headers=get_header_check( authorization,
            cookie_string,
            ct0,
            link,),
    )

def get_username_from_url(url):
    path = urlparse(url).path
    username = path.strip("/")
    return username
