import pytest
from lockatme.unlockers.facial_recognition import facial_recognition

def test_true():
    assert facial_recognition("juju.jpg","juju2.jpg") == True

def test_false():
    assert facial_recognition("juju.jpg","james.jpg") == False
