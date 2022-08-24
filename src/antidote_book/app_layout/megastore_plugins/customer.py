"""A Customer that receives a Greeting from a Greeter."""
from dataclasses import dataclass

from antidote import injectable


@injectable
@dataclass
class Customer:
    """A person that receives a greeting."""

    name: str = "Steve"
