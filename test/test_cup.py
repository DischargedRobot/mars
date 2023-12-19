import pytest
from cup import Cup

def test_repr():
    c = Cup(13)
    assert repr(c) == "Количество кубиков: 13"
def test_init():
    c = Cup(13)
    assert c.numbers == 13
def test_delite_creature():
    c = Cup(13)
    c.cast()
    lis = c.list_cup
    for i in range(lis.count('корова')):
        lis.remove('корова')
    assert lis == c.delite_creature('корова')

