from greet import greet


def test_default():
    assert greet() == "Bonjour, world !"


def test_name():
    assert greet("Tekton") == "Bonjour, Tekton !"


def test_blank_name():
    assert greet("   ") == "Bonjour, world !"
