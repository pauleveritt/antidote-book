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
from ..customer import ALL_CUSTOMERS
from ..customer import Customer
from ..customer import FrenchCustomer
from ..greeter import Greeter
from ..visit import Visit
from ..visit import VisitHandler


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
    visit: Visit = inject.me(source=VisitHandler)

    def __call__(self) -> str:
        """Give the text of the greeting."""
        gn, p = self.greeter.name, self.punctuation  # Shorten line
        customer = ALL_CUSTOMERS[self.visit.customer_id]
        return f"{self.salutation} {customer.name}, my name is {gn}{p}"


@implements(Greeting).when(qualified_by=FrenchCustomer)
@injectable
@dataclass
class FrenchGreeting:
    """The message given to a French customer."""

    customer: Customer = inject.me()
    greeter: Greeter = inject.me(qualified_by=FrenchCustomer)
    punctuation: str = MegaStoreConfig.PUNCTUATION
    salutation: str = "Bonjour"
    visit: Visit = inject.me(source=VisitHandler)

    def __call__(self) -> str:
        """Give the text of the greeting."""
        gn, p = self.greeter.name, self.punctuation  # Shorten line
        customer = ALL_CUSTOMERS[self.visit.customer_id]
        return f"{self.salutation} {customer.name}, je m'appelle {gn}{p}"
