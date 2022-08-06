"""Pass "props" as per-invocation construction values.``."""
from dataclasses import dataclass

from antidote import inject
from antidote import injectable
from antidote import unscoped


@unscoped
def counter(previous: int | None) -> int:
    """Return and increment the counter."""
    return (previous or 0) + 1


@injectable(scope="bound")
@dataclass
class Greeter:
    """A person that gives a random greeting."""

    counter: int = inject[counter]
    salutation: str = "Hello"

    def __call__(self, customer_name: str = "Default") -> str:
        """Return a greeting."""
        customer_name = "Marie"
        return f"({self.counter}): {self.salutation} {customer_name}!"


@inject
def greeting(
    greeter: Greeter = inject.me(),
) -> str:
    """Get a `Greeter` and return a greeting."""
    return greeter()


def main() -> str:
    """Process a greeting."""
    return greeting()


if __name__ == "__main__":  # pragma: no cover
    print(main())
