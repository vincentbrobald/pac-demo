"""Command line: python -m greet [NAME...] prints the greeting for NAME."""
import sys

from greet import greet

print(greet(" ".join(sys.argv[1:])))
