import pytest

from src.main import hello_world

def test_hello_world():
    assert hello_world() == "Hello World!"