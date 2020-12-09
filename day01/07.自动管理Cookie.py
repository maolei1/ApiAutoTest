'''
自动管理cookie
通过 requests.session 自动管理cookies
'''

import requests

s = requests.session()

#登录百格
url = "https://www.bagevent.com/user/login"
user ={
    "access_type": "1",
    "loginType": "1",
    "emailLoginWay": "0",
    "account": "2780487875@qq.com",
    "password": "qq2780487875",
    "remindmeBox": "on",
    "remindme": "1"
}
r = s.post(url, data=user)
# print(r.text)
print("*"*50,"登录后的cookies",s.cookies)

#获取账户的信息
url = "https://www.bagevent.com/account/dashboard"
r = s.get(url)
# print(r.text)
assert "<title>百格活动 - 账户总览</title>" in r.text

#退出登录
url = "https://www.bagevent.com/user/login_uot"
r = s.get(url)
# print(r.text)
print("*"*50,"退出登录后的cookies",s.cookies)