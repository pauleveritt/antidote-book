"""Move punctuation to a configurable, injectable constant.

Your injectables almost always need some configuration.
Antidote provides an approach for such "constants" with extra touches for
how development works.
"""
from dataclasses import dataclass

from antidote import const
from antidote import inject
from antidote import injectable


class Config:
    """Global settings for this app."""

    PUNCTUATION = const("!")


@injectable
@dataclass
class Greeter:
    """A person that gives a greeting."""

    salutation: str = "Hello"


@inject
def greeting(
    greeter: Greeter = inject.me(),
    punctuation: str = inject[Config.PUNCTUATION],
) -> str:
    """Get a `Greeter` and return greeting with configured punctuation."""
    return f"{greeter.salutation}{punctuation}"


def main() -> str:
    """Process a greeting."""
    return greeting()


if __name__ == "__main__":  # pragma: no cover
    print(main())
