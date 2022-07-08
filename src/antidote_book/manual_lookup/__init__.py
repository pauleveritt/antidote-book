"""Use the Antidote `world` to get a dependency manually.

We have a `greeting` function that needs a `Greeter`.
"""
from antidote import injectable
from antidote import world


@injectable
class Greeter:
    """A person that gives a greeting."""

    salutation: str

    def __init__(self, salutation: str = "Hello"):
        """Construct a ``Greeter``."""
        self.salutation = salutation


def greeting() -> str:
    """Get a `Greeter` and return a greeting."""
    greeter = world.get(Greeter)
    return f"{greeter.salutation}!"


def main() -> str:
    """Process a greeting."""
    return greeting()


if __name__ == "__main__":  # pragma: no cover
    print(main())
