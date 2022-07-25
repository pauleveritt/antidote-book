# Custom Choosing with Predicates

We just saw something powerful: we could say "only use this implementation in this case."
We also saw how to have a "default" case.

But it wasn't really a default.
We had to make a "DefaultCustomer" and spread the "qualified_by" throughout the codebase, on caller and callee.

Let's use the Antidote concept of "predicates" to simplify this with a `NoQualified` predicte.

## The Problem

- Go to test_default_greeter
  - Change to just world.get, fails
- megastore/**init**
  - Add noqual
