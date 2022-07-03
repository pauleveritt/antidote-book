"""A framework which provides default implementations."""
from typing import Type, Protocol, TypeVar, Callable

from antidote import QualifiedBy, world
from antidote.lib.interface.interface import implements, interface


@interface
class View:
    pass


V = TypeVar('V', bound=Type[View])


def view(context: object) -> Callable[[V], V]:
    def decorate(cls: V) -> V:
        implements(View).when(qualified_by=context)(cls)
        return cls

    return decorate


Customer = object()
# Store = object()


@view(context=Customer)
class CustomerView(View):
    name: str = "View Impl"

#
# @view(context=Store)
# class StoreView(View):
#     name: str = "Store Impl"


class Customer:
    name: str = "Fred"


@interface
class Greeter(Protocol):
    """A way to talk about all variations of a `Greeter`."""
    name: str
    salutation: str


@implements(Greeter).when(QualifiedBy(Customer))
class DefaultGreeter:
    """The bundled `Greeter`."""
    name: str = "Fred"
    salutation: str = "Hello"


def greeting(customer_type: Type[Customer]) -> str:
    """Get a `Greeter` and return a greeting."""
    greeter = world.get[Greeter].single(QualifiedBy(customer_type))
    return f"{greeter.salutation}, my name is {greeter.name}!"


def get_view() -> str:
    """Find the correct view and render it."""
    this_view = world.get[View].single(qualified_by=Customer)
    result = "result"
    return result


if __name__ == '__main__':
    get_view()
