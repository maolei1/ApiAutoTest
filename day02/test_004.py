'''
fixture 测试前置和后置，比较常用的方式
1、命名比较灵活，不限于setup、teardown等命名方式
2、使用比较灵活
3、不需要import即可实现共享
'''

import pytest
#测试前置和后置
@pytest.fixture()
def login():
    print("登录系统") #yield之前是前置
    yield
    print("退出系统") #yield之后是后置

def test_query():
    print("查询功能，不需要登录")

#使用方式一：将fixture作为参数传到脚本中
def test_add(login):
    print("添加功能，需要登录")

# 使用方式二：使用use装饰器fixtures
@pytest.mark.usefixtures("login")
def test_delete():
    print("删除功能，需要登录")