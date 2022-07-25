"""A Greeter that gives a Greeting to a Customer."""
from dataclasses import dataclass
from typing import Protocol
from typing import Type
from typing import cast

from antidote import implements
from antidote import interface

from ..customer import FrenchCustomer


@interface
class Greeter(Protocol):
    """A definition of a MegaStore greeter."""

    name: str


GreeterT = cast(Type[Greeter], Greeter)


@implements(Greeter)
@dataclass
class DefaultGreeter:
    """A person that gives a default greeting."""

    name: str = "Susie"


@implements(Greeter).when(qualified_by=FrenchCustomer)
@dataclass
class FrenchGreeter:
    """A French person that gives a greeting."""

    name: str = "Marie"
