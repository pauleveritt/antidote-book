"""Use lazy as a factory function to integrate external classes.

Sometimes your code uses a class that you don't control, for
example from an installed library. If it doesn't have `injectable`,
you can't inject, it, right?
"""
from dataclasses import dataclass

from antidote import const
from antidote import inject
from antidote import injectable
from antidote import lazy


class Config:
    """Global settings for this app."""

    PUNCTUATION = const("!")


@dataclass
class OutsideMessage:
    """The message to give in the greeting."""

    salutation: str = "Hello"
    punctuation: str = "..."


@lazy
def outside_message(punctuation: str = Config.PUNCTUATION) -> OutsideMessage:
    """Register and construct an ``OutsideMessage``."""
    return OutsideMessage(punctuation=punctuation)


@injectable
@dataclass
class Greeter:
    """A person that gives a greeting."""

    name: str = "Marie"
    message: OutsideMessage = outside_message()


@inject
def greeting(
    greeter: Greeter = inject.me(),
) -> str:
    """Get a `Greeter` and return the greeting."""
    g = greeter.message
    salutation, punctuation = g.salutation, g.punctuation
    return f"{salutation}, my name is {greeter.name}{punctuation}"


def main() -> str:
    """Process a greeting."""
    return greeting()


if __name__ == "__main__":  # pragma: no cover
    print(main())
