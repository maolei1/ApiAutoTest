class TestAdd:
    def test_01(self,login): #这里执行前置
        print("添加：用例1")

    def test_02(self):
        print("添加：用例2")

    def test_03(self,login): #这里执行后置
        print("添加：用例3")