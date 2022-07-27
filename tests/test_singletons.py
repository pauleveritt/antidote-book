"""Do the shallow and deep tests for the singletons example."""

from antidote_book.singletons import Greeter
from antidote_book.singletons import greeting
from antidote_book.singletons import main


def test_shallow() -> None:
    """Get the main function, run it, ensure results match expected."""
    actual = main()
    assert actual[0] == actual[1]


def test_greeting() -> None:
    """Call greeting but pass in our own ``Greeter`` instance."""
    greeter = Greeter()
    actual = greeting(greeter)
    assert actual == greeter.salutation
