"""Do the shallow and deep tests for the `vary` example."""

from antidote import inject
from antidote import world

from antidote_book.vary.megastore_plugins.config import MegaStoreConfig
from antidote_book.vary.megastore_plugins.customer import CustomerT
from antidote_book.vary.megastore_plugins.customer import DefaultCustomer
from antidote_book.vary.megastore_plugins.customer import FrenchCustomer
from antidote_book.vary.megastore_plugins.greeter import GreeterT
from antidote_book.vary.megastore_plugins.greeting import GreetingT
from antidote_book.vary.site import main


def test_config() -> None:
    """Ensure MegaStore has config-driven injectable punctuation."""

    @inject
    def get_punctuation(punctuation: str = MegaStoreConfig.PUNCTUATION) -> str:
        return punctuation

    this_punctuation = get_punctuation()
    assert this_punctuation == "!"


def test_customer() -> None:
    """Ensure the world can make a ``Customer`` from dependencies."""
    customer = world.get(CustomerT)
    assert customer.name == "Steve"


def test_default_greeter() -> None:
    """Ensure the world can make a ``Greeter`` from dependencies."""
    greeter = world.get[GreeterT].single(qualified_by=DefaultCustomer)
    assert greeter.name == "Susie"


def test_french_greeter() -> None:
    """Ensure the world can make a ``Greeter`` from dependencies."""
    greeter = world.get[GreeterT].single(qualified_by=FrenchCustomer)
    assert greeter.name == "Marie"


def test_default_greeting() -> None:
    """Ensure the world can make a ``Greeting`` from dependencies."""
    greeting = world.get[GreetingT].single(qualified_by=DefaultCustomer)
    assert greeting.customer.name == "Steve"
    assert greeting.greeter.name == "Susie"
    assert greeting.punctuation == "!"
    assert str(greeting.salutation) == "Hello"
    assert greeting() == "Hello, my name is Susie!"


def test_french_greeting() -> None:
    """Ensure the world can make a ``FrenchGreeting`` from dependencies."""
    greeting = world.get[GreetingT].single(qualified_by=FrenchCustomer)
    assert greeting.customer.name == "Steve"
    assert greeting.greeter.name == "Marie"
    assert greeting.punctuation == "!"
    assert str(greeting.salutation) == "Bonjour"
    assert greeting() == "Bonjour, je m'appelle Marie!"


def test_main() -> None:
    """Let the pluggable app get our greeting."""
    result = main()
    assert result == "Hello, my name is Susie!"
