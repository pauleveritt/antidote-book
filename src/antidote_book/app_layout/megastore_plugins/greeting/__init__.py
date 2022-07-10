"""The message given by a Greeter to a Customer."""
from dataclasses import dataclass

from antidote import injectable, inject

from ..customer import Customer
from ..greeter import Greeter
from ..config import MegaStoreConfig


@injectable
@dataclass
class Greeting:
    """The message given to a customer."""

    customer: Customer = inject.me()
    greeter: Greeter = inject.me()
    punctuation: str = MegaStoreConfig.PUNCTUATION
    salutation: str = "Hello"

    def __call__(self) -> str:
        """Give the text of the greeting."""
        gn = self.greeter.name  # Shorten line
        return f"{self.salutation}, my name is {gn}{self.punctuation}"
