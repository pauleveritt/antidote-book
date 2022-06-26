"""Injectbles can be dataclasses."""
from dataclasses import dataclass

from antidote import inject, injectable


@injectable
@dataclass
class Greeter:
    salutation: str = "Hello"


@inject
def greeting(greeter: Greeter = inject.me()) -> str:
    """Get a `Greeter` and return a greeting."""
    return f'{greeter.salutation}!'


def main():
    return greeting()
