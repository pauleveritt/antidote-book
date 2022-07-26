# Customer Visits with Scopes

Our `MegaStore` system works so far, but only for the same two customers.
We're using dataclass default field values to assign `Steve` and `Jean`.

Let's see how scopes can let us work with changing data.

## Scopes in Antidote

Each customer visit results in a greeting.
It's like a transaction in a database system or, more accurately, a "request" in a web framework.
Like a web request, data comes in from the outside world and gets converted into data inside the system.

For our system, we want each "visit" to:

- Collect information about the visit
- Make this visit information easily accessible, i.e. injectable
- Use this visit information to retrieve the current customer from a mini-database
- Anything that depends on this visit information should be cleared from cache on each visit

The last part is quite important.

Fortunately, Antidote has the concept of {doc}`scopes <antidote:recipes/scopes>` to provide this.
This lets you declare a dependency to be

:::{note} Changes are a-comin'

Antidote has [big plans in V2](https://github.com/Finistere/antidote/discussions/51) for reworking scope.
This book will be updated accordingly.
:::

## Failing Tests

- We want "Hello Steve" and "Bonjour Jean"
- This means `test_default_greeting`, `test_french_greeting`, and `test_main`
- The first two need to grab the VisitHandler and set the customer from a database

## VisitHandler

- We need a new plugin `Visit`
- It has a "stateful factory", a `VisitHandler`, which manages changing `Visit` state
- It has two public interfaces
  - A method to change the current customer ID
  - Access to the visit as the `current` attribute
- Is "bound to the scope"
  - Define `VISIT_SCOPE`
  - `@factory` uses that scope as an argument, to trigger cache clear when scope is reset
  - `set_customer` triggers scope reset
- The `__call__` is part of the factory protocol in Antidote
  - It's called when a value is asked for via `inject.me(source=VisitHandler)`
  - This lets us inject a `Visit` via the stateful `VisitHandler`

## Customers

- Define an ALL_CUSTOMERS database of instances

## Greeting

- DefaultGreeting and FrenchGreeting
  - Import the database
  - Inject the `Visit` using `source=VisitHandler`
  - Grab current customer_id, then customer, then name
  - Use that in the f-string

## Megastore

- Import customers db
- In get_greeting
- Change signature to call it with a customer_id, then inject the visit_handler
- Call visit handler to set the current customer_id
- Qualified `Greeting` lookup based on the type of the current customer
  - Use passed-in customer_id to get the customer instance

## Problems

- Too much importing of the customer DB
- Customer is being injected but isn't used
  - Have to instead inject VisitHandler each time and get the right customer from the db
- Would be nice to inject current customer
- Greeting test is testing the injection of Customer, etc.
  - Should learn to trust the injector
