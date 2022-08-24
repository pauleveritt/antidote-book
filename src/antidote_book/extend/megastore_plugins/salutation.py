"""Get a salutation based on time of day."""
from dataclasses import dataclass
from datetime import datetime
from typing import Protocol

from antidote import implements
from antidote import interface


@interface
class Salutation(Protocol):
    """Provide a string-based salutation from list of choices."""

    def __str__(self) -> str:
        """Return the salutation from this implementation."""
        ...


@implements.protocol[Salutation]()
@dataclass
class DefaultSalutation:
    """Give a different salutation based on time of day."""

    choices: tuple[str, ...] = ("Good morning", "Good afternoon")

    def __str__(self) -> str:
        """Different greeting based on time of day."""
        current_time = datetime.now()
        hour = current_time.hour
        return self.choices[0] if hour < 12 else self.choices[1]
