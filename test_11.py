import pytest
@pytest.fixture(params=["参数1","参数2"])
def myfixture(request):
    return request.param
def test_print_param(myfixture):
    print("执⾏test_two")
    print(myfixture)
    assert 1==1