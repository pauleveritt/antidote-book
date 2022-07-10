"""Do the shallow and deep tests for the manual_lookup example."""
import pytest
from antidote import world
from antidote.core.exceptions import DependencyNotFoundError

from antidote_book.manual_lookup import Greeter
from antidote_book.manual_lookup import greeting
from antidote_book.manual_lookup import main


def test_shallow() -> None:
    """Get the main function, run it, ensure results match expected."""
    actual = main()
    assert actual == "Hello!"


def test_world_setup() -> None:
    """See how Antidote test helpers support isolation."""
    with world.test.clone():
        # Works in a clone of the already-setup world
        actual = main()
        assert actual == "Hello!"
    with world.test.empty():
        # In an empty world, no registration for `Greeting`.
        with pytest.raises(DependencyNotFoundError) as exc:
            main()
        assert str(exc.value) == "antidote_book.manual_lookup.Greeter"
    with world.test.clone():
        # Try it again, back to clone of the original
        actual = main()
        assert actual == "Hello!"


class DummyGreeter:
    """A fake for the config."""

    salutation: str

    def __init__(self, salutation: str = "Fake Hello"):
        """Construct a fake ``Greeter``."""
        self.salutation = salutation


def test_greeting() -> None:
    """Use Antidote test helpers to set up a world."""
    with world.test.clone():
        dummy_greeter = DummyGreeter()
        world.test.override.singleton(Greeter, dummy_greeter)
        actual = greeting()
        assert actual == "Fake Hello!"
