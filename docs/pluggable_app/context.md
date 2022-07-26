# Context

- Create a new `Customer`, either a `DefaultCustomer` or a `FrenchCustomer`
- Put this `Customer` in a well-known place, where anything can inject it
- Each new `Customer` instance replaces the old
- Anything that has `Customer` as a dependency, or something that ultimately depends on it, needs to be re-calculated

## Tests

- pytest fixture
  - default_world
  - french_world
- ## New test_context

## VisitHandler

- Introduce idea of Context
- `get_context` that does NOT set the scope
  - Ensure in test that changing the scope FAILS to get new
- Add scope
  - Ensure that it correctly gets a new one

## Greeting

- Now the greetings can just get the customer directly
- No need to inject VisitHandler and poke at ALL_CUSTOMERS
- When this change is made, suddenly, the `test_french_greeting` starts to fail
  - Because finally, we are injecting the correct customer
  - Fix the test

## Problems

- Still kind of sucks that FrenchGreeting has to "forward" the qualified_by
  - `greeter: Greeter = inject.me(qualified_by=FrenchCustomer)`
  - That's a job for custom predicates
