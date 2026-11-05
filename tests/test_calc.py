from calc import add, mul


def test_add():
    assert add(2, 3) == 5


def test_mul():
    assert mul(2, 3) == 6


def test_sub():
    from calc import sub
    assert sub(5, 3) == 2


def test_div():
    from calc import div
    import pytest
    assert div(6, 3) == 2
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
