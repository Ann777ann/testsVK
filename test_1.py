from utils import i_good, f_good, s_good
import pytest

@pytest.mark.parametrize('a,b, expected_result', [(10, 2,5),
                                         (10, 5, 2),
                                         (-5, -5, 1)])
def test_i_good(a, b, expected_result):
    assert i_good(a,b) == expected_result

def test_i_negative():
    with pytest.raises(TypeError):
        i_good(10,'a')

@pytest.mark.parametrize('c,d, result', [(10.0, 5.0, 2.0),
                                         (10.8, 0.5,21.6)])

def test_f_good(c,d,result):
    assert f_good(c,d) == result

def test_f_negative():
    with pytest.raises(ZeroDivisionError):
        i_good(5.0/0)

def test_s_good():
    assert s_good('a',5) == 'aaaaa'

def test_s_negative():
    with pytest.raises(TypeError):
        s_good('a', 'a')