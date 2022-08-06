"""Do the shallow and deep tests for the counter state example."""

from antidote_book.counter_state import counter
from antidote_book.counter_state import greeting
from antidote_book.counter_state import main


def test_shallow() -> None:
    """Get the main function, run it, ensure results match expected."""
    actual = main()
    assert actual == "(1): Hello!"


def test_greeting() -> None:
    """Each time you call greeting, it gets the state and increments."""
    # Each time you call it, the count is the same. In fact, `greeting`
    # doesn't even get called the second time.
    assert greeting() == "(1): Hello!"
    assert greeting() == "(1): Hello!"

    # But when you update the state, it recomputes.
    counter.update()
    assert greeting() == "(2): Hello!"
