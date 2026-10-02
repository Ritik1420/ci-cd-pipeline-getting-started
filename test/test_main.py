from src.main import add 

def test_add_function():
    assert add(2, 3) == 5
    assert add(-1, 1) == 2
    assert add(0, 0) == 0

def test_sanity():
    assert 1 + 1 == 0