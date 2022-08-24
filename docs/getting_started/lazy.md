# Outside Code with `lazy`

Sometimes your code uses a class that you don't control, for example from an installed library.
If it doesn't have `@injectable`, you can't inject, it, right?

Not so fast!
Antidote proves the `@lazy` directive to wrap a symbol which you want to inject.

## Foreign Message

Let's return to our `Message` from the previous example in [](chained_injection):

```{literalinclude} ../../src/antidote_book/chained_injection/__init__.py
---
start-at: "# inject Message"
end-at: "punctuation: str"
emphasize-lines: 7
---
```

Imagine that this `Message` was actually imported from a package that we installed.
We want use it as part of our system, but without forking the original.
We need to write some glue code.

To make the example work better, let's remove the `Config.PUNCTUATION` part.
We'll also rename from `Message` to `OutsideMessage` to drive home the point.
The foreign package probably won't use our `Config` system (or likely even Antidote.)

```{literalinclude} ../../src/antidote_book/chained_injection/__init__.py
---
start-at: "# inject Message"
end-at: "punctuation: str"
emphasize-lines: 7
---
```

We'll see though how `Config.PUNCTUATION` makes a re-appearance.

## Wrap That OutsideMessage

What is it we're looking for?

- We want to inject an `OutsideMessage`
- We need a way for the injector to _find_ `OutsideMessage`
- And a "factory" that can construct a `OutsideMessage`
- Unlike `@injectable`, don't cache as a singleton
- That factory needs access to injection, to get the data we want for `OutsideMessage`

Let's write a function that does that and decorate it with Antidote's {doc}`Lazy <antidote:tutorial/5_lazy>` decorator:

```{literalinclude} ../../src/antidote_book/lazy_calls/__init__.py
---
start-at: "@lazy"
end-at: "return OutsideMessage"
---
```

Lots going on here.
First, the directory is kind of like `@injectable` -- it "registers" something.
But what?
The thing it is wrapping isn't a type.

Instead, `@lazy` looks at that callable's _return type hint_.
Fortunately `outside_message` says it returns an `OutsideMessage`.
Antidote uses introspection, grabs the return value, and registers `outside_message` as a factory for `OutsideMessage`.

`OutsideMessage` isn't "one of ours" and obviously doesn't do injection when it is being made.
But we can still do injection in our factory function and then use the injected value when _we_ make an `OutsideMessage`.
That's kind of the secret for `@lazy` -- _we_ are in charge of construction, not Antidote.
Thus, our function signature asks Antidote to grab and inject `punctuation`.
We then pass that value in when we create `OutsideMessage`.

## Injecting an `OutsideMessage`

Now it is set up, and we want to see it in use.
Our `Greeter` is the one that wanted a `Message`.
How does it inject `OutsideMessage` from the `@lazy` factory?

```{literalinclude} ../../src/antidote_book/lazy_calls/__init__.py
---
start-at: "@injectable"
end-at: "message: OutsideMessage"
emphasize-lines: 7
---
```

The dataclass's `message` field has a default value which _injects_ a call to our factory function.
This puts a lazily-evaluated callable into the class definition.
Later, when this `@injectable` class is actually injected, the Antidote injector will look at this field.
It will then do the actual calling of `outside_message`.

Want to know something fun?
Other than imports, the tests for this didn't change:

```{literalinclude} ../../tests/test_lazy_calls.py
---
start-at: "def test_shallow"
end-at: "Hello, my name is From Test"
---
```

## Odds and Ends

This `@lazy` decorator, like `@injectable`, does _not_ default to singleton usage.
The result is calculated on each injection.
Why?
Because an injection of it -- we used `inject[outside_message()]` -- might pass an argument.
For example: `inject[outside_message(punctionation="????")]`.

There might be cases where you want to use a factory function even for injectable classes under your own control.
Then again, Antidote provides a number of protocols to control injectable creation, directly on the class, with resorting to a separate factory function.

As noted in the {doc}`docs on lazy <antidote:tutorial/5_lazy>`, the call to the function is like a normal function.
You can pass arguments to parameterize the usage.

## Download Files

- {download}`lazy_calls/__init__.py <../../src/antidote_book/lazy_calls/__init__.py>`
- {download}`tests/test_lazy_calls.py <../../tests/test_lazy_calls.py>`
