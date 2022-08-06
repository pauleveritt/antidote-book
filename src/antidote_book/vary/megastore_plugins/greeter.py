"""A Greeter that gives a Greeting to a Customer."""
from dataclasses import dataclass
from typing import Protocol

from antidote import implements
from antidote import interface

from .customer import DefaultCustomer
from .customer import FrenchCustomer


@interface
class Greeter(Protocol):
    """A definition of a MegaStore greeter."""

    name: str


@implements.protocol[Greeter]().when(qualified_by=DefaultCustomer)
@dataclass
class DefaultGreeter:
    """A person that gives a default greeting."""

    name: str = "Susie"


@implements.protocol[Greeter]().when(qualified_by=FrenchCustomer)
@dataclass
class FrenchGreeter:
    """A French person that gives a greeting."""

    name: str = "Marie"
