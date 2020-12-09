import pytest
import requests
# 练习：注册接口的测试代码，用这种方式来实现
# 测试数据
# 参数使用params关键字，一个列表，列表中有5组数据，前3组数据是字典。
@pytest.fixture(params=[
                        {"data":{"mobilephone": "1234567890", "pwd": "123456"},"except":{'code':'20109','msg':'手机号码格式不正确'}},
                        {"data":{"mobilephone": "111111111111", "pwd": "123456"},"except":{'code':'20109','msg':'手机号码格式不正确'}},
                        {"data":{"mobilephone": None, "pwd": "123456"},"except":{'code':'20103','msg':'手机号不能为空'}},
                        ])
def login_data(request): #参数request是固定的，不能写成其他的
    return request.param # 使用request.param返回每组数据

# 测试逻辑(测试步骤)
# 登录功能测试脚本
def test_login(login_data):
    url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
    r = requests.post(url, data=login_data["data"])
    r = r.json()
    assert r['msg'] == login_data['except']['msg']
    assert  r['code'] == login_data['except']['code']
    print()
    print("测试数据：",login_data["data"])
    print("预期结果：",login_data["except"])
