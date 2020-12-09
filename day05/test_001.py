'''
mock:
1.按接口测试的测试场景比较难模拟，需要大量的工作才能做好。
2.该接口的测试，依赖其他模块的接口，依赖的接口尚未开发完成
测试条件不允许时，怎么开展测试接口？
使用Mock模拟接口的返回值。
'''
from unittest import mock

import requests
'''
支付接口：http://www.zhifu.com/
方法：post
参数：{"订单号":"12345","支付金额"：20.56","支付方式":"支付宝/微信/余额宝/银行卡"}
返回值：{"code":200,"msg":"支付成功"}、{"code":201,"msg":"支付失败"}
接口尚未开发完成
'''

class Pay:
    def zhifu(self,data):
        r = requests.post("http://www.zhifu.com/",data=data)
        return r.json()

def test_01():
    pay = Pay()
    # 通过mock模拟接口的返回值
    pay.zhifu = mock.Mock(return_value={"code":200,"msg":"支付成功"})
    canshu = {"订单号":"12345","支付金额":20.56,"支付方式":"支付宝"}
    r = pay.zhifu(canshu)
    print(r)
    assert r['msg'] == '支付成功'

def test_02():
    pay = Pay()
    # 通过mock模拟接口的返回值
    pay.zhifu = mock.Mock(return_value={"code":201,"msg":"支付失败"})
    canshu = {"订单号":"123456","支付金额":-20.56,"支付方式":"支付宝"}
    r = pay.zhifu(canshu)
    print(r)
    assert r['msg'] == '支付失败'

# 模块名.类名.方法名
@mock.patch("day05.test_001.Pay.zhifu",return_value={"code":200,"msg":"支付成功"})
def test_03(mock_pay):
    pay = Pay()
    canshu = {"订单号": "123456", "支付金额": 2000.56, "支付方式": "微信"}
    r = pay.zhifu(canshu)
    print(r)
    assert r['msg'] == '支付成功'

# 取现接口未实现，写一个取现成功的用例
class Quxian:
    def quxian(self,data):
        r = requests.post("http:/192.168.150.54:8089/futureloan/mvc/api/member/withdraw",data=data)
        return r.json()

@mock.patch("day05.test_001.Quxian.quxian",return_value={"code":200,"msg":"取现成功"})
def test_quxian(m):
    qx = Quxian()
    canshu = {"mobilephone":"13398761234","amount":"100"}
    r = qx.quxian(canshu)
    print(r)
    assert r['msg'] == '取现成功'




