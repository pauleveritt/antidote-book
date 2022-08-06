"""A Greeter that gives a Greeting to a Customer."""
from dataclasses import dataclass
from typing import Protocol
from typing import Type
from typing import cast

from antidote import implements
from antidote import interface


@interface
class Greeter(Protocol):
    """A definition of a MegaStore greeter."""

    name: str


GreeterT = cast(Type[Greeter], Greeter)


@implements.protocol[Greeter]()
@dataclass
class DefaultGreeter:
    """A person that gives a greeting."""

    name: str = "Susie"
