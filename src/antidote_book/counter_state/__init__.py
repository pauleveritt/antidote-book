"""Manage a counter with ``@state``."""
from dataclasses import dataclass

from antidote import ScopeVar
from antidote import inject
from antidote import injectable


counter = ScopeVar[int]()


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
    counter.set(1)
    return greeting()


if __name__ == "__main__":  # pragma: no cover
    print(main())
