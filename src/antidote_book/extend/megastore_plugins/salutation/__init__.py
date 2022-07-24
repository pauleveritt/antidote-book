"""Get a salutation based on time of day."""
from dataclasses import dataclass
from datetime import datetime
from typing import Protocol

from antidote import interface, implements


@interface
class Salutation(Protocol):
    """Provide a string-based salutation."""

    def __str__(self) -> str:
        """Return the salutation from this implementation."""
        ...


@implements(Salutation)
@dataclass
class DefaultSalutation:
    """Give a different salutation based on time of day."""

    def __str__(self) -> str:
        """Different greeting based on time of day."""

        current_time = datetime.now()
        hour = current_time.hour
        return "Good morning" if hour < 12 else "Good afternoon"
