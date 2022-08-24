"""Core logic for the MegaStore pluggable app.

Most of the work is done in plugins. This package provides the common
interfaces, entry points, and shared core logic, etc.
"""
from typing import Type

from antidote import inject
from antidote import instanceOf
from antidote import world

from ..megastore_plugins.customer import Customer
from ..megastore_plugins.customer import DefaultCustomer
from ..megastore_plugins.greeting import Greeting


@inject
def get_greeting(customer_type: Type[Customer] = DefaultCustomer) -> str:
    """Process a greeting."""
    g1 = world[instanceOf[Greeting]().single(qualified_by=customer_type)]
    return g1()
