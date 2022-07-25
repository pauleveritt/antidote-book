# Customer Visits with Scopes

Our `MegaStore` system works so far, but only for the same two customers.
We're using dataclass default field values to assign `Steve` and `Jean`.

Let's see how scopes can let us work with changing data.

## Scopes in Antidote

Each customer visit results in a greeting.
It's like a transaction in a database system or, more accurately, a "request" in a web framework.
Like a web request, data comes in from the outside world and gets converted into data inside the system.

For our system, we want each "visit" to:

- Create a new `Customer`, either a `DefaultCustomer` or a `FrenchCustomer`
- Put this `Customer` in a well-known place, where anything can inject it
- Each new `Customer` instance replaces the old
- Anything that has `Customer` as a dependency, or something that ultimately depends on it, needs to be re-calculated

The last part is quite important.

Fortunately, Antidote has the concept of {doc}`scopes <antidote:recipes/scopes>` to provide this.
This lets you declare a dependency to be 

:::{note} Changes are a-comin'

Antidote has [big plans in V2](https://github.com/Finistere/antidote/discussions/51) for reworking scope.
This book will be updated accordingly.
:::

- Make sure current customer is injectable
- 