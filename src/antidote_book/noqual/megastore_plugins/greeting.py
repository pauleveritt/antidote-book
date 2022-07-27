"""The message given by a Greeter to a Customer."""
from dataclasses import dataclass
from typing import Protocol
from typing import Type
from typing import cast

from antidote import implements
from antidote import inject
from antidote import injectable
from antidote import interface

from ..megastore.predicates import NotQualified
from .config import MegaStoreConfig
from .customer import Customer
from .customer import FrenchCustomer
from .greeter import Greeter


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


GreetingT = cast(Type[Greeting], Greeting)


@implements(Greeting)
@injectable
@dataclass
class DefaultGreeting:
    """The message given to a customer."""

    customer: Customer = inject.me()
    greeter: Greeter = inject.me(NotQualified())
    punctuation: str = MegaStoreConfig.PUNCTUATION
    salutation: str = "Hello"

    def __call__(self) -> str:
        """Give the text of the greeting."""
        gn = self.greeter.name  # Shorten line
        return f"{self.salutation}, my name is {gn}{self.punctuation}"


@implements(Greeting).when(qualified_by=FrenchCustomer)
@injectable
@dataclass
class FrenchGreeting:
    """The message given to a French customer."""

    customer: Customer = inject.me()
    greeter: Greeter = inject.me(qualified_by=FrenchCustomer)
    punctuation: str = MegaStoreConfig.PUNCTUATION
    salutation: str = "Bonjour"

    def __call__(self) -> str:
        """Give the text of the greeting."""
        gn = self.greeter.name  # Shorten line
        return f"{self.salutation}, je m'appelle {gn}{self.punctuation}"
