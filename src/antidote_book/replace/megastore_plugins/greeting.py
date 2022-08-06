"""The message given by a Greeter to a Customer."""
from dataclasses import dataclass
from typing import Protocol

from antidote import implements
from antidote import inject
from antidote import interface

from .config import MegaStoreConfig
from .customer import Customer
from .greeter import Greeter
from .salutation import Salutation


@interface
class Greeting(Protocol):
    """A definition of a MegaStore greeting."""

    customer: Customer
    greeter: Greeter
    punctuation: str
    salutation: str

    def __call__(self) -> str:
        """Definition of the call method."""
        ...


@implements.protocol[Greeting]()
@dataclass
class DefaultGreeting:
    """The message given to a customer."""

    customer: Customer = inject.me()
    greeter: Greeter = inject.me()
    punctuation: str = inject[MegaStoreConfig.PUNCTUATION]
    salutation: Salutation = inject.me()

    def __call__(self) -> str:
        """Give the text of the greeting."""
        gn = self.greeter.name  # Shorten line
        return f"{self.salutation}, my name is {gn}{self.punctuation}"
