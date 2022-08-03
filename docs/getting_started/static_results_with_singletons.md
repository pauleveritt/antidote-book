# Static Results with Singletons

In Antidote v2, `@injectable` does _not_ return a singleton by default.
This means there can only be one result every produced during the lifetime of that world.
That makes it fast!

But sometimes the results vary.
For example, information in the outside world might change in a way that the Antidote world isn't tracking.

Let's see how to control usage of singletons.

## Random But Static Greeting

We saw in [](using_dataclasses) the `Greeter` that we are injecting:

```{literalinclude} ../../src/antidote_book/using_dataclasses/__init__.py
---
start-at: "@injectable"
end-at: "salutation: str"
---
```

The `@injectable` decorator was shorthand for the default value of an argument.
Spelled in full, it would be `@injectable(singleton=True)`.
Because, by default, Antidote thinks every call to a "factory" will return the same result.

Sometimes that's not true.
Especially, as we'll see in the chapter on `@lazy`, when the factory wraps some outside code.
For our case, what if the `Greeter` (mostly) randomly selected a choice of punctuation marks?
In this case, we need `@injectable(singleton=False)`:

```{literalinclude} ../../src/antidote_book/singletons/__init__.py
---
start-at: "@injectable"
end-at: "self.salutation"
---
```

In this case, the "factory" -- the `Greeter` class initializer -- randomly chooses the value.
(Sure, it's only kinda-random.)

The `greeting` then injects a `Greeter`:

```{literalinclude} ../../src/antidote_book/singletons/__init__.py
---
start-at: "@inject"
end-at: "greeter.salutation"
---
```

Our simple test can then assert that the second run is different...that is, there was no singleton caching:

```{literalinclude} ../../tests/test_singletons.py
---
start-at: "test_shallow"
end-at: "assert actual"
---
```

In fact, this example shows why Antidote makes it easy to test.
Let's look at the unit test:

```{literalinclude} ../../tests/test_singletons.py
---
start-at: "test_greeting"
end-at: "assert actual"
---
```

If the lookup was inside `greeting`, it would be hard to reach the random value from the test.
Thus, how would we know the value?
With injection, we can manually pass in our own `Greeter` (to override injection) and then compare the `salutation`.

Does your application really need to create more than one instance?
Do the inputs to object construction vary each time something asks for the injectable, or all they all known at compile time or first call?
Remember, it isn't just the direct input dependencies, but the dependencies of those dependencies.

## Download Files

- {download}`singletons/__init__.py <../../src/antidote_book/singletons/__init__.py>`
- {download}`tests/test_singletons.py <../../tests/test_singletons.py>`
