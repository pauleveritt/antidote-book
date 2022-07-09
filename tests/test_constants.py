"""Do the shallow and deep tests for the constants example."""

from antidote_book.constants import Greeter
from antidote_book.constants import greeting
from antidote_book.constants import main


def test_shallow() -> None:
    """Get the main function, run it, ensure results match expected."""
    actual = main()
    assert actual == "Hello!"


def test_greeting() -> None:
    """Call greeting but pass in ``Greeter`` and ``punctuation``."""
    greeter = Greeter(salutation="From Test")
    punctuation = "??"
    actual = greeting(greeter, punctuation)
    assert actual == "From Test??"
