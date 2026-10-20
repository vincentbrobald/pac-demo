"""Tiny library used to demonstrate CI with Tekton Pipelines-as-Code."""


def greet(name: str = "world") -> str:
    """Return a greeting for name; a blank name greets the world."""
    name = name.strip() or "world"
    return f"Bonjour, {name} !"
