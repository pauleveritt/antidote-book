"""Manage a counter with ``@state``."""
from dataclasses import dataclass

from antidote import inject
from antidote import injectable
from antidote.core import unscoped


@unscoped
def counter(previous: int | None) -> int:
    """Return and increment the counter."""
    return (previous or 0) + 1


@injectable
@dataclass
class Greeter:
    """A person that gives a random greeting."""

    salutation: str = "Hello!"


@inject
def greeting(
    greeter: Greeter = inject.me(),
    count: int = inject[counter],
) -> str:
    """Get a `Greeter` and return a greeting."""
    return f"({count}): {greeter.salutation}"


def main() -> str:
    """Process a greeting."""
    return greeting()


if __name__ == "__main__":  # pragma: no cover
    print(main())
