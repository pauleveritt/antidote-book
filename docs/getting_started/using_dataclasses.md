# Using Dataclasses

We have a bit of boilerplate in our injectable classes.
Like Antidote, Python's dataclasses are type-hinting-friendly.
Let's use them for our injectables.

## Too Much Boilerplate

In [](easy_injection) we saw a plain old class `Greeter` used as an injectable:

```{literalinclude} ../../src/antidote_book/easy_injection/__init__.py
---
start-at: "@injectable"
end-at: "self.salutation"
---
```

That's a bit of boilerplate.
We have an `__init__` initializer where pass in `salutation` with a type hint and default value.
We then do the assignment.

Just the problem dataclasses were meant for!
Let's reduce the boilerplate:

```{literalinclude} ../../src/antidote_book/using_dataclasses/__init__.py
---
start-at: "@injectable"
end-at: "salutation: str"
---
```

Dataclasses have some warts.
But for the purposes in this book, they are perfect: concise and friendly to type hints.

## Download Files

- {download}`using_dataclasses/__init__.py <../../src/antidote_book/using_dataclasses/__init__.py>`
- {download}`tests/test_using_dataclasses.py <../../tests/test_using_dataclasses.py>`
