'''
Cookie:
http协议：无状态，无连接，媒体独立
每一个请求都是独立的。有一些接口登录后餐能访问，需要使用Cookies验证用户是否登录
account/dashboard 用户内有登录时，返回登录的页面
account/dashboard 如果登录了，返回用户的详细信息。浏览器登陆后，获取到的cookie直接放到自动化来用
如果cookie失败或者换其他用户登录，就不能继续访问了。
'''
import requests
#百格网站，有一些接口登录之后才能访问
print("未登录时，返回结果为：")
url = "https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)

# 用Fiddler抓到的包，将里面的头设置到这里
head = { "cookie":'__auc=1d057e3517627477821b5bed508; MEIQIA_TRACK_ID=1l8RWYPxr7rNPXyTnkV0tXicH9E; _ga=GA1.2.713197231.1606976783; __asc=2abb17d91762cbeebb9565c5455; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1606976762,1606977828,1607068478; _gid=GA1.2.1244014961.1607068478; BAGSESSIONID=bfed010c-e1cd-4a7d-bea1-da830c612ee0; JSESSIONID=C2867EBD60760811AC6B0C682614143F; MEIQIA_VISIT_ID=1lBRXPXRQSzJ7A4LqVojBTn92on; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1607068590'
}
print("登录后，返回的结果为：")
r = requests.get(url,headers =head)
print(r.text)