'''
发送post请求
'''

import requests
#登录的接口
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user ={"mobilephone":"17792930289", "pwd": "123456"}
# 用data传表单参数
r = requests.post(url,data=user)

# print(r.json())

url = "http://www.httpbin.org/post"
user ={"mobilephone":"17792930289","pwd":"123456"}
r = requests.post(url,data=user)
# print(r.text)
print("*"*50) #分隔线
# 用json传参数
r = requests.post(url,json=user)
# print(r.text)

#练习：充值接口，给注册的用户充值
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/withdraw"
user = {"mobilephone": "17792930289", "amount": 500000}
r = requests.post(url,data=user)
# print(r.json())