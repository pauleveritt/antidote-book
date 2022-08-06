"""A Customer that receives a Greeting from a Greeter."""
from dataclasses import dataclass
from typing import Protocol
from typing import Type
from typing import cast

from antidote import implements
from antidote import interface


@interface
class Customer(Protocol):
    """A definition of a MegaStore customer."""

    name: str


CustomerT = cast(Type[Customer], Customer)


@implements.protocol[Customer]()
@dataclass
class DefaultCustomer:
    """Default implementation of a customer."""

    name: str = "Steve"
