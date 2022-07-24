# Protocols

Notes:

- Show the mypy error, discuss all the edge cases
- Need to use `cast` when working with the world directly
- TODO introduce runtime checking

## Previous

We just showed different kinds of `Greeter`.
Let's use `PEP 544 protocols <https://peps.python.org/pep-0544/>`\_ instead of subclasssing.

In our little framework, define `Greeter` as a protocol, then change `DefaultGreeter` to no longer subclass `Greeter`:

Also change our `FrenchGreeter` to no longer subclass from `Greeter`:

## Analysis

This is a small but important change.
Our implementations no longer have to use inheritance.
Instead, their structure complies with the structure of `Greeter`.

Why might you care?
What if you want to use a named tuple as the implementation, or an `attrs` class.
You don't want to have to subclass.
But if you don't, you're no longer a "type of" `Greeter` and Antidote gets made when using the nominal-typing approach.

With protocols, we're using structural typing and `FrenchGreeter` doesn't have to be a "type of" `Greeter`.
It just needs to be something that can be used the same as `Greeter`.

## Downloads

TODO
