'''
登录接口测试脚本
'''

import pytest
from ZongHe.caw import DataRead
from ZongHe.baw import Member
from ZongHe.baw import DbOp

@pytest.fixture(params=DataRead.read_yaml("data_case\login_setup.yaml"),scope='module')
def setup_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml("data_case\login_data.yaml"))
def login_data(request):
    return request.param

@pytest.fixture(scope='module')
def register(url,baserequests,setup_data,db,):
    # 注册用户
    print(f"测试数据：{setup_data}")
    mobile = setup_data['casedata']['mobilephone']
    r = Member.register(url,baserequests,setup_data['casedata'])
    assert r.json()['msg'] == setup_data['expect']['msg']
    assert r.json()['code'] == setup_data['expect']['code']
    yield
    # 删除注册用户
    DbOp.delete_user(db, mobile)


def test_login(register,login_data,url,baserequests):
    # 下发登录请求
    r = Member.login(url, baserequests, login_data['casedata'])
    # 检查结果
    assert r.json()['msg'] == login_data['expect']['msg']
    assert r.json()['code'] == login_data['expect']['code']
