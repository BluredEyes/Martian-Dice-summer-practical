import json
from dice import Dice

def test_init():
    c = Dice()
    assert c.current_side in [1, 2, 3, 4, 5, 6]
    a = Dice(5)
    assert a.current_side == 5

def test_repr():
    c = Dice(3)
    assert type(c) == Dice

def test_save():
    c = Dice(5)
    c.save()
    with open('data1.json', 'r') as file:
        a = json.load(file)
    assert a == {"current_side":c.current_side}
    assert type(a) == dict

def test_load():
    c = Dice(2)
    c = c.load(1)
    assert c.current_side == 1
