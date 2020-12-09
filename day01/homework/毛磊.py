import requests
import random
#注册
#sign_001
#验证用10位数的手机号注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {"mobilephone": "1234567890", "pwd": "123456"}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

#sign_002
#验证用12位数的手机号注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {"mobilephone": "111111111111", "pwd": "123456"}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

#sign_003
#验证用空手机号注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {"mobilephone": None, "pwd": "123456"}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '手机号不能为空'

#sign_004
#"验证用已经注册的手机号注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {"mobilephone": 17792930289, "pwd": "123456"}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20110'
assert r['msg'] == '手机号码已被注册'

#sign_005
#"验证用5位数密码注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {"mobilephone": "15523451769", "pwd": "12345"}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20108'
assert r['msg'] == '密码长度必须为6~18'

#sign_006
#"验证用19位数密码注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {"mobilephone": "15523452769", "pwd": "1234567890111111111"}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20108'
assert r['msg'] == '密码长度必须为6~18'

#sign_007
#"验证用6位数密码注册，注册成功
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {"mobilephone": "151%s"%random.randint(10000000,99999999), "pwd": "123456"}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 1
assert r['code'] == '10001'
assert r['msg'] == '注册成功'

#sign_008
#"验证用18位数密码注册，注册成功
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {"mobilephone": "151%s"%random.randint(10000000,99999999), "pwd": "123456789011111111"}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 1
assert r['code'] == '10001'
assert r['msg'] == '注册成功'

#sign_009
#"验证用空密码注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {"mobilephone": "151%s"%random.randint(10000000,99999999), "pwd": None}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '密码不能为空'

#sign_0010
#验证用正确的手机号，正确的密码注册，正确注册名，填用户昵称，注册成功
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {"mobilephone": "151%s"%random.randint(10000000,99999999), "pwd": '123456','regname':'毛磊'}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 1
assert r['code'] == '10001'
assert r['msg'] == '注册成功'

#登陆
#sign_0011
#验证用10位数的手机号登录，登陆异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {"mobilephone": "1234567890", "pwd": "123456"}
r = requests.get(url, params=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或密码错误'

#sign_0012
#验证用12位数的手机号登录，登陆异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {"mobilephone": "123456789000", "pwd": "123456"}
r = requests.get(url, params=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或密码错误'

#sign_0013
#验证用空手机号登录，登陆异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {"mobilephone": None, "pwd": "123456"}
r = requests.get(url, params=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '手机号不能为空'

#sign_14
#"验证用5位数密码登陆，登陆异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {"mobilephone": "15523451769", "pwd": "12345"}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或密码错误'

#sign_15
#"验证用19位数密码登陆，登陆异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {"mobilephone": "15523451769", "pwd": "1234567890111111111"}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或密码错误'

#sign_16
#"验证用6位数密码登陆，登陆成功
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {"mobilephone": "17792930289", "pwd": "123456"}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 1
assert r['code'] == '10001'
assert r['msg'] == '登录成功'

#sign_17
#"验证用18位数密码登陆，登陆成功
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {"mobilephone": "17792930281", "pwd": "123456789000000000"}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或密码错误'

#sign_18
#"验证用空密码登陆，登陆失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {"mobilephone": "17792930289", "pwd": None}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '密码不能为空'

#sign_19
#"验证用未注册的手机号登陆，登陆失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {"mobilephone": "13792930289", "pwd": '123456'}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或密码错误'



