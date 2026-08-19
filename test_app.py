from app import add, greet

def test_add():
    assert add(2, 3) == 99 # deliberate failure


def test_greet():
    assert greet("World") == "Hello, World!"
