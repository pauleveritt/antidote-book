"""Customizing the creation of injected instances.

Antidote will construct your injected instances for you. But sometimes
you need more control. Fortunately, Antidote gives you some hook points
to specify the logic used for construction.
"""
from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime

from antidote import const
from antidote import inject
from antidote import injectable


class Config:
    """Global settings for this app."""

    PUNCTUATION = const("!")


@injectable
class GreeterInit:
    """A person that gives a greeting using injection in init."""

    salutation: str

    def __init__(self, punctuation: str = inject[Config.PUNCTUATION]) -> None:
        """Use init injection to custom construct."""
        dow = datetime.today().strftime("%A")
        self.salutation = f"Happy {dow}{punctuation}"


@injectable
@dataclass
class GreeterPostInit:
    """A person that gives a greeting using injection then post init."""

    punctuation: str = inject[Config.PUNCTUATION]
    salutation: str = field(init=False)

    def __post_init__(self) -> None:
        """Use post init injection to custom construct."""
        dow = datetime.today().strftime("%A")
        self.salutation = f"Happy {dow}{self.punctuation}"


@injectable(factory_method="build")
@dataclass
class GreeterBuild:
    """A person that gives a greeting using ``factory_method``."""

    salutation: str

    @classmethod
    def build(cls, punctuation: str = inject[Config.PUNCTUATION]) -> GreeterBuild:
        """Customize the creation of instances."""
        dow = datetime.today().strftime("%A")
        salutation = f"Happy {dow}{punctuation}"
        return cls(salutation=salutation)


@inject
def greeting_init(greeter: GreeterInit = inject.me()) -> str:
    """Get a `GreeterInit` and return a greeting."""
    return f"{greeter.salutation}"


@inject
def greeting_post_init(greeter: GreeterPostInit = inject.me()) -> str:
    """Get a `GreeterPostInit` and return a greeting."""
    return f"{greeter.salutation}"


@inject
def greeting_build(greeter: GreeterBuild = inject.me()) -> str:
    """Get a `GreeterBuild` and return a greeting."""
    return f"{greeter.salutation}"


def main() -> tuple[str, str]:
    """Process a greeting."""
    return (
        greeting_init(),
        greeting_build(),
    )


if __name__ == "__main__":  # pragma: no cover
    print(main())
