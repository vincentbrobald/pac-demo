from greet import greet


def test_default():
    """Without a name, greet() greets the world."""
    assert greet() == "Bonjour, world !"


def test_name():
    """A name is greeted as given."""
    assert greet("Tekton") == "Bonjour, Tekton !"


def test_blank_name():
    """A name of only spaces counts as no name."""
    assert greet("   ") == "Bonjour, world !"
