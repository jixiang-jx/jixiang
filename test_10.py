import pytest
@pytest.fixture(params=["参数1","参数2"])
def myfixture(request):
    print("执⾏testPytest⾥的前置函数，%s" % request.param)