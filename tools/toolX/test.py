from curl_cffi import requests
from action.util import get_cookie
from golike.util import human_sleep
cookie_string = get_cookie()
cookies = dict(item.split("=", 1) for item in cookie_string.split("; "))

ct0 = cookies["ct0"]

authorization = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

def get_header():
    headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'origin': 'https://x.com',
    'priority': 'u=1, i',
    'referer': 'https://x.com/elonmusk/status/2037068353635004606',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"iOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1',
    'x-client-transaction-id': 'af3jeKbU6jSPYLsvgzYj+ZN17dakEA47OGyegdybvlG2rpP+7VIsGie0qGhH9K2ZPqbYHGzjDTh4M8jSvfNu/Z9vOaxiag',
    'x-csrf-token': '4808338932ed29b75b864532a74ff6a96f27ac667df7dc02c536ccbfb124d35194db9d25be95cf057945fe555539141cffb4f6987ff57737424d30fe06a1ef5cd5c669e3ae2fbbeb32a329dbf5fc9c03',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
    'cookie': 'guest_id=v1%3A177450642452161673; guest_id_marketing=v1%3A177450642452161673; guest_id_ads=v1%3A177450642452161673; personalization_id="v1_IEOPzziKluj1lnW3hyvLiQ=="; __cuid=950aa99fab194f2b803d6fd9fef9a461; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; g_state={"i_l":0,"i_ll":1774506434278,"i_e":{"enable_itp_optimization":0}}; kdt=w0PnrO9wAle69qRM6JhrWwd3Y7ZlO7GSqUotnvMv; auth_token=1cf40b65721a91034e417d4c1b669f8722380697; ct0=4808338932ed29b75b864532a74ff6a96f27ac667df7dc02c536ccbfb124d35194db9d25be95cf057945fe555539141cffb4f6987ff57737424d30fe06a1ef5cd5c669e3ae2fbbeb32a329dbf5fc9c03; twid=u%3D2037053795268718592; lang=en; __cf_bm=bimedU97iCagIZ3jeeCeipxYudLES6z4Nfe43YT7BlU-1774523085.3735356-1.0.1.1-M6CNgC5VUBmWoz5LWSc1m_g7qkzKBY4plrM31IxLua3bVtRIv_rWzjROHdDubBdYXGxYafEzcBRV8bF10zz05T_UucC5uClzHx34NAvOMDib.pifjoI_wsy92AjwA8XK',
    }
    return headers

session = requests.Session()

def retweet(tweet_id, link):
        json_data = {
            'variables': {
                'tweet_id': tweet_id,
            },
            'queryId': 'mbRO74GrOvSfRcJnlMapnQ',
        }

        headers = get_header(
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

        data_check_retweet_post = get_retweet_check(tweet_id, link).json()

        result = check_status_retweet_post(data_check_retweet_post)
        print (f"Da retweet: {result}")
        if result == False:
            r = session.post(
            "https://x.com/i/api/graphql/mbRO74GrOvSfRcJnlMapnQ/CreateRetweet",
            headers=headers,
            json=json_data
            )
            print (r.status_code)
            print (r.text)
            print("Đã retweet")
            return True
        else:
            return False




def get_header_check():
    headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'origin': 'https://x.com',
    'priority': 'u=1, i',
    'referer': 'https://x.com/elonmusk/status/2037068353635004606',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"iOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1',
    'x-client-transaction-id': 'af3jeKbU6jSPYLsvgzYj+ZN17dakEA47OGyegdybvlG2rpP+7VIsGie0qGhH9K2ZPqbYHGzjDTh4M8jSvfNu/Z9vOaxiag',
    'x-csrf-token': '4808338932ed29b75b864532a74ff6a96f27ac667df7dc02c536ccbfb124d35194db9d25be95cf057945fe555539141cffb4f6987ff57737424d30fe06a1ef5cd5c669e3ae2fbbeb32a329dbf5fc9c03',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
    'cookie': 'guest_id=v1%3A177450642452161673; guest_id_marketing=v1%3A177450642452161673; guest_id_ads=v1%3A177450642452161673; personalization_id="v1_IEOPzziKluj1lnW3hyvLiQ=="; __cuid=950aa99fab194f2b803d6fd9fef9a461; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; g_state={"i_l":0,"i_ll":1774506434278,"i_e":{"enable_itp_optimization":0}}; kdt=w0PnrO9wAle69qRM6JhrWwd3Y7ZlO7GSqUotnvMv; auth_token=1cf40b65721a91034e417d4c1b669f8722380697; ct0=4808338932ed29b75b864532a74ff6a96f27ac667df7dc02c536ccbfb124d35194db9d25be95cf057945fe555539141cffb4f6987ff57737424d30fe06a1ef5cd5c669e3ae2fbbeb32a329dbf5fc9c03; twid=u%3D2037053795268718592; lang=en; __cf_bm=bimedU97iCagIZ3jeeCeipxYudLES6z4Nfe43YT7BlU-1774523085.3735356-1.0.1.1-M6CNgC5VUBmWoz5LWSc1m_g7qkzKBY4plrM31IxLua3bVtRIv_rWzjROHdDubBdYXGxYafEzcBRV8bF10zz05T_UucC5uClzHx34NAvOMDib.pifjoI_wsy92AjwA8XK',
    }
    return headers

