"""Simplify our injectable classes using Python dataclasses.

We have a bit of boilerplate in our injectable classes.
Like Antidote, Python's dataclasses are type-hinting-friendly.
Let's use them for our injectables.
"""
from dataclasses import dataclass

from antidote import inject
from antidote import injectable


@injectable
@dataclass
class Greeter:
    """A person that gives a greeting."""

    salutation: str = "Hello"


@inject
def greeting(greeter: Greeter = inject.me()) -> str:
    """Get a `Greeter` and return a greeting."""
    return f"{greeter.salutation}!"


def main() -> str:
    """Process a greeting."""
    return greeting()


if __name__ == "__main__":
    print(main())
