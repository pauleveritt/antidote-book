# Context

- Create a new `Customer`, either a `DefaultCustomer` or a `FrenchCustomer`
- Put this `Customer` in a well-known place, where anything can inject it
- Each new `Customer` instance replaces the old
- Anything that has `Customer` as a dependency, or something that ultimately depends on it, needs to be re-calculated

- pytest fixture
-
