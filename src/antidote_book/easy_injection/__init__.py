"""Get dependency through injection.

In the previous example we manually retrieved our ``Greeter`` from the
``world``. In this example we state our dependency in our function
parameters and ask Antidote to retrieve it for us.
"""
from antidote import inject
from antidote import injectable


@injectable
class Greeter:
    """A person that gives a greeting."""

    salutation: str

    def __init__(self, salutation: str = "Hello"):
        """Construct a ``Greeter``."""
        self.salutation = salutation


@inject
def greeting(greeter: Greeter = inject.me()) -> str:
    """Get a `Greeter` and return a greeting."""
    return f"{greeter.salutation}!"


def main() -> str:
    """Process a greeting."""
    return greeting()


if __name__ == "__main__":
    print(main())
