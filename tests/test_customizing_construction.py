"""Do the shallow and deep tests for the customizing_construction example."""
from datetime import datetime

import pytest

from antidote_book.customizing_construction import GreeterBuild
from antidote_book.customizing_construction import GreeterInit
from antidote_book.customizing_construction import GreeterPostInit
from antidote_book.customizing_construction import greeting_build
from antidote_book.customizing_construction import greeting_init
from antidote_book.customizing_construction import greeting_post_init
from antidote_book.customizing_construction import main


@pytest.fixture
def salutation_day_of_week() -> str:
    """Fixture to make a greeting based on day of week."""
    # Get day of the week during the test run
    current_dow = datetime.today().strftime("%A")
    return f"Happy {current_dow}"


def test_shallow(salutation_day_of_week: str) -> None:
    """Get the main function, run it, ensure results match expected."""
    actual = main()
    expected_greeting = salutation_day_of_week + "!"
    expected = (
        expected_greeting,
        expected_greeting,
    )
    assert actual == expected


def test_greeter_init(salutation_day_of_week: str) -> None:
    """Ensure init constructs a correct ``GreeterInit``."""
    greeter_init = GreeterInit(punctuation="??")
    assert greeter_init.salutation == salutation_day_of_week + "??"


def test_greeter_post_init(salutation_day_of_week: str) -> None:
    """Ensure post init constructs a correct ``GreeterPostInit``."""
    greeter_post_init = GreeterPostInit(punctuation="??")
    assert greeter_post_init.salutation == salutation_day_of_week + "??"


def test_greeter_build(salutation_day_of_week: str) -> None:
    """Ensure build method constructs a correct ``Greeter``."""
    greeter_build = GreeterBuild.build(punctuation="??")
    assert greeter_build.salutation == salutation_day_of_week + "??"


def test_greeting_init(salutation_day_of_week: str) -> None:
    """Call greeting but pass in our own ``GreeterInit`` instance."""
    greeter = GreeterInit(punctuation="??")
    actual = greeting_init(greeter)
    assert actual == f"{salutation_day_of_week}??"


def test_greeting_post_init(salutation_day_of_week: str) -> None:
    """Call greeting but pass in our own ``GreeterPostInit`` instance."""
    greeter = GreeterPostInit(punctuation="??")
    actual = greeting_post_init(greeter)
    assert actual == f"{salutation_day_of_week}??"


def test_greeting_build(salutation_day_of_week: str) -> None:
    """Call greeting but pass in our own ``GreeterBuild`` instance."""
    greeter = GreeterBuild.build(punctuation="??")
    actual = greeting_build(greeter)
    assert actual == f"{salutation_day_of_week}??"
