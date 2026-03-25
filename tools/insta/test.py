from curl_cffi import requests

from action.util import get_cookie
cookie_string = get_cookie()
cookies = dict(item.split("=", 1) for item in cookie_string.split("; "))

csrftoken = cookies["csrftoken"]

print( csrftoken)