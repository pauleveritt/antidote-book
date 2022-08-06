"""Do the shallow and deep tests for the props example."""

from antidote_book.props import Greeter
from antidote_book.props import main


def test_shallow() -> None:
    """Get the main function, run it, ensure results match expected."""
    actual = main()
    assert actual == "(1): Hello Marie!"


def test_greeting() -> None:
    """Manually pass in dependencies."""
    greeter = Greeter()
    assert greeter() == "(1): Hello Marie!"
