"""Do the shallow and deep tests for the lazy_calls example."""

from antidote_book.lazy_calls import Greeter
from antidote_book.lazy_calls import OutsideMessage
from antidote_book.lazy_calls import greeting
from antidote_book.lazy_calls import main


def test_shallow() -> None:
    """Get the main function, run it, ensure results match expected."""
    actual = main()
    assert actual == "Hello, my name is Marie!"


def test_greeting() -> None:
    """Call greeting but pass in ``Greeter``."""
    message = OutsideMessage(punctuation="??")
    greeter = Greeter(name="From Test", message=message)
    actual = greeting(greeter)
    assert actual == "Hello, my name is From Test??"
