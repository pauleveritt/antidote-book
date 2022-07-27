"""The message given by a Greeter to a Customer."""
from dataclasses import dataclass

from antidote import implements
from antidote import inject
from antidote import interface

from .config import MegaStoreConfig
from .customer import Customer
from .greeter import Greeter


@interface
class Greeting:
    """A definition of a MegaStore greeting."""

    customer: Customer
    greeter: Greeter
    punctuation: str
    salutation: str

    def __call__(self) -> str:
        """Definition of the call method."""
        return ""


@implements(Greeting)
@dataclass
class DefaultGreeting(Greeting):
    """The message given to a customer."""

    customer: Customer = inject.me()
    greeter: Greeter = inject.me()
    punctuation: str = MegaStoreConfig.PUNCTUATION
    salutation: str = "Hello"

    def __call__(self) -> str:
        """Give the text of the greeting."""
        gn = self.greeter.name  # Shorten line
        return f"{self.salutation}, my name is {gn}{self.punctuation}"
