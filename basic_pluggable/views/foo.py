from dataclasses import dataclass
from typing import Callable, Type, TypeVar, Protocol

from antidote import implements, interface, world


@interface
class View:
    name: str

    def __html__(self) -> str:
        ...


V = TypeVar('V', bound=Type[View])


def view(context: object) -> Callable[[V], V]:
    def decorate(cls: V) -> V:
        implements(View).when(qualified_by=context)(cls)
        return cls

    return decorate


class Resource(Protocol):
    name: str


@dataclass
class Customer:
    name: str


@dataclass
class Store:
    name: str


@view(context=Customer)
@dataclass
class CustomerView(View):
    name: str = "Customer View"

    def __html__(self) -> str:
        return f'Hello {self.name}'


@view(context=Store)
@dataclass
class StoreView(View):
    name: str = "Store View"

    def __html__(self) -> str:
        return f'Welcome to {self.name}'


def get_view(context_type: object) -> str:
    """Find the correct view and render it."""
    this_view = world.get[View].single(qualified_by=context_type)
    result = this_view.__html__()
    return result


if __name__ == '__main__':
    print(get_view(Store))
