'''
fixture作用域：类级别的
'''

import pytest
#测试前置和后置
@pytest.fixture(scope='class') #scope设置作用域，取值范围：function、module、class、session
def login():
    print("登录系统") #yield之前是前置
    yield
    print("退出系统") #yield之后是后置

class TestQuery:
    def test_01(self):
        print("查询：用例1")

    def test_02(self,login): #这里执行前置
        print("查询：用例2")

    def test_03(self,login):
        print("查询：用例3")

    def test_04(self,login): #这里执行后置
        print("查询：用例4")

class TestAdd:
    def test_01(self,login): #这里执行前置
        print("添加：用例1")

    def test_02(self):
        print("添加：用例2")

    def test_03(self,login): #这里执行后置
        print("添加：用例3")