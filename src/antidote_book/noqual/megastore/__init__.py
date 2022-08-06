"""Core logic for the MegaStore pluggable app.

Most of the work is done in plugins. This package provides the common
interfaces, entry points, and shared core logic, etc.
"""
from typing import Type

from antidote import QualifiedBy
from antidote import inject
from antidote import instanceOf
from antidote import world

from ..megastore_plugins.customer import Customer
from ..megastore_plugins.customer import DefaultCustomer
from ..megastore_plugins.greeting import Greeting
from .predicates import NotQualified


@inject
def get_greeting(customer_type: Type[Customer] | None = None) -> str:
    """Process a greeting."""
    if customer_type is None:
        # No customer used
        g1 = world[instanceOf[Greeting]().single(qualified_by=NotQualified)]
    else:
        g1 = world[instanceOf[Greeting]().single(QualifiedBy(DefaultCustomer))]
    return g1()
