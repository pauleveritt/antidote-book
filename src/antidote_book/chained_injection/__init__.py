"""Multi-step dependencies are injected correctly.

Injection can depend on something which depends on something. Antidote
is quite good at these "transitive dependencies". Let's take a look at
representing a multistep dependency.
"""
from dataclasses import dataclass

from antidote import const
from antidote import inject
from antidote import injectable


class Config:
    """Global settings for this app."""

    PUNCTUATION = const("!")


@injectable  # inject Message
@dataclass
class Message:
    """The message to give in the greeting."""

    salutation: str = "Hello"
    punctuation: str = Config.PUNCTUATION


@injectable  # inject Greeter
@dataclass
class Greeter:
    """A person that gives a greeting."""

    name: str = "Marie"
    message: Message = inject.me()


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