def get_params(focalTweetId):
    params = {
    'variables': f'{{"focalTweetId":"{focalTweetId}","with_rux_injections":false,"rankingMode":"Relevance","includePromotedContent":true,"withCommunity":true,"withQuickPromoteEligibilityTweetFields":true,"withBirdwatchNotes":true,"withVoice":true}}',
    'features': '{"rweb_video_screen_enabled":false,"profile_label_improvements_pcf_label_in_post_enabled":true,"responsive_web_profile_redirect_enabled":false,"rweb_tipjar_consumption_enabled":false,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"premium_content_api_read_enabled":false,"communities_web_enable_tweet_community_results_fetch":true,"c9s_tweet_anatomy_moderator_badge_enabled":true,"responsive_web_grok_analyze_button_fetch_trends_enabled":false,"responsive_web_grok_analyze_post_followups_enabled":true,"responsive_web_jetfuel_frame":true,"responsive_web_grok_share_attachment_enabled":true,"responsive_web_grok_annotations_enabled":true,"articles_preview_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"content_disclosure_indicator_enabled":true,"content_disclosure_ai_generated_indicator_enabled":true,"responsive_web_grok_show_grok_translated_post":false,"responsive_web_grok_analysis_button_from_backend":true,"post_ctas_fetch_enabled":true,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":false,"responsive_web_grok_image_annotation_enabled":true,"responsive_web_grok_imagine_annotation_enabled":true,"responsive_web_grok_community_note_auto_translation_is_enabled":false,"responsive_web_enhance_cards_enabled":false}',
    'fieldToggles': '{"withArticleRichContentState":true,"withArticlePlainText":false,"withArticleSummaryText":true,"withArticleVoiceOver":true,"withGrokAnalyze":false,"withDisallowedReplyControls":false}',
    }
    return params

def get_retweet_check(focalTweetId, link):
    return requests.get(
        'https://x.com/i/api/graphql/CysGzLIZa76UzZ3WTe-Bhg/TweetDetail',
        params=get_params(focalTweetId),
        headers=get_header_check())

def check_status_retweet_post(data):
    instructions = data["data"]["threaded_conversation_with_injections_v2"]["instructions"]
   

    entries = []

    for item in instructions:
        if "entries" in item:
            entries = item["entries"]
            break

    # lấy tweet
    for entry in entries:
        content = entry.get("content", {})
        item = content.get("itemContent")

        if not item:
            continue

        result = item.get("tweet_results", {}).get("result", {})

        # 👇 FIX QUAN TRỌNG
        legacy = result.get("legacy") or result.get("tweet", {}).get("legacy", {})

        retweeted = legacy.get("retweeted")

        return retweeted
    
result = retweet("2037068353635004606", "https://x.com/elonmusk/status/2037068353635004606")

print(result)