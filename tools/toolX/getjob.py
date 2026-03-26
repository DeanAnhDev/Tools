from curl_cffi import requests
from golike.util import get_account_id, get_authorization
from action.follow import follow
from action.favorite import like_tweet
from action.comment import comment
from action.retweet import retweet
from skipjob import skip_job, send
from complete import complete_job
from golike.util import job_sleep, job_complete_sleep

authorization = get_authorization() 

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': authorization,
    'content-type': 'application/json;charset=utf-8',
    'origin': 'https://app.golike.net',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"iOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    't': 'VFZSak0wNUVSVEpPVkZFelRVRTlQUT09',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1',
}


account_id = get_account_id()

params = {
    'account_id': account_id,
}

session = requests.Session(impersonate="chrome120")

def get_job():
    response = session.get('https://gateway.golike.net/api/advertising/publishers/twitter/jobs', params=params, headers=headers)

    data = response.json() 

    if data['status'] == 200:
        return data

    elif data['status'] == 400 and data['success'] == False:
        print(data['message'])
        return None
    else:
        print("Lỗi không xác định:", response.text)
        return None

def run_job():
    sum_money = 0

    while sum_money < 1000:
        job_sleep()
        response = get_job()
        if response is None:
            print("⏳ Hết job, nghỉ 30s...")
            job_sleep()
            continue
        job_id = response['data']['id']
        link_job = response['data']['link']
        job_type = response['data']['type']
        object_id = response['data']['object_id']
        job_cost = response['data']['price_per_after_cost']
        

        print(f"🔔 Nhận được job: {job_id} | Link: {link_job} | Type: {job_type} | Cost: {job_cost} VND | object_id: {object_id}")

        if job_type == "follow" :
            result = follow(object_id, link_job)
            if result == False:
                send_result = send(job_id, account_id)
                skip_job_result = skip_job(job_id, account_id, object_id)
                if send_result and skip_job_result:
                    print(f"Đã bỏ qua job {job_id} vì đã làm rồi.")
                    continue
        elif job_type == "like" :
            result = like_tweet(object_id, link_job)
            if result == False:
                send_result = send(job_id, account_id)
                skip_job_result = skip_job(job_id, account_id, object_id)
                if send_result and skip_job_result:
                    print(f"Đã bỏ qua job {job_id} vì đã làm rồi.")
                    continue
        # elif job_type == "comment" :
        #        comment_job = response['lock']['message']
        #     result = comment(object_id, comment_job, session, link_job)
        #     if result == False:
        #         send_result = send(job_id, account_id)
        #         skip_job_result = skip_job(job_id, account_id, object_id)
        #         if send_result and skip_job_result:
        #             print(f"Đã bỏ qua job {job_id} vì không thực hiện được.")
        #             continue
        elif job_type == "retweet" :
            result = retweet(object_id, link_job)
            if result == False:
                send_result = send(job_id, account_id)
                skip_job_result = skip_job(job_id, account_id, object_id)
                if send_result and skip_job_result:
                    print(f"Đã bỏ qua job {job_id} vì đã làm rồi.")
                    continue
        else:
            send_result = send(job_id, account_id)
            skip_job_result = skip_job(job_id, account_id, object_id)
            if send_result and skip_job_result:
                print(f"Đã bỏ qua job {job_id} vì không thực hiện được.")
                continue
        # Sau khi làm job xong thì gửi
        job_complete_sleep()
        complete_job(job_id, account_id)
        sum_money += job_cost
        print(f"💰 Đã hoàn thành job: {job_id}| Link: {link_job} | {job_cost} VND | Đã kiếm: {sum_money}")

    print("Đã đạt mục tiêu 1000đ, dừng!")