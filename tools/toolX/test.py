import requests

cookies = {
    'datr': 'G3qeaafadqsZ--pX8w-PDzqZ',
    'ig_did': '2A6FB4C3-4356-4361-A9D3-FCF9616E7F17',
    'mid': 'aZ56GwALAAElRbs_welgTud5bMqX',
    'ps_l': '1',
    'ps_n': '1',
    'csrftoken': 'to1uUfj5txtzfrm9UgqaG049E4uYdJty',
    'ds_user_id': '47848450874',
    'sessionid': '47848450874%3Accu7l7lWVIBF53%3A17%3AAYh-ukHMaY1MS7imok5o_jvATWPpoSl-SP8xTxM-JH0',
    'wd': '1186x1202',
    'dpr': '2',
    'rur': '"EAG\\05447848450874\\0541806111919:01fe14f917ae9dbb88094d030a161499e5f88771075c2d014871350f3532d0f58f2d8b2b"',
}

headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/htgkayletem_/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    'sec-ch-ua-full-version-list': '"Chromium";v="146.0.7680.165", "Not-A.Brand";v="24.0.0.0", "Google Chrome";v="146.0.7680.165"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"6.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36',
    'x-asbd-id': '359341',
    'x-bloks-version-id': '74ac2194124071d4925c1e5ed9d479298251c3f517a443d023893164137bb26b',
    'x-csrftoken': 'to1uUfj5txtzfrm9UgqaG049E4uYdJty',
    'x-fb-friendly-name': 'usePolarisFollowMutation',
    'x-fb-lsd': 'rYwVDpXxb7qdI8Vo-EMyBx',
    'x-ig-app-id': '1217981644879628',
    'x-root-field-name': 'xdt_create_friendship',
    # 'cookie': 'datr=G3qeaafadqsZ--pX8w-PDzqZ; ig_did=2A6FB4C3-4356-4361-A9D3-FCF9616E7F17; mid=aZ56GwALAAElRbs_welgTud5bMqX; ps_l=1; ps_n=1; csrftoken=to1uUfj5txtzfrm9UgqaG049E4uYdJty; ds_user_id=47848450874; sessionid=47848450874%3Accu7l7lWVIBF53%3A17%3AAYh-ukHMaY1MS7imok5o_jvATWPpoSl-SP8xTxM-JH0; wd=1186x1202; dpr=2; rur="EAG\\05447848450874\\0541806111919:01fe14f917ae9dbb88094d030a161499e5f88771075c2d014871350f3532d0f58f2d8b2b"',
}

data = {
    'av': '17841447846231056',
    'fb_dtsg': 'NAftH1QLKVWokWEbG7cvwtS-9hE06Z6QM4wbPhE7okD9T60A9KZ2zAQ:17864329786054772:1772012178',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'usePolarisFollowMutation',
    'variables': '{"target_user_id":"31154882871","container_module":"profile","nav_chain":"PolarisProfilePostsTabRoot:profilePage:1:via_cold_start"}',
    'doc_id': '9740159112729312',
}

response = requests.post('https://www.instagram.com/graphql/query', cookies=cookies, headers=headers, data=data)