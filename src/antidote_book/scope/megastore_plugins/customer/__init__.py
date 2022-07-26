"""A Customer that receives a Greeting from a Greeter."""
from __future__ import annotations

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


@implements(Customer)
@dataclass
class DefaultCustomer:
    """Default implementation of a customer."""

    name: str = "Steve"


@dataclass
class FrenchCustomer:
    """Default implementation of a French customer."""

    name: str = "Jean"


ALL_CUSTOMERS: dict[str, Customer] = dict(
    steve=DefaultCustomer(name="Steve"),
    jean=FrenchCustomer(name="Jean"),
)
