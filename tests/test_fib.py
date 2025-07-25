from src.fib import fib

def test_fib0():
    # test edge 0
    obs = fib(0)
    assert obs == 0

def test_fib1():
    # test edge 1
    obs = fib(1)
    assert obs == 1

def test_fib6():
    # test internal point
    obs = fib(6)
    assert obs == 8

def test_fib_negative():
    # test negative input
    obs = fib(-1)
    assert obs == NotImplemented

def test_fib_nonint():
    # test non-integer input
    obs = fib(2.5)
    assert obs == NotImplemented