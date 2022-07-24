"""A Greeter that gives a Greeting to a Customer."""
from dataclasses import dataclass
from typing import Protocol

from antidote import implements
from antidote import interface


@interface
class Greeter(Protocol):
    """A definition of a MegaStore greeter."""

    name: str


@implements(Greeter)
@dataclass
class DefaultGreeter:
    """A person that gives a greeting."""

    name: str = "Susie"
