'''
注册脚本
'''
import pytest
from ZongHe.caw import DataRead
from ZongHe.baw import Member
from ZongHe.baw import DbOp

@pytest.fixture(params=DataRead.read_yaml("data_case/register_fail.yaml"))
def fail_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml("data_case/register_pass.yaml"))
def pass_data(request):
    return request.param

# 测试逻辑/测试步骤
def test_register_fail(url,baserequests,fail_data):
    print(f"测试数据为：{fail_data}")
    # 下发注册的请求
    # fixture sission级别 conftest.py
    r = Member.register(url,baserequests,fail_data['data'])
    # 校验结果
    assert r.json()['msg'] == fail_data['expect']['msg']
    assert  r.json()['code'] == fail_data['expect']['code']

# 测试逻辑/测试步骤:注册成功
def test_register_success(db,url,baserequests,pass_data):
    print(f"测试数据：{pass_data}")
    # 获取手机号
    mobile = pass_data['data']['mobilephone']
    # 下发注册的请求
    # fixture sission级别 conftest.py
    r = Member.register(url, baserequests, pass_data['data'])
    # 检查结果，1.检查响应与预期结果一致
    assert r.json()['msg'] == pass_data['expect']['msg']
    assert r.json()['code'] == pass_data['expect']['code']
    # 检查结果，2.检查系统中用户注册成功
    # 方式1
    r = Member.list(url,baserequests)
    assert mobile in r.text
    # 清理环境：删除注册用户
    # 方式2
    r = DbOp.selete_user(db,mobile)
    assert len(r) == 1
    DbOp.delete_user(db, mobile)

# 重复注册
def test_register_repeat(db,url,baserequests,pass_data):
    mobile = pass_data['data']['mobilephone']
    print(f"测试数据：{pass_data}")
    r = Member.register(url, baserequests, pass_data['data'])
    assert r.json()['msg'] == pass_data['expect']['msg']
    n = Member.register(url, baserequests, pass_data['data'])
    # 检查结果，1.检查响应与预期结果一致
    assert n.json()['msg'] == '手机号码已被注册'
    DbOp.delete_user(db, mobile)
