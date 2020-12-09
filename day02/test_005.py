'''
fixture的作用域
1、默认是函数级别的
2、函数级别-> 模块级别的->类级别的->Session级别的
'''

# 模块级别
import pytest
#测试前置和后置
@pytest.fixture(scope='module') #scope设置作用域，取值范围：function、module、class、session
def login():
    print("登录系统") #yield之前是前置
    yield
    print("退出系统") #yield之后是后置

@pytest.fixture(scope='module')
def db():
    print("连接数据库")
    yield
    print("断开连接数据库")

def test_query(db): #连接数据库
    print("查询功能，不需要登录")

def test_add(login,db): #第一次使用fixture的地方执行前置
    print("添加功能，需要登录")

def test_delete():
    print("删除功能，需要登录")

def test_modify(): #模块执行结束，执行后置
    print("执行后置")