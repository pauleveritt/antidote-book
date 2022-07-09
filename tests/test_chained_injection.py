"""Do the shallow and deep tests for the chained_injection example."""

from antidote_book.chained_injection import Greeter
from antidote_book.chained_injection import Message
from antidote_book.chained_injection import greeting
from antidote_book.chained_injection import main


def test_shallow() -> None:
    """Get the main function, run it, ensure results match expected."""
    actual = main()
    assert actual == "Hello, my name is Marie!"


def test_greeting() -> None:
    """Call greeting but pass in ``Greeter``."""
    message = Message(punctuation="??")
    greeter = Greeter(name="From Test", message=message)
    actual = greeting(greeter)
    assert actual == "Hello, my name is From Test??"
