# Replacing Built-In Implementations

We now have a pluggable app which defines key pieces -- `Customer`, `Greeter`, etc. -- via interfaces.
The app ships with implementations of these, but what if we want to _replace_ them with a site-local implementation?

Let's show how a site can implement its own `Salutation` -- without forking the plugin's implementation.
Also, without making all the existing code point to our site's `Salutation`.
Everybody will just start getting the overridden one, without even knowing it was added!

# Replacing with `override`

MegaStore has opened a store in Quebec, so the salutations in `DefaultSalutation.choices` should be in French.
The _site_ can override this without having to fork the built-in `DefaultSalutation` nor any callers.

We'll start, of course, with a failing test.
Let's change `test_greeting` and `test_main` to use the French salutations:

```{literalinclude} ../../tests/test_replace.py
---
start-at: "def test_greeting"
emphasize-lines: 7, 14-15
---
```

When we run our tests, we see that they failed, which is good.

Now we start the implementation with a _wrong_ approach.
In `site.py`, let's add a `FrenchSalutation` that implements the `Salutation` interface:

```python
@implements(Salutation)
@dataclass
class FrenchSalutation(DefaultSalutation):
    """A salutation for a Quebec store."""

    choices: tuple[str, ...] = ("Bonjour", "Bon après-midi")
```

This is pretty nice -- the existing `DefaultSalutation.__call__` doesn't have to change, so we can subclass `DefaultSalutation` to re-use it.
Also, we said via `@implements` that `FrenchSalutation` can be used as a `Salutation`.
All good, right?

Wrong!
When we start up the application -- for example, by running our test -- we get an error from Antidote:

```
RuntimeError: Multiple implementations match the interface
<class 'antidote_book.replace.megastore_plugins.salutation.Salutation'> for the constraints []:
<class 'antidote_book.replace.site.FrenchSalutation'> and
<class 'antidote_book.replace.megastore_plugins.salutation.DefaultSalutation'>
```

Now _that's_ a specific exception!
It tells us exactly the problem: the new `@implements` in `site.py` matches the bundled one in the plugin.
Meaning, there are now two classes fighting to be the One True `Salutation`.

The first solution to this is to use [Antidote's `overriding` support](https://antidote.readthedocs.io/en/stable/recipes/interface.html#overriding):

```python
@implements(Salutation).overriding(DefaultSalutation)
@dataclass
class SiteGreeting(DefaultGreeting):
    """A FrenchGreeting for a French store."""

    salutation: str = "Bonjour"
```

We changed just the first line, saying that this _implementation_ should "override" the one at `DefaultSalutation`.
With this in place, our tests now run correctly.

Good, right?

## Setting a `.by_default` Implementation

Alas, this approach is really tied to the choice of implementation.

We'd like our `site` to just think about kinds-of-things, i.e. _interfaces_.
It shouldn't have to do the extra work to go find the implementation it wants to override.

Fortunately Antidote has a better approach, [using `by_default`](https://antidote.readthedocs.io/en/stable/recipes/interface.html#default).
We'll change the `Salutation` plugin to indicate that `DefaultSalutation` should _only_ be used if nothing else is provided.

```{literalinclude} ../../src/antidote_book/replace/megastore_plugins/salutation.py
---
start-at: "@implements(Salutation)"
end-at: class DefaultSalutation
emphasize-lines: 1
---
```

Now our customized `FrenchSalutation` in `site.py` has a simpler `@implements`:

```{literalinclude} ../../src/antidote_book/replace/site.py
---
start-at: "@implements(Salutation)"
end-at: class FrenchSalutation
emphasize-lines: 1
---
```

The tests pass, `mypy` is still happy, and this change had a better "balance of work":

- The _consumer_ in `site.py` had to know less and do less
- The _provider_ in the plugin was more explicit in saying "register this as the default `Salutation`"

Also, any software that uses `Salutation` will get the site's custom salutation.
This is really nice for large ecosystems with lots of plugin authors.
