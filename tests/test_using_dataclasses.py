"""Do the shallow and deep tests for the using_dataclasses example."""

from antidote_book.using_dataclasses import Greeter
from antidote_book.using_dataclasses import greeting
from antidote_book.using_dataclasses import main


def test_shallow() -> None:
    """Get the main function, run it, ensure results match expected."""
    actual = main()
    assert actual == "Hello!"


def test_greeting() -> None:
    """Call greeting but pass in our own ``Greeter`` instance."""
    greeter = Greeter(salutation="From Test")
    actual = greeting(greeter)
    assert actual == "From Test!"
