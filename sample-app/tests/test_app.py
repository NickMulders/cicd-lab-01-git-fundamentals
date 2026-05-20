from app import greet


def test_greet_uses_name():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_default_world():
    assert greet("world") == "Hello, world!"


def test_greet_shout():
    assert greet("Ada", shout=True) == "HELLO, ADA!"
