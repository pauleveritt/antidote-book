"""A Customer that receives a Greeting from a Greeter."""
from dataclasses import dataclass
from typing import Protocol

from antidote import implements
from antidote import interface


@interface
class Customer(Protocol):
    """A definition of a MegaStore customer."""

    name: str


@implements.protocol[Customer]()
@dataclass
class DefaultCustomer:
    """Default implementation of a customer."""

    name: str = "Steve"
