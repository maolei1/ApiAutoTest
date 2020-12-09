'''
mark标记：
1、跳过用例，某个版本有缺陷导致脚本执行不通过，可以跳过改用例，待缺陷解决后再执行
2、脚本越来越多，如果想执行其中一部分脚本怎么办？使用自定义标记
   全量的脚本，挑选了一部分作为冒烟测试的脚本，只想执行冒烟测试这部分的脚本
'''

import pytest

@pytest.mark.smoke  #自定义的标记
def test_01():
    print("测试用例1")

@pytest.mark.skip("跳过原因：尚未支持的功能，暂不执行，待实现后再执行")
def test_02():
    print("测试用例2")

@pytest.mark.smoke
def test_03():
    print("测试用例3")
@pytest.mark.api
def test_04():
    print("测试用例4")

@pytest.mark.api
class TestMark:
    def test_011(self):
        print("测试用例11")

    @pytest.mark.smoke
    def test_012(self):
        print("测试用例12")

    def test_013(self):
        print("测试用例13")

    @pytest.mark.smoke
    def test_014(self):
        print("测试用例14")

'''
; -m=smoke 执行smoke标记的用例
; -m="smoke and api" 执行既有smoke又有api标记的用例
; -m="smoke or api" 执行有smoke或者api标记的用例
; -m="not smoke" 执行非smoke标记的用例
'''