"""Do the shallow and deep tests for the example."""
import pytest
from antidote import inject
from antidote import instanceOf
from antidote import world

from antidote_book.context.megastore.predicates import NotQualified
from antidote_book.context.megastore_plugins.config import MegaStoreConfig
from antidote_book.context.megastore_plugins.customer import Customer
from antidote_book.context.megastore_plugins.customer import FrenchCustomer
from antidote_book.context.megastore_plugins.greeter import Greeter
from antidote_book.context.megastore_plugins.greeting import Greeting
from antidote_book.context.megastore_plugins.visit import VisitHandler
from antidote_book.context.megastore_plugins.visit import get_context
from antidote_book.context.site import main


def test_config() -> None:
    """Ensure MegaStore has config-driven injectable punctuation."""

    @inject
    def get_punctuation(punctuation: str = inject[MegaStoreConfig.PUNCTUATION]) -> str:
        return punctuation

    this_punctuation = get_punctuation()
    assert this_punctuation == "!"


def test_customer() -> None:
    """Ensure the world can make a ``Customer`` from dependencies."""
    customer = world[instanceOf[Customer]]
    assert customer.name == "Steve"


def test_default_greeter() -> None:
    """Ensure the world can make a ``Greeter`` from dependencies."""
    greeter = world[instanceOf[Greeter]().single(qualified_by=NotQualified)]
    assert greeter.name == "Susie"


def test_french_greeter() -> None:
    """Ensure the world can make a ``Greeter`` from dependencies."""
    greeter = world[instanceOf[Greeter]().single(qualified_by=FrenchCustomer)]
    assert greeter.name == "Marie"


@pytest.mark.skip(reason="V2 refactoring needed")
def test_default_greeting() -> None:
    """Ensure the world can make a ``Greeting`` from dependencies."""
    # Set the context
    visit_handler = world[VisitHandler]
    visit_handler.set_customer_id("steve")
    greeting = world[instanceOf[Greeting]().single(qualified_by=NotQualified)]
    assert greeting.customer.name == "Steve"
    assert greeting.greeter.name == "Susie"
    assert greeting.punctuation == "!"
    assert str(greeting.salutation) == "Hello"
    assert greeting() == "Hello Steve, my name is Susie!"


@pytest.mark.skip(reason="V2 refactoring needed")
def test_french_greeting() -> None:
    """Ensure the world can make a ``FrenchGreeting`` from dependencies."""
    # Set the context
    visit_handler = world[VisitHandler]
    visit_handler.set_customer_id("jean")
    greeting = world[instanceOf[Greeting]().single(qualified_by=FrenchCustomer)]
    assert greeting.customer.name == "Jean"
    assert greeting.greeter.name == "Marie"
    assert greeting.punctuation == "!"
    assert str(greeting.salutation) == "Bonjour"
    assert greeting() == "Bonjour Jean, je m'appelle Marie!"


@pytest.mark.skip(reason="V2 refactoring needed")
def test_context() -> None:
    """An injectable Context to retrieve current customer."""
    visit_handler = world[VisitHandler]
    visit_handler.set_customer_id("steve")

    @inject
    def this_context(tc: Customer = inject[get_context()]) -> Customer:
        return tc

    tc1 = this_context()
    assert this_context().name == "Steve"

    # Ensure that getting the context again, retrieves same object
    assert this_context() is tc1

    # But changing the scope, resets this
    visit_handler.set_customer_id("jean")
    assert this_context() is not tc1


@pytest.mark.skip(reason="V2 refactoring needed")
def test_main() -> None:
    """Let the pluggable app get our greeting."""
    result = main()
    assert result == "Hello Steve, my name is Susie!"
