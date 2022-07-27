"""Control caching with singletons off.

By default, Antidote treats injection results as singletons. This
means there can only be one result every produced during the
lifetime of that world.

But sometimes the results vary. For example, information in
the outside world might change in a way that the Antidote world
isn't tracking.

Let's see how to control usage of singletons.
"""
from random import choice

from antidote import inject
from antidote import injectable


PUNCTUATION: tuple[str, ...] = ("!", ".", "!!", "?", "!?", "...", "!!", "?!")


@injectable(scope='singleton')
class Greeter:
    """A person that gives a random greeting."""

    salutation: str

    def __init__(self) -> None:
        """Make a salutation using a random choice."""
        punctuation = choice(PUNCTUATION) + choice(PUNCTUATION)  # noqa: S311
        self.salutation = f"Hello {punctuation}"


@inject
def greeting(greeter: Greeter = inject.me()) -> str:
    """Get a `Greeter` and return a greeting."""
    return greeter.salutation


def main() -> tuple[str, str]:
    """Process a series of greetings with likely different results."""
    first_multi_greeting = greeting()
    second_multi_greeting = greeting()
    return first_multi_greeting, second_multi_greeting


if __name__ == "__main__":  # pragma: no cover
    print(main())
