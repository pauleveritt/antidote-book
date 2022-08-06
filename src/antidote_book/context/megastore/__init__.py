"""Core logic for the MegaStore pluggable app.

Most of the work is done in plugins. This package provides the common
interfaces, entry points, and shared core logic, etc.
"""

from antidote import QualifiedBy
from antidote import inject
from antidote import instanceOf
from antidote import world

from ..megastore_plugins.customer import ALL_CUSTOMERS
from ..megastore_plugins.customer import DefaultCustomer
from ..megastore_plugins.customer import FrenchCustomer
from ..megastore_plugins.greeting import Greeting
from ..megastore_plugins.visit import VisitHandler
from .predicates import NotQualified


@inject
def get_greeting(
    customer_id: str = "steve",
    visit_handler: VisitHandler = inject.me(),
) -> str:
    """Process a greeting."""
    # Hardwired in this first step
    visit_handler.set_customer_id(customer_id)
    this_customer = ALL_CUSTOMERS[customer_id]
    if isinstance(this_customer, DefaultCustomer):
        greeting = world[instanceOf[Greeting]().single(qualified_by=NotQualified)]
    else:
        greeting = world[
            instanceOf[Greeting]().single(qualified_by=QualifiedBy(FrenchCustomer))
        ]
    return greeting()
