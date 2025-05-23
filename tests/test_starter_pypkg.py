import pytest

from src.starter_pypkg import add


def test_add_valid():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-5, -3) == -8


def test_add_large_numbers():
    assert add(999999, 1) == 1000000
    assert add(-999999, -1) == -1000000


def test_add_type_error():
    with pytest.raises(TypeError):
        add("1", 2)
    with pytest.raises(TypeError):
        add(1, "2")
    with pytest.raises(TypeError):
        add(None, 2)
