"""A local site installation for a store."""
from dataclasses import dataclass

from antidote import implements

from .megastore import get_greeting
from .megastore_plugins.salutation import DefaultSalutation
from .megastore_plugins.salutation import Salutation


@implements(Salutation)
@dataclass
class FrenchSalutation(DefaultSalutation):
    """A salutation for a Quebec store."""

    choices: tuple[str, ...] = ("Bonjour", "Bon après-midi")


def main() -> str:
    """This is the "main loop" for the pluggable app."""
    return get_greeting()
