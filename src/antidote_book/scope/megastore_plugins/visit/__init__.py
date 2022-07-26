"""Represent outside data for a customer visit."""
from dataclasses import dataclass

from antidote import factory
from antidote import world


VISIT_SCOPE = world.scopes.new(name="visit")


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
        assert self.__visit is not None
        return self.__visit

    def set_customer_id(self, value: str) -> None:
        """Record the customer ID of the current visiting customer."""
        self.__visit = Visit(customer_id=value)
        world.scopes.reset(VISIT_SCOPE)
