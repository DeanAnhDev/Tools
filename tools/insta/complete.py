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
        'captcha_token': '0cAFcWeA7pnqUHZxzaDZecaCtZ6JMnYfJij02zZXsK2J6O9MIJusPgHAwX8jyDCnn5dBI5291fTv8VA76ilzf_u6MpKc5FKtI8EQ9UHsv1sbrtAxhBSO5pns8G0eAuDg0r8Ws-5hyjOLuyfmELHUzm3f7OrKrfWxrbBc3TNmuim137eZAK_cRkyk3piI6qSQQlNY71BP-pWs5_2oY1m5dZtQbI7rTpKkjZE33DbjzeY4yAvo645fsVWjLrCEN0DFrGb75Ua6UpSBIk5y6BY1cvgHkZ50pjGocLtCGO-B-3aXlTvuc1Uh4ENGoQ2r7y-EC-L2w_hJQMiBjtazSxfdMV71b08u1Fs_tjxewuLderVUbM31Id_yCaxSVys_V1aaXRHiVKAyADgsd1Yi8vVVfY1DQWWxHxVqK0HBqBlzuRxK-pl2eQewUfKI68dtpNhmY3nxi8mNaJb7ONzuMLvG_8plnqmsT8QvKo7mm8_SNiYHjvJf9yVFHNRsQiVpVqoK0L3Q93_ncpehaHpKG3OLVGpC2GVu_LiE-4ohx6k3cCib5e1JsKbDcU5rhLTxMFrV-Q8VFkwsi0wP7UZk19J9Uv5vNlaeyCUwI3XLi4gHPy32I2BRa67Fe_KPqC4wOisOhX1Ls9pHvCh-iCWS8KWS6rJz-5I3aI5SBL_l3xRXpyxPBP820QSwDD7Jdw9zXQJ9LnqkhJG8H68kULaozt60lRqjNWwNrP5jfmfk1m_ElF6TOzprqFxu43IMpbiZQGqfFkJsjTGsP44VBzPaBCxF4iP-nMZi9wxcwoiDou25K1VGpdUizinbHJceML7iBvRbM6LBIBubk9Ywg6Snqha8eoBC3oDHoVg0tulO6zkVj_PuJUF7cLDk5JTG2fLCDEIDLtY0LizDJjBTFId2AcWjcKtEKYhPYwI_Ahy7MXO4b2iic5Hjj3eK-_Gx6CG2uaoDQ_mvg7_8WLdhUQvPINXg4sVSBWuf6iBYtckAfPod54K2WwFKrHJFgojorXU2mxmSLjciX5TGNA_Ytn51wRmU4Vqu1T_4vsFMPeo2KHsgmLiIDa8nKlukW0kq-Mkl4Qqaa0EYRlH18e7Vrmsdv1VjV_uh97E4WQ-RbWfXfSvgF0vXhEcjDjBUqXux26lev6jWu3cn9lrA6ektq6pZ3EMJ4rUALSNR4GAUBBGZxx1qGpv1Vn9KphDGJ7lf-6qpY5c8vpEnTMi6MUOrh3giSBag6cAo4VOi8bh4Dfx4i0IZd-KfXnR8vZqGGViTKPYa_0-NJ8p-cUmdJYtrxWsGudenYl9_osYt_kiL4D0lglUafOL5GxSFsW2spiC95z4HXtj2ohVM-rH4374VN28Q01eof4wCgJ5dMTW9cU1OsH69lb2QGXMrN-DkN5MWXLPQe1_9qQzQYy7p6C7F2PzXopaBRh257f20DKJvLbpZA1q8ShuEy5FNKS_Cfp-OdrPBedyB3hHJVs-ycV2sHDEwhtKXN4GGe37gDb98wEsioBVBs1acp_4sH0842ciQUQ52IvvOm-4XLIaYD8bUwqW2IH6roRVOTaLMVQqRDeoGQ_7HDoW89e2s2uK-iCIxyMvX3qV5XvFE74r8dQcIrCvEEt1tPzfqjK3ZEmuEdNnrqhjxJiU44LOSQuV5Kwaw98JqNd3PicCryPHAMA47Kvhob2WCf7TpTUdPFtzIuTxygGoUf02SzFPOriUwMMFEwOGQPFOp9dmIv4EAa7qiIPNjlESqTzsI6ZZCniyNxxSkajuWe4DYN9UFVkmxm-1jOeIfx05nEdr_OK--eRrjU4YksqTuHc7ICZDPLxXhO1f5cMLjsBr304dnn5MENj9GBXY8a70nhGvWqLWDpELwwVI3mfSn2F8Pa5vNnQ73bmWXEbRA4iIELWch10p6uaJiRoYgrDUKgFFQddh-8mEq804Z7BU2boCNGXrx1so5PDjz2u_pro64auOQR7SFn9wULB8npM6_3frBMSevpBTOVnZ7on9IXj5H1aowwaqEqXg0zhZuDUvEq17PQ-lo5KlsXLYI5XF0MI5C4oSef2K9JANFGaQkc9OhD-E7cMXgcF-QJocO91AVsk4hek5JXXtQeSH77uz2VhmKlR-aOhdjmRErf3vonKmDfKWEI7ie_dk3xGPceaDqyVoPznHMtIQ9M',
        'captcha': 'recaptcha',
    }

    response = session.post('https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs', headers=headers, json=json_data).json()
    if response['data'] == 200 and response['success'] == True:
        return True
    return False

