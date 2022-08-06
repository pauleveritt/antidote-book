# Static Results with Singletons

During injection, Antidote finds the "factory" and then helpful calls it, to construct the thing you were asking for.
Antidote, by default, presumes that everything needed to construct that object is "in the world", so the instance will never change.
It's a "singleton".
That makes it _fast_!

Antidote _also_ supports saying "this injectable is _not_ a singleton."
It might rely on some changing outside state.

Let's see how to make an injectable into a not-singleton.

## Dynamic Salutations

We saw in [](using_dataclasses) the `Greeter` that we are injecting:

```{literalinclude} ../../src/antidote_book/using_dataclasses/__init__.py
---
start-at: "@injectable"
end-at: "salutation: str"
---
```

The `@injectable` decorator was shorthand for the default value of an argument.
Spelled in full, it would be `@injectable(scope="singleton")`.
Because, by default, Antidote thinks every call to an injectable will return the same result.

Sometimes that's not true.
For our case, what if we had `Greeter` that kept a count of each time it was asked for?
In this case, we need `@injectable(scope="instance")`:

```{literalinclude} ../../src/antidote_book/singletons/__init__.py
---
start-at: "@injectable(scope="
end-at: "self.salutation ="
---
```

In this case, the "factory" -- the `CountingGreeter` class initializer -- incremented a global variable.

Let's see this in tests.
First, let's test the singleton case by getting `Greeter`:

```{literalinclude} ../../tests/test_singletons.py
---
start-at: "test_greeter_singleton"
end-at: "assert greeter2"
---
```

We only constructed one `Greeter` instance, so its `__init__` was only run once.

Now let's see a test of `CountingGreeter`:

```{literalinclude} ../../tests/test_singletons.py
---
start-at: "test_greeter_not_singleton"
end-at: "assert greeter2"
---
```

In this case, `CountingGreeter.__init__` ran twice.
Antidote did _not_ treat `CountingGreeter` as a singleton, as we said `scope="instance"`.
Each time the `world` was asked for a `CountingGreeter`, it made a new one.

## Download Files

- {download}`singletons/__init__.py <../../src/antidote_book/singletons/__init__.py>`
- {download}`tests/test_singletons.py <../../tests/test_singletons.py>`
