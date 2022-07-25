"""Represent outside data for a customer visit."""
from dataclasses import dataclass, field
from random import randint
from typing import Protocol

from antidote import (
    world,
    inject,
    interface,
    implements,
    QualifiedBy,
    factory,
)

VISIT_SCOPE = world.scopes.new(name="visit")


@dataclass
class Customer:
    name: str = "Fred"


@dataclass(frozen=True)
class Visit:
    customer: Customer


@factory(scope=VISIT_SCOPE)
class VisitHandler:
    def __init__(self):
        self.__visit = None

    def __call__(self) -> Visit:
        print("In the VisitHandler call")
        assert self.__visit is not None
        return self.__visit

    def set_customer(self, customer: Customer) -> None:
        self.__visit = Visit(customer=customer)
        world.scopes.reset(VISIT_SCOPE)


@interface
class Greeter(Protocol):
    """A way to talk about all variations of a `Greeter`."""

    name: str
    greeting: str


@implements(Greeter).when(QualifiedBy(Customer))
@dataclass
class DefaultGreeter:
    """The bundled `Greeter`."""

    name: str = "Fred"
    greeting: str = field(init=False)

    def __post_init__(self):
        marker = randint(0, 99999)
        self.greeting = f"Hello {self.name} {marker}"


@inject
def greeting(visit: Visit = inject.me(source=VisitHandler)) -> str:
    """Get a `Greeter` for a ``Customer`` and return a greeting."""
    customer_type = visit.customer.__class__
    greeter = world.get[Greeter].single(QualifiedBy(customer_type))
    return greeter.greeting
    # return f"{greeter.salutation}, my name is {greeter.name}!"


@inject
def handle_visit(
    customer: Customer,
    visit_handler: VisitHandler = inject.me(),
) -> str:
    """Reset scope to use current customer and return greeting."""
    visit_handler.set_customer(customer=customer)
    print(f"***** {greeting()}")
    return greeting()


if __name__ == "__main__":
    for n in ["John", "Jill", "Marie"]:
        c = Customer(name=n)
        g = handle_visit(c)
        print(g)
