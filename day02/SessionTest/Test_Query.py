class TestQuery:
    def test_01(self):
        print("查询：用例1")

    def test_02(self,login): #这里执行前置
        print("查询：用例2")

    def test_03(self,login):
        print("查询：用例3")

    def test_04(self,login): #这里执行后置
        print("查询：用例4")