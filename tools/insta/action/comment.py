from curl_cffi import requests
from action.util import get_cookie
cookie_string = get_cookie()
cookies = dict(item.split("=", 1) for item in cookie_string.split("; "))

ct0 = cookies["ct0"]

authorization = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

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
    'x-client-transaction-id': '5EWLuuw7ZxLY3oH/X1LtaCRNFzEYyUbLGT8sggYqludxlEVOIHRMG9NLXkW8eDv07ttPjOEtV0sBECIDIuFNTh3Wz5BY5w',
    'x-csrf-token': ct0,
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
    'cookie': cookie_string,
    }
    return headers

session = requests.Session(impersonate="chrome120")

def comment(post_id, comment, session, link):
        
        headers = get_header(
            authorization,
            cookie_string,
            ct0,
            link,
        )

      
        json_data = {
    'variables': {
        'tweet_text': comment,
        'reply': {
            'in_reply_to_tweet_id': post_id,
            'exclude_reply_user_ids': [],
        },
        'media': {
            'media_entities': [],
            'possibly_sensitive': False,
        },
        'semantic_annotation_ids': [],
        'disallowed_reply_options': None,
    },
    'features': {
        'premium_content_api_read_enabled': False,
        'communities_web_enable_tweet_community_results_fetch': True,
        'c9s_tweet_anatomy_moderator_badge_enabled': True,
        'responsive_web_grok_analyze_button_fetch_trends_enabled': False,
        'responsive_web_grok_analyze_post_followups_enabled': True,
        'responsive_web_jetfuel_frame': True,
        'responsive_web_grok_share_attachment_enabled': True,
        'responsive_web_grok_annotations_enabled': True,
        'responsive_web_edit_tweet_api_enabled': True,
        'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
        'view_counts_everywhere_api_enabled': True,
        'longform_notetweets_consumption_enabled': True,
        'responsive_web_twitter_article_tweet_consumption_enabled': True,
        'tweet_awards_web_tipping_enabled': False,
        'content_disclosure_indicator_enabled': True,
        'content_disclosure_ai_generated_indicator_enabled': True,
        'responsive_web_grok_show_grok_translated_post': False,
        'responsive_web_grok_analysis_button_from_backend': True,
        'post_ctas_fetch_enabled': True,
        'longform_notetweets_rich_text_read_enabled': True,
        'longform_notetweets_inline_media_enabled': False,
        'profile_label_improvements_pcf_label_in_post_enabled': True,
        'responsive_web_profile_redirect_enabled': False,
        'rweb_tipjar_consumption_enabled': False,
        'verified_phone_label_enabled': False,
        'articles_preview_enabled': True,
        'responsive_web_grok_community_note_auto_translation_is_enabled': False,
        'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
        'freedom_of_speech_not_reach_fetch_enabled': True,
        'standardized_nudges_misinfo': True,
        'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': True,
        'responsive_web_grok_image_annotation_enabled': True,
        'responsive_web_grok_imagine_annotation_enabled': True,
        'responsive_web_graphql_timeline_navigation_enabled': True,
        'responsive_web_enhance_cards_enabled': False,
    },
    'queryId': 'ZumXEfvjHvt55CBVLR_DBA',
    }

        r = session.post(
        'https://x.com/i/api/graphql/ZumXEfvjHvt55CBVLR_DBA/CreateTweet',
        headers=headers,
        json=json_data,
    )

        if r.status_code == 200:
                return True
        else:              
                return False
        

