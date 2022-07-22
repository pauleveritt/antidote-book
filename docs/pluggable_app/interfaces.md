# Interfaces

Now that we have the layout for a pluggable app, let's start towards the 3 ways of pluggability: extending, replacing, and varying.
In this chapter we lay the groundwork by introducing _interfaces_.

## About Interfaces and Implementations

We want systems where new things can be added, existing things can be replaced, and multiple variations of things can exist.

We're using the word "things", but let's be a little more specific.
What we really want to say is "like a" thing.
For example, for injecting a `Greeting`, you're just interested in something that says it behaves like a `Greeting`.
You're not particularly interested in the specific class for the `Greeting`.

How do we write down the "contract" the says whether something is "like a" `Greeting`?
In Antidote, we can define and register an {doc}`interface <antidote:recipes/interface>` using a `@interface` decorator.
Then, we can register an `@implementation` of that interface.

`@interface` defines something for lookup and `@implementation` defines construction.
Let's see that in action.

## The `Greeting` interface and `DefaultGreeting` Implementation

We'd like a generic concept of `Greeting`, decoupled from the implementation -- or even _implementations_.

First we define the "contract" as an Antidote interface:

```{literalinclude} ../../src/antidote_book/interfaces/megastore_plugins/greeting/__init__.py
---
start-at: "@interface"
end-at: "return"
---
```

We now have a symbol `Greeting` we can use during injection: "Hey, get me a `Greeting`."
But this `Greeting` class is never instantiated.
It's just a marker.
As you can see, `Greeting` is no longer a dataclass, nor does it have a default value on the field.
Strictly speaking, the `name: str` isn't enforced as part of the contract.

Then how do we register the class used to _make_ a `Greeting`?
Using Antidote's `@implements`:

```{literalinclude} ../../src/antidote_book/interfaces/megastore_plugins/greeting/__init__.py
---
start-at: "@implements"
end-at: "return f"
---
```

In this system, as it stands now, there is one implementation of `Greeting`.
If you ask for a `Greeting` -- for example, with `Greeting: Greeting = inject.me()` -- you will get a `DefaultGreeting` instance.

It's important that `DefaultGreeting` subclass `Greeting`.
That is, `DefaultGreeting` must be a subtype of `Greeting`.
Otherwise, Antidote will raise an exception during startup:

```
E   TypeError: <class 'antidote_book.interfaces.megastore_plugins.greeting.DefaultGreeting'> is not a issubclass of <class 'antidote_book.interfaces.megastore_plugins.greeting.Greeting'>, but a <class 'type'>
```

We changed the `Greeting` plugin, now it's time to change the tests.
But wait -- we don't have to!
Everything "just works".
The system doesn't have to know which implementation of `Greeting` was used -- it found the "right" `Greeting`, made an instance using `DefaultGreeting`, and passed it in.

Thus, this test "just works", unchanged:

```{literalinclude} ../../tests/test_interfaces.py
---
start-at: "def test_greeting"
end-at: "assert greeting.salutation"
emphasize-lines: 3
---
```

## Interfaces in Other Plugins

The `Greeting` plugin now does two things:

- Define something called `Greeting` which can be injected
- Define one implementation of `Greeting`, allowing `MegaStore` to work out-of-the-box (OOTB)

Let's apply the same treatment to the other plugins (except `Config` which doesn't define an injectable).
First, `Customer`:

```{literalinclude} ../../src/antidote_book/interfaces/megastore_plugins/customer/__init__.py
---
start-at: "@interface"
end-at: "name: str ="
---
```

Next, `Greeter`:

```{literalinclude} ../../src/antidote_book/interfaces/megastore_plugins/greeter/__init__.py
---
start-at: "@interface"
end-at: "name: str ="
---
```

And that's it -- our pluggable system now has definitions (interfaces) separated from implementations.

TODO Download
