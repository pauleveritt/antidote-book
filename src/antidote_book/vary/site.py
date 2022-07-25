"""A local site installation for a store."""

from .megastore import get_greeting


def main() -> str:
    """This is the "main loop" for the pluggable app."""
    return get_greeting()
