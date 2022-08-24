"""Do the shallow and deep tests for the manual_lookup example."""
from antidote import world

from antidote_book.manual_lookup import Greeter
from antidote_book.manual_lookup import main


def test_shallow() -> None:
    """Get the main function, run it, ensure results match expected."""
    actual = main()
    assert actual == "Hello!"


def test_greeting() -> None:
    """See how Antidote test helpers support isolation."""

    class DummyGreeter:
        """A fake for the config."""

        salutation: str = "Fake Hello"

    with world.test.new() as overrides:
        overrides[Greeter] = DummyGreeter()
        actual = main()
        assert actual == "Fake Hello!"
