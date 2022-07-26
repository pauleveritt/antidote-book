"""The message given by a Greeter to a Customer."""
from dataclasses import dataclass
from typing import Protocol
from typing import Type
from typing import cast

from antidote import implements
from antidote import inject
from antidote import injectable
from antidote import interface

from ...megastore.predicates import NotQualified
from ..config import MegaStoreConfig
from ..customer import Customer
from ..customer import FrenchCustomer
from ..greeter import Greeter
from ..visit import get_context


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

    customer: Customer = get_context()
    greeter: Greeter = inject.me(NotQualified())
    punctuation: str = MegaStoreConfig.PUNCTUATION
    salutation: str = "Hello"

    def __call__(self) -> str:
        """Give the text of the greeting."""
        gn, p = self.greeter.name, self.punctuation  # Shorten line
        return f"{self.salutation} {self.customer.name}, my name is {gn}{p}"


@implements(Greeting).when(qualified_by=FrenchCustomer)
@injectable
@dataclass
class FrenchGreeting:
    """The message given to a French customer."""

    customer: Customer = get_context()
    greeter: Greeter = inject.me(qualified_by=FrenchCustomer)
    punctuation: str = MegaStoreConfig.PUNCTUATION
    salutation: str = "Bonjour"

    def __call__(self) -> str:
        """Give the text of the greeting."""
        gn, p = self.greeter.name, self.punctuation  # Shorten line
        return f"{self.salutation} {self.customer.name}, je m'appelle {gn}{p}"
