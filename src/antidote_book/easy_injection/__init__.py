from antidote import inject, injectable


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
