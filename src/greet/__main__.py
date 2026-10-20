"""Command line: python -m greet [NAME...] prints the greeting for NAME."""
import sys

from greet import greet

# Several arguments form one name ("python -m greet Ada Lovelace").
print(greet(" ".join(sys.argv[1:])))
