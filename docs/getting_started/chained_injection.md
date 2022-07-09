# Chained Injection

Injection can depend on something which depends on something.
Antidote is quite good at these "transitive dependencies".
Let's take a look at representing a multistep dependency.

## The Dependency Chain

We have a dependency chain: `greeting` -> `Greeter` -> `Message` -> `Config`.
Let's break it down.

Here's our `greeting` function:

```{literalinclude} ../../src/antidote_book/chained_injection/__init__.py
---
start-at: def greeting
end-at: return f
---
```

:::{admonition} Local Variables
:class: note

The local variables are only there to shorten the line for the f-string.
:::

This function has one dependency: `Greeter`.
We're familiar with that as a `greeting` dependency.
But... it's changed:

```{literalinclude} ../../src/antidote_book/chained_injection/__init__.py
---
start-at: "# inject Greeter"
end-at: "message: Message"
emphasize-lines: 7
---
```

Look at that `message` field!
`Greeter` is an `@injectable` but it is _also_ using injection, and it isn't using it in a function signature.
It's using injection in a dataclass field's default value.

This is pretty cool.
We know that injection helps us get arguments when _we_ call a function such as `greeting`.
But _we_ aren't calling `Greeter`.
The "system" invokes that class when making an instance, and it figures out what needs to be injected.
This has some cool pluggability consequences a bit down the line.

So `Greeter` wants a `Message`.
Let's see the registration for that:

```{literalinclude} ../../src/antidote_book/chained_injection/__init__.py
---
start-at: "# inject Message"
end-at: "punctuation: str"
emphasize-lines: 7
---
```

Kind of the same dance.
It's a dataclass with two fields.
The second field brings back in our `Constant` idea from [](configuration_with_constants).

All in all, our `greeting` function had a dependency, which had a dependency, which had a dependency.
And it was all kicked off with this line:

```{literalinclude} ../../src/antidote_book/chained_injection/__init__.py
---
start-at: "def main"
end-at: "return greeting"
emphasize-lines: 2
---
```

What does the output look like?
Let's look at our "integration" test:

```{literalinclude} ../../tests/test_chained_injection.py
---
start-at: "def test_shallow"
end-at: "assert actual"
emphasize-lines: 4
---
```

Let's look at our "integration" test:

```{literalinclude} ../../tests/test_chained_injection.py
---
start-at: "def test_shallow"
end-at: "assert actual"
emphasize-lines: 4
---
```

## Download Files

- {download}`chained_injection/__init__.py <../../src/antidote_book/chained_injection/__init__.py>`
- {download}`tests/test_chained_injection.py <../../tests/test_chained_injection.py>`
