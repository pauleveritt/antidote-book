"""Do the shallow and deep tests for the without_singletons example."""

from antidote_book.without_singletons import Greeter
from antidote_book.without_singletons import greeting
from antidote_book.without_singletons import main


def test_shallow() -> None:
    """Get the main function, run it, ensure results match expected."""
    actual = main()
    assert actual[0] != actual[1]


def test_greeting() -> None:
    """Call greeting but pass in our own ``Greeter`` instance."""
    greeter = Greeter()
    actual = greeting(greeter)
    assert actual == greeter.salutation
