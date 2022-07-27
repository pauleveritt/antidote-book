"""Represent outside data for a customer visit."""
from dataclasses import dataclass

from antidote import factory
from antidote import inject
from antidote import lazy
from antidote import world

from .customer import ALL_CUSTOMERS
from .customer import Customer


VISIT_SCOPE = world.scopes.new(name="visit2")

Context = Customer


@dataclass(frozen=True)
class Visit:
    """Data used for a customer visit."""

    customer_id: str


@factory(scope=VISIT_SCOPE)
@dataclass
class VisitHandler:
    """Stateful factory to represent visit data within a scope."""

    __visit: Visit | None = None

    def __call__(self) -> Visit:
        """Give Antidote access to the current visit value."""
        if self.__visit is None:
            raise ValueError("VisitHandler needs a customer.")
        return self.__visit

    def set_customer_id(self, value: str) -> None:
        """Record the customer ID of the current visiting customer."""
        self.__visit = Visit(customer_id=value)
        world.scopes.reset(VISIT_SCOPE)


@lazy(scope=VISIT_SCOPE)
def get_context(
    visit: Visit = inject.me(source=VisitHandler),
) -> Context:
    """A factory to retrieve the current context from the database."""
    return ALL_CUSTOMERS[visit.customer_id]
