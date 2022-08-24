# Counter State

- Based on singletons, but

  - Back to a dataclass
  - Just one class

- Add `@state`
- Have `greeting()` inject it
- Show the test

  - Nothing changes until counter.update
  - In fact, if you use debugger,

- Previous counter example
- Write a test that shows the dependency isn't recalculated
- But when state changes, it is recalculated
