"""Pass "props" as per-invocation construction values.``."""
# from dataclasses import dataclass
# from typing import Any
# from typing import Callable
# from typing import ParamSpec
# from typing import Protocol
# from typing import Type
# from typing import TypeAlias
# from typing import TypeVar
#
# from antidote import ScopeVar
# from antidote import const
# from antidote import implements
# from antidote import inject
# from antidote import interface
# from antidote import lazy
# from antidote import world
# from antidote.lib.interface import NeutralWeight
# from antidote.lib.interface._function import LazyInterfaceImpl
# from antidote.lib.interface.interface import LazyInterface
#
#
# @dataclass
# class Request:
#     """Information from the outside world for this transaction."""
#
#     path: str
#
#
# @dataclass
# class Resource:
#     """The entity being processed."""
#
#     title: str
#
#
# @dataclass
# class Invoice(Resource):
#     """A specific kind of entity."""
#
#     pass
#
#
# @dataclass
# class Customer(Resource):
#     """Another specific kind of entity."""
#
#     pass
#
#
# current_request = ScopeVar[Request]()
# context = ScopeVar[Resource]()
#
#
# class Config:
#     """The configuration of the site."""
#
#     site_title = const("This Site")
#
#
# @dataclass
# class ExpectedResource:
#     """A discriminator."""
#
#     resource: Type[Resource]
#
#     def weight(self) -> NeutralWeight:
#         """Give a weight calculation for this predicate usage."""
#         return NeutralWeight()
#
#
# @interface
# def base_view(title: str | None = ...) -> str:
#     """Generic definition of a view."""
#     ...
#
#
# VDOM: TypeAlias = str
#
#
# @interface
# def base_component(title: str | None = ...) -> VDOM:
#     """Generic definition of a component."""
#     ...
#
#
# class BaseComponent(Protocol):
#     """Another generic definition of a component."""
#
#     def __call__(self, title: str | None = ...) -> VDOM:
#         """Render a component."""
#         ...
#
#
# def view(resource_type: Type[Resource] | None = None) -> Any:
#     """The decorator that turns a callable into a view."""
#     if resource_type is None:
#         return implements(base_view).by_default
#     return implements(base_view).when(ExpectedResource(resource_type))
#
#
# def component(resource_type: Type[Resource] | None = None) -> Any:
#     """The decorator that turns a callable into a component."""
#     if resource_type is None:
#         return implements(base_component).by_default
#     return implements(base_component).when(ExpectedResource(resource_type))
#
#
# @view()
# def default_view(title: str = "Default View") -> str:
#     """Use this as the view when nothing else matches."""
#     return title
#
#
# @view(Invoice)
# def invoice_view(title: str = "Invoice View") -> str:
#     """A view for a particular entity."""
#     return "Invoice"
#
#
# @inject
# def is_expected_resource(
#     predicate: ExpectedResource | None, resource: Resource = inject[context]
# ) -> bool:
#     """The predicate for matching the current context."""
#     if predicate is None:
#         return False
#     return isinstance(resource, predicate.resource)
#
#
# @inject
# def show_view(
#     my_view: Callable[[], str] = inject[base_view.single(is_expected_resource)]
# ) -> None:
#     """Create an instance of a view."""
#     print(my_view())
#
#
# @inject
# def show_component(
#     my_component: BaseComponent = inject[base_component.single(is_expected_resource)],
# ) -> None:
#     """Create an instance of a component."""
#     print(my_component(title="From Inside"))
#
#
# P = ParamSpec("P")
# Out = TypeVar("Out")
#
#
# def show(
#     __component: LazyInterfaceImpl[P, Out], *args: P.args, **kwargs: P.kwargs
# ) -> Out:
#     """Lookup and create an instance."""
#     return world[__component.single(is_expected_resource)](*args, **kwargs)
#
#
# @lazy
# def get(attr: str, cr: Request = inject[current_request]) -> str | None:
#     """Shorthand operator."""
#     return getattr(cr, attr, None)
#
#
# @component()
# def Greeting(
#     title: str = "Greeting",
#     # TODO mypy complains that get returns Dependency[str]
#     this_path: str = get("path"),  # type: ignore
#     salutation: str = "Hello",
# ) -> VDOM:
#     """A specific component."""
#     return f"{title} -- {this_path} {salutation}"
#
#
# @component(Invoice)
# def InvoiceGreeting(
#     title: str = "Invoice Greeting",
#     # TODO mypy complains that get returns Dependency[str]
#     this_path: str = get("path"),  # type: ignore
# ) -> VDOM:
#     """Get a `Greeter` and return a greeting."""
#     return f"{title} -- {this_path}"
#
#
# def main() -> str:
#     """Process a greeting."""
#     current_request.set(Request(path="/book"))
#     context.set(Resource("book"))
#     show_view()
#     show_component()
#     print("###", show(base_component, title="hello"))
#     print("###", show(base_component))
#
#     context.set(Invoice("invoice"))
#     current_request.set(Request(path="/invoice"))
#     show_view()
#     show_component()
#
#     context.set(Customer("customer"))
#     current_request.set(Request(path="/customer"))
#     show_view()
#     show_component()
#
#     return "(1): Hello Marie!"
#
#
# if __name__ == "__main__":  # pragma: no cover
#     main()
