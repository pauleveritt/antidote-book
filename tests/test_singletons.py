"""Do the shallow and deep tests for the singletons example."""
from antidote import world

from antidote_book.singletons import CountingGreeter
from antidote_book.singletons import Greeter
from antidote_book.singletons import main


def test_shallow() -> None:
    """Get the main function, run it, ensure results match expected."""
    actual = main()
    assert actual == "(1): Hello!"


def test_greeter_singleton() -> None:
    """By default, ``@injectable`` is a singleton. Prove it."""
    # This increases the counter
    greeter1 = world[Greeter]
    # This doesn't increase the counter
    greeter2 = world[Greeter]
    assert greeter1.salutation == "(1): Hello!"
    assert greeter2.salutation == "(1): Hello!"


def test_greeter_not_singleton() -> None:
    """Replace Greeter with as a non-singleton."""
    greeter1 = world[CountingGreeter]
    # This next line increases to 2, as we are making a new
    # ``CountingGreeter``. It isn't a singleton.
    greeter2 = world[CountingGreeter]
    assert greeter1.salutation == "(1): Hello!"
    assert greeter2.salutation == "(2): Hello!"
