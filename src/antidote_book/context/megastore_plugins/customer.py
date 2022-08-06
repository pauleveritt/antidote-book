"""A Customer that receives a Greeting from a Greeter."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from antidote import implements
from antidote import interface

from antidote_book.context.megastore.predicates import NotQualified


@interface
class Customer(Protocol):
    """A definition of a MegaStore customer."""

    name: str


@implements.protocol[Customer]().when(qualified_by=NotQualified)
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
