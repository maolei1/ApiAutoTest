'''
脚本层的一些公共方法
'''

import pytest
from ZongHe.caw import DataRead
from ZongHe.caw.BaseRequests import BaseRequests

# 从环境文件中读取环境信息，整个过程读一次即可
@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini('data_env/env.ini','url')

# 创建有个BaseRequests的实例，整个执行过程使用这个实例下发请求
@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()

# 从环境文件中读取db信息，整个过程读一次即可
@pytest.fixture(scope='session')
def db():
    # 读取出来的是字符串，需要的诗歌字典，需要将字符串解析成字典
    info = DataRead.read_ini('data_env/env.ini','db')
    print(type(info))
    return eval(info) # 将字符串解析成字典