from golike.util import get_authorization
from curl_cffi import requests

authorization = get_authorization()

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': authorization,
    'origin': 'https://app.golike.net',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"iOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    't': 'VFZSak0wNUVSVE5PVkUweVRWRTlQUT09',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1',
}
session = requests.Session(impersonate="chrome120")

def complete_job(job_id, account_id):

    json_data = {
        'ads_id': job_id,
        'account_id': account_id,
        'async': True,
    }

    response = session.post('https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs', headers=headers, json=json_data).json()
    if response['data'] == 200 and response['success'] == True:
        return True
    return False

