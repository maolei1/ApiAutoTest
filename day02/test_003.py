'''
测试前置和后置
'''
# 类级别和方法级别

class Test001:
    def setup_class(self):
        print("测试前置:class级别，类开始执行一次")

    def teardown_class(self):
        print("测试后置:class级别，类结束执行一次")

    def setup_method(self):
        print("测试前置：function级别")

    def teardown_method(self):
        print("测试后置：function级别")

    def test_01(self):
        print("测试脚本1")

    def test_02(self):
        print("测试脚本2")

    def test_03(self):
        print("测试脚本3")