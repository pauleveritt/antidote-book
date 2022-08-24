"""Control caching with singletons off.

By default, Antidote treats injection results as singletons. This
means there can only be one result every produced during the
lifetime of that world.

But sometimes the results vary. For example, information in
the outside world might change in a way that the Antidote world
isn't tracking.

Let's see how to control usage of singletons.
"""
from antidote import inject
from antidote import injectable


GREETER_COUNT: int = 0
COUNTING_GREETER_COUNT: int = 0


@injectable
class Greeter:
    """A person that gives a greeting."""

    salutation: str

    def __init__(self) -> None:
        """Make a salutation with a counter."""
        global GREETER_COUNT
        GREETER_COUNT += 1
        self.salutation = f"({GREETER_COUNT}): Hello!"


@injectable(lifetime="transient")
class CountingGreeter:
    """A variation that keeps a counter every time the factory runs."""

    salutation: str

    def __init__(self) -> None:
        """Make a salutation with a counter."""
        global COUNTING_GREETER_COUNT
        COUNTING_GREETER_COUNT += 1
        self.salutation = f"({COUNTING_GREETER_COUNT}): Hello!"


@inject
def greeting(greeter: Greeter = inject.me()) -> str:
    """Get a `Greeter` and return a greeting."""
    return greeter.salutation


def main() -> str:
    """Process a greeting."""
    return greeting()


if __name__ == "__main__":  # pragma: no cover
    print(main())
