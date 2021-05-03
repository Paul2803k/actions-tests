import pytest
import main

def test_mult():
    res = main.multiply(3,4)
    assert  res == 3*4
