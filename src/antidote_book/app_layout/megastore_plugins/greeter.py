"""A Greeter that gives a Greeting to a Customer."""
from dataclasses import dataclass

from antidote import injectable


@injectable
@dataclass
class Greeter:
    """A person that gives a greeting."""

    name: str = "Susie"
