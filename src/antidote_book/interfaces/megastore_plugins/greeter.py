"""A Greeter that gives a Greeting to a Customer."""
from dataclasses import dataclass

from antidote import implements
from antidote import interface


@interface
class Greeter:
    """A definition of a MegaStore greeter."""

    name: str


@implements(Greeter)
@dataclass
class DefaultGreeter(Greeter):
    """A person that gives a greeting."""

    name: str = "Susie"
