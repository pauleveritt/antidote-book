"""Core logic for the MegaStore pluggable app.

Most of the work is done in plugins. This package provides the common
interfaces, entry points, and shared core logic, etc.
"""

from antidote import inject

from ..megastore_plugins.greeting import Greeting


@inject
def get_greeting(greeting: Greeting = inject.me()) -> str:
    """Process a greeting."""
    return greeting()
