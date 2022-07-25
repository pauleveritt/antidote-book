"""Do the shallow and deep tests for the 'extend' example."""

from antidote import inject
from antidote import world

from antidote_book.extend.megastore_plugins.config import MegaStoreConfig
from antidote_book.extend.megastore_plugins.customer import CustomerT
from antidote_book.extend.megastore_plugins.greeter import GreeterT
from antidote_book.extend.megastore_plugins.greeting import GreetingT
from antidote_book.extend.megastore_plugins.salutation import DefaultSalutation
from antidote_book.extend.site import main


def test_default_salutation_str() -> None:
    """Make a DefaultSalutation and check its str representation."""
    salutation = DefaultSalutation()
    assert str(salutation) in ["Good morning", "Good afternoon"]


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


def test_greeter() -> None:
    """Ensure the world can make a ``Greeter`` from dependencies."""
    greeter = world.get(GreeterT)
    assert greeter.name == "Susie"


def test_greeting() -> None:
    """Ensure the world can make a ``Greeting`` from dependencies."""
    greeting = world.get(GreetingT)
    assert greeting.customer.name == "Steve"
    assert greeting.greeter.name == "Susie"
    assert greeting.punctuation == "!"
    assert str(greeting.salutation) in ["Good morning", "Good afternoon"]


def test_main() -> None:
    """Let the pluggable app get our greeting."""
    result = main()
    assert result in [
        "Good morning, my name is Susie!",
        "Good afternoon, my name is Susie!",
    ]
