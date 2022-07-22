"""A Customer that receives a Greeting from a Greeter."""
from dataclasses import dataclass

from antidote import implements
from antidote import interface


@interface
class Customer:
    """A definition of a MegaStore customer."""

    name: str


@implements(Customer)
@dataclass
class DefaultCustomer(Customer):
    """Default implementation of a customer."""

    name: str = "Steve"
