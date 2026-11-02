from greeter import greet, greet_all

def test_greet_with_name():
    assert greet("Ada") == "Hello, Ada!"

def test_greet_with_empty_string():
    assert greet("") == "Hello, stranger!"

def test_greet_with_none():
    assert greet(None) == "Hello, stranger!"

def test_greet_all():
    assert greet_all(["Ada", "Izzy"]) == "Hello, Ada, Izzy!"