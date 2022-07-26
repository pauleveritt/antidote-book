# TODO

## Now

- Get rid of **init**.py for all components to ease changing files

## Next

- Sybil etc. for docstring-based storytelling
- Move get_greeting to Greeting plugin
- Write good docstrings
- Get "Hello Kevin, my name is" customer.name in earlier

## Soon

- Fix any cut-and-paste docstring violations
- Constantly remind people that civilians won't write this, they will consume it
  - You're giving them well-managed, domain-specific entities
- Re-invent test writing to provide alternates passed in for injection
  - Rather than use a world all the time
  - Have a local function in the test
    - Which has an assert itself
- More comments on included code
- Move the cast thing to a top-level "const" and re-use
- Get preface type chapters in place
- Consider mixing in some doctest
- Setup api docs and make good docstrings
- In singletons, introduce debugger to prove it only runs once
- In first usage of `world.get[Something](Something)` clarify the double usage

## Later

- Each example module is in the api docs and can be linked to via "Files:"
- Start each chapter with a context-free example done with a doctest
- Clean out top README
- Emphasize PyCharm screenshots and mypy results
- Clean out unused top-level docs
- Add ref targets in Antidote Sphinx docs

## Done

- Organize outline
- Decide on the `main` and `test` function ideas
- GreeterT when cast appears
